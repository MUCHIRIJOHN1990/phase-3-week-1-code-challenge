# phase-3-week-1-code-challenge

Based on the contents of `functions.py`, here's a revised `README.md` file that reflects the functionality provided:

---

# Project Overview

## Table of Contents

- [phase-3-week-1-code-challenge](#phase-3-week-1-code-challenge)
- [Project Overview](#project-overview)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview-1)
  - [Installation](#installation)
  - [Usage](#usage)
  - [functions.py](#functionspy)

## Project Overview

This project contains a single Python file, `functions.py`, with various utility functions and a class. These include functions for mathematical operations, string manipulation, dictionary merging, and sorting, as well as a class for representing cars. 

## Installation

No special installation is required beyond having Python installed. Simply clone the repository and ensure you have Python 3.x installed.

## Usage

To use the functions and class in `functions.py`, you can import them into your Python scripts. Here's an example of how to use them:

```python
from functions import add_numbers, reverse_string, count_vowels, calculate_factorial, decorator_func, sort_by_age, merge_dicts, Car

# Example usage of functions
print(add_numbers(5, 3))  # Output: 8
print(reverse_string("hello"))  # Output: "olleh"
print(count_vowels("hello"))  # Output: 2
print(calculate_factorial(5))  # Output: 120

# Using decorator_func
@decorator_func
def say_hello():
    print("Hello!")

say_hello()
# Output: Decorator Applied
#         Hello!

# Sorting a list by age
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
print(sort_by_age(people))  # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]

# Merging dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dicts(dict1, dict2))  # Output: {'a': 1, 'b': 5, 'c': 4}

# Using Car class
car = Car("Toyota", "Corolla", 2021)
car.display_info()
# Output: Car Information: Make - Toyota, Model - Corolla, Year - 2021
```

## functions.py

This file includes:

- **Functions**:
  - **`add_numbers(num1, num2)`**: Returns the sum of two numbers.
  - **`is_even(number)`**: Checks if a number is even.
  - **`reverse_string(text)`**: Reverses the given string using a loop.
  - **`count_vowels(text)`**: Counts the number of vowels in a given string.
  - **`calculate_factorial(n)`**: Calculates the factorial of a non-negative integer.
  - **`decorator_func(func)`**: A decorator that prints a message before calling the function.
  - **`sort_by_age(list_of_tuples)`**: Sorts a list of tuples (name, age) by age in ascending order.
  - **`merge_dicts(dict1, dict2)`**: Merges two dictionaries, summing values of common keys.

- **Class**:
  - **`Car`**:
    - **Attributes**: `make`, `model`, `year`.
    - **Methods**:
      - **`__init__(self, make, model, year)`**: Initializes the car's attributes.
      - **`display_info(self)`**: Displays the car’s make, model, and year.
