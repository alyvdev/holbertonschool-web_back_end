# Python Variable Annotations

## Introduction
This project focuses on Python variable annotations, a feature introduced in Python 3.5. Variable annotations provide a way to attach type hints to variables, improving code readability and aiding in static type checking.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Getting Started
To get started with Python variable annotations, ensure you have Python 3.5 or later installed. You can check your Python version by running:
```sh
python --version
```

## Usage
Variable annotations are used to specify the expected type of a variable. They do not enforce type checking at runtime but can be used by tools like `mypy` for static type checking.

### Syntax
```python
variable_name: type = value
```

### Example
```python
age: int = 25
name: str = "John Doe"
height: float = 5.9
```

## Examples
Here are some examples of how to use variable annotations in Python:

### Basic Annotations
```python
x: int = 10
y: float = 20.5
name: str = "Alice"
is_active: bool = True
```

### Function Annotations
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

### Complex Types
```python
from typing import List, Dict

numbers: List[int] = [1, 2, 3, 4, 5]
user_info: Dict[str, str] = {"name": "Bob", "email": "bob@example.com"}
```

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.