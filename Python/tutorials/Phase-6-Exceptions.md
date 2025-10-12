# Python Programming - Intermediate & Advanced Guide

## Table of Contents
8. [Exception Handling](#exception-handling)
9. [File I/O](#file-io)
10. [Object-Oriented Programming](#object-oriented-programming)
11. [Modules and Packages](#modules-and-packages)
12. [Advanced Topics](#advanced-topics)

---

## Exception Handling

Exception handling allows you to gracefully handle errors in your code.

### Basic Exception Handling:

```python
# Basic try-except
def safe_divide(a, b):
    """Safely divide two numbers."""
    try:
        result = a / b
        return f"{a} / {b} = {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Invalid input types!"

print("Exception Handling:")
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "hello"))

# Multiple exceptions
def process_list(data, index):
    """Process a list element safely."""
    try:
        value = data[index]
        result = 100 / value
        return f"Result: {result}"
    except IndexError:
        return "Error: Index out of range!"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except (TypeError, ValueError) as e:
        return f"Error: Invalid data type - {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

test_data = [1, 2, 0, 4, 5]
print(f"\nProcessing list: {test_data}")
print(process_list(test_data, 0))  # Normal case
print(process_list(test_data, 2))  # Zero division
print(process_list(test_data, 10)) # Index error
```

**Output:**
```
Exception Handling:
10 / 2 = 5.0
Error: Cannot divide by zero!
Error: Invalid input types!

Processing list: [1, 2, 0, 4, 5]
Result: 100.0
Error: Cannot divide by zero!
Error: Index out of range!
```

### Advanced Exception Handling:

```python
# try-except-else-finally
def read_file_safely(filename):
    """Read a file with proper exception handling."""
    try:
        # Simulate file operations
        if filename == "nonexistent.txt":
            raise FileNotFoundError("File not found")
        
        content = f"Content of {filename}"
        print(f"File read successfully: {filename}")
        return content
    
    except FileNotFoundError as e:
        print(f"File error: {e}")
        return None
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    
    else:
        print("File operation completed without errors")
    
    finally:
        print("Cleanup operations completed")

print("Advanced Exception Handling:")
read_file_safely("data.txt")
print()
read_file_safely("nonexistent.txt")

# Custom exceptions
class CustomValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_age(age):
    """Validate age with custom exception."""
    try:
        age = int(age)
        if age < 0:
            raise CustomValidationError("Age cannot be negative")
        elif age > 150:
            raise CustomValidationError("Age seems unrealistic")
        return f"Valid age: {age}"
    except ValueError:
        raise CustomValidationError("Age must be a number")

print(f"\nCustom Exception Examples:")
try:
    print(validate_age("25"))
    print(validate_age("-5"))
except CustomValidationError as e:
    print(f"Validation error: {e}")
```

**Output:**
```
Advanced Exception Handling:
File read successfully: data.txt
File operation completed without errors
Cleanup operations completed

File error: File not found
Cleanup operations completed

Custom Exception Examples:
Valid age: 25
Validation error: Age cannot be negative
```

---
