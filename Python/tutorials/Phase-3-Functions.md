# Python Programming - Intermediate & Advanced Guide

## Table of Contents
7. [Functions](#functions)

---

## Functions

Functions are reusable blocks of code that perform specific tasks.

### Function Basics:

```python
# Basic function definition
def greet(name):
    """Greet a person with their name."""
    return f"Hello, {name}!"

# Function with default parameters
def introduce(name, age=25, city="Unknown"):
    """Introduce a person with optional parameters."""
    return f"Hi, I'm {name}, {age} years old, from {city}"

# Function with multiple return values
def calculate_circle(radius):
    """Calculate area and circumference of a circle."""
    import math
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

print("Function Examples:")
print(greet("Alice"))
print(introduce("Bob"))
print(introduce("Charlie", 30, "New York"))

area, circumference = calculate_circle(5)
print(f"Circle (r=5): Area = {area:.2f}, Circumference = {circumference:.2f}")
```

**Output:**
```
Function Examples:
Hello, Alice!
Hi, I'm Bob, 25 years old, from Unknown
Hi, I'm Charlie, 30 years old, from New York
Circle (r=5): Area = 78.54, Circumference = 31.42
```

### Advanced Functions:

```python
# *args and **kwargs
def flexible_function(*args, **kwargs):
    """Function that accepts any number of arguments."""
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")
    
    total = sum(args) if args else 0
    print(f"Sum of positional args: {total}")

print("Flexible Function:")
flexible_function(1, 2, 3, name="Alice", age=25)

# Lambda functions
square = lambda x: x ** 2
add = lambda x, y: x + y

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(f"\nLambda Functions:")
print(f"Original: {numbers}")
print(f"Squared: {squared_numbers}")
print(f"Add 5 + 3 = {add(5, 3)}")

# Higher-order functions
def apply_operation(numbers, operation):
    """Apply an operation to a list of numbers."""
    return [operation(num) for num in numbers]

def cube(x):
    return x ** 3

cubed_numbers = apply_operation([1, 2, 3, 4], cube)
print(f"Cubed numbers: {cubed_numbers}")

# Decorator example
def timing_decorator(func):
    """Decorator to measure function execution time."""
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    """A function that takes some time to execute."""
    import time
    time.sleep(0.1)  # Simulate work
    return "Done!"

print(f"\nDecorator Example:")
result = slow_function()
print(f"Result: {result}")
```

**Output:**
```
Flexible Function:
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Alice', 'age': 25}
Sum of positional args: 6

Lambda Functions:
Original: [1, 2, 3, 4, 5]
Squared: [1, 4, 9, 16, 25]
Add 5 + 3 = 8
Cubed numbers: [1, 8, 27, 64]

Decorator Example:
slow_function took 0.1001 seconds
Result: Done!
```

---
