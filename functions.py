def add_numbers(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

def is_even(number):
    """Checks if a number is even."""
    return number % 2 == 0

def reverse_string(text):
    """Reverses the given string using a loop."""
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text  # Prepend each character to build the reversed string
    return reversed_text

def count_vowels(text):
    """Counts the number of vowels in a given string."""
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

def calculate_factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def decorator_func(func):
    """A decorator that prints a message before calling the function."""
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def sort_by_age(list_of_tuples):
    """Sorts a list of tuples (name, age) by age in ascending order."""
    return sorted(list_of_tuples, key=lambda x: x[1])

def merge_dicts(dict1, dict2):
    """Merges two dictionaries, summing values of common keys."""
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

class Car:
    """A class representing a car."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Displays the car's information."""
        print(f"Car Information: Make - {self.make}, Model - {self.model}, Year - {self.year}")

