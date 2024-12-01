# Python Async Function

This repository contains examples and exercises related to Python's asynchronous programming capabilities using `asyncio`. Below is a brief description of each file in this project:

## Files

### `0-basic_async_syntax.py`
This script contains a basic example of an asynchronous function:
- `wait_random(max_delay: int = 10) -> float`: Asynchronously waits for a random delay between 0 and `max_delay` seconds and returns the actual delay.

### `1-concurrent_coroutines.py`
This script demonstrates running multiple asynchronous tasks concurrently:
- `wait_n(n: int, max_delay: int) -> List[float]`: Runs `n` instances of `wait_random` concurrently and returns a list of the delays in the order they complete.

### `2-measure_runtime.py`
This script measures the runtime of running multiple asynchronous tasks:
- `measure_time(n: int, max_delay: int) -> float`: Measures the total runtime for running `wait_n(n, max_delay)` and returns the average time per task.

### `3-tasks.py`
This script shows how to create and return an asyncio Task:
- `task_wait_random(max_delay: int) -> asyncio.Task`: Creates and returns an asyncio Task for `wait_random`.

### `4-tasks.py`
This script modifies `wait_n` to use tasks:
- `task_wait_n(n: int, max_delay: int) -> List[float]`: Similar to `wait_n`, but uses `task_wait_random` to create tasks.

## Usage

To run any of these scripts, you need to have Python 3.7 or higher installed. You can execute the scripts using the following command:

```sh
python3 script_name.py
```

Replace `script_name.py` with the name of the script you want to run.

## License

This project is licensed under the MIT License.
