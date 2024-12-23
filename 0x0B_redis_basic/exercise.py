import redis
import uuid
from typing import Callable, Union
from functools import wraps

# Decorator to count method calls
def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Increment the call count in Redis
        method_name = method.__qualname__
        self._redis.incr(method_name)
        # Call the original method
        return method(self, *args, **kwargs)
    return wrapper

# Decorator to store the history of calls (inputs and outputs)
def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Generate keys for inputs and outputs
        method_name = method.__qualname__
        inputs_key = f"{method_name}:inputs"
        outputs_key = f"{method_name}:outputs"

        # Store inputs as strings in Redis lists
        self._redis.rpush(inputs_key, str(args))

        # Call the original method
        result = method(self, *args, **kwargs)

        # Store outputs in Redis lists
        self._redis.rpush(outputs_key, str(result))

        return result
    return wrapper

class Cache:
    def __init__(self):
        # Initialize Redis client and flush the DB
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Generate a random UUID key
        key = str(uuid.uuid4())
        # Store the data in Redis
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, int, bytes]:
        # Get the value from Redis
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            # Apply the conversion function if provided
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        return self.get(key, fn=int)

    @count_calls  # Apply the count_calls decorator
    @call_history  # Apply the call_history decorator
    def store(self, data: Union[str, bytes, int, float]) -> str:
        # This store method is decorated
        key = self.store(data)  # Delegate to the original store method
        return key

    def replay(self, method: Callable) -> None:
        method_name = method.__qualname__
        inputs_key = f"{method_name}:inputs"
        outputs_key = f"{method_name}:outputs"

        # Retrieve the inputs and outputs from Redis
        inputs = self._redis.lrange(inputs_key, 0, -1)
        outputs = self._redis.lrange(outputs_key, 0, -1)

        print(f"{method_name} was called {len(inputs)} times:")

        for input_data, output_data in zip(inputs, outputs):
            # Decode inputs and outputs
            input_data = input_data.decode("utf-8")
            output_data = output_data.decode("utf-8")
            print(f"{method_name}({input_data}) -> {output_data}")
