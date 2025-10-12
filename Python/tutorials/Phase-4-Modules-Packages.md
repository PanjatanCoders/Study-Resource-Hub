# Python Programming - Intermediate & Advanced Guide

## Table of Contents
11. [Modules and Packages](#modules-and-packages)

---

## Modules and Packages

Modules help organize code into separate files, making it reusable and maintainable.

### Creating and Using Modules:

```python
# math_utils.py (example module content)
math_utils_content = '''
"""
Math utilities module
Provides common mathematical functions
"""

import math

def factorial(n):
    """Calculate factorial of a number."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """Generate fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

# Module-level variable
PI = 3.14159

# Module initialization
print("Math utils module loaded!")
'''

# Create the module file (simulation)
print("Creating math_utils module...")

# Using built-in modules
import os
import sys
import datetime
import random

print("Built-in Modules Demo:")
print(f"Current directory: {os.getcwd()}")
print(f"Python version: {sys.version}")
print(f"Current time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Random number: {random.randint(1, 100)}")

# Different ways to import
from math import sqrt, pi
import math as m

print(f"\nImport Examples:")
print(f"Square root of 16: {sqrt(16)}")
print(f"Pi value: {pi}")
print(f"Cosine of pi: {m.cos(pi)}")

# Module aliasing
import datetime as dt
now = dt.datetime.now()
print(f"Current year: {now.year}")
```

**Output:**
```
Creating math_utils module...
Built-in Modules Demo:
Current directory: /current/path
Python version: 3.x.x
Current time: 2025-01-15 10:30:45
Random number: 42

Import Examples:
Square root of 16: 4.0
Pi value: 3.141592653589793
Cosine of pi: -1.0
Current year: 2025
```

### Package Structure and __init__.py:

```python
# Demonstrating package structure
package_structure = """
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        submodule.py
"""

print("Package Structure:")
print(package_structure)

# __init__.py example content
init_content = '''
"""
Package initialization file
"""

# Import modules to make them available at package level
from .module1 import function1
from .module2 import Class2

# Package-level variables
__version__ = "1.0.0"
__author__ = "Python Developer"

# Package initialization code
print("Package initialized!")

# Define what gets imported with "from package import *"
__all__ = ["function1", "Class2", "CONSTANT"]

CONSTANT = "Package constant"
'''

print("__init__.py content example:")
print(init_content)

# Simulating module usage
def simulate_module_usage():
    """Simulate using a custom module."""
    
    # Simulated math_utils functions
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    print("\nSimulated Module Usage:")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Is 15 prime? {is_prime(15)}")

simulate_module_usage()
```

**Output:**
```
Package Structure:
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        submodule.py

__init__.py content example:
"""
Package initialization file
"""

# Import modules to make them available at package level
from .module1 import function1
from .module2 import Class2

# Package-level variables
__version__ = "1.0.0"
__author__ = "Python Developer"

# Package initialization code
print("Package initialized!")

# Define what gets imported with "from package import *"
__all__ = ["function1", "Class2", "CONSTANT"]

CONSTANT = "Package constant"

Simulated Module Usage:
Factorial of 5: 120
Is 17 prime? True
Is 15 prime? False
```

---
