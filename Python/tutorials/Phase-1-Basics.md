# Python Programming - Complete Study Guide

## Table of Contents
1. [Introduction to Python](#introduction-to-python)
2. [Identifiers](#identifiers)
3. [Variables](#variables)
4. [Comments](#comments)
5. [Indentation Importance](#indentation-importance)
6. [Operators](#operators)
7. [Conditions (If-Else Statements)](#conditions-if-else-statements)
8. [Loops](#loops)

---

## Introduction to Python

Python is a high-level, interpreted programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991.

### Key Features of Python:
- **Easy to learn and use**
- **Interpreted language** (no compilation needed)
- **Cross-platform** (runs on Windows, Mac, Linux)
- **Large standard library**
- **Object-oriented programming support**
- **Free and open source**

### Why Learn Python?
- Web development
- Data science and analytics
- Artificial Intelligence and Machine Learning
- Automation and scripting
- Desktop applications

---

## Identifiers

Identifiers are names used to identify variables, functions, classes, modules, etc. in Python.

### Rules for Identifiers:
1. Must start with a letter (a-z, A-Z) or underscore (_)
2. Can contain letters, digits (0-9), and underscores
3. Case-sensitive (Age and age are different)
4. Cannot be a Python keyword
5. No special characters allowed (@, #, $, %, etc.)

### Examples:

```python
# Valid Identifiers
name = "John"
age = 25
_private = "secret"
student_1 = "Alice"
myVariable = 100
CLASS_NAME = "Python"

# Invalid Identifiers (These will cause errors)
# 2name = "Invalid"      # Starts with digit
# my-name = "Invalid"    # Contains hyphen
# class = "Invalid"      # Python keyword
# my@name = "Invalid"    # Contains special character

print("Valid identifier examples:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Student: {student_1}")
```

**Output:**
```
Valid identifier examples:
Name: John
Age: 25
Student: Alice
```

### Python Keywords (Reserved Words):
```python
import keyword
print("Python Keywords:")
print(keyword.kwlist)
```

**Output:**
```
Python Keywords:
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

---

## Variables

Variables are containers that store data values. In Python, you don't need to declare the type of variable explicitly.

### Variable Assignment:

```python
# Different types of variables
name = "Python"           # String
age = 25                  # Integer
height = 5.9             # Float
is_student = True        # Boolean
marks = [85, 90, 78]     # List

print("Variable Examples:")
print(f"Name: {name} (Type: {type(name)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"Height: {height} (Type: {type(height)})")
print(f"Is Student: {is_student} (Type: {type(is_student)})")
print(f"Marks: {marks} (Type: {type(marks)})")
```

**Output:**
```
Variable Examples:
Name: Python (Type: <class 'str'>)
Age: 25 (Type: <class 'int'>)
Height: 5.9 (Type: <class 'float'>)
Is Student: True (Type: <class 'bool'>)
Marks: [85, 90, 78] (Type: <class 'list'>)
```

### Multiple Assignment:

```python
# Multiple variables in one line
a, b, c = 10, 20, 30
print(f"a = {a}, b = {b}, c = {c}")

# Same value to multiple variables
x = y = z = 100
print(f"x = {x}, y = {y}, z = {z}")

# Swapping variables
num1 = 5
num2 = 10
print(f"Before swap: num1 = {num1}, num2 = {num2}")

num1, num2 = num2, num1
print(f"After swap: num1 = {num1}, num2 = {num2}")
```

**Output:**
```
a = 10, b = 20, c = 30
x = 100, y = 100, z = 100
Before swap: num1 = 5, num2 = 10
After swap: num1 = 10, num2 = 5
```

---

## Comments

Comments are used to explain code and make it more readable. Python ignores comments during execution.

### Types of Comments:

```python
# This is a single-line comment
print("Hello, World!")  # Comment at end of line

# Multi-line comments using triple quotes
"""
This is a multi-line comment
You can write multiple lines here
Very useful for documentation
"""

'''
This is also a multi-line comment
using single quotes
'''

def greet(name):
    """
    This is a docstring comment
    Used to document functions, classes, and modules
    
    Args:
        name (str): The name to greet
    
    Returns:
        str: Greeting message
    """
    return f"Hello, {name}!"

print(greet("Student"))

# Comments for code organization
# ===============================
# SECTION 1: Variable Declaration
# ===============================
student_name = "Alice"
student_grade = "A+"

# ===============================
# SECTION 2: Display Information
# ===============================
print(f"Student: {student_name}")
print(f"Grade: {student_grade}")
```

**Output:**
```
Hello, World!
Hello, Student!
Student: Alice
Grade: A+
```

---

## Indentation Importance

Python uses indentation to define code blocks instead of braces {}. This is a unique feature of Python.

### Why Indentation Matters:

```python
# Correct indentation
age = 18
if age >= 18:
    print("You are eligible to vote")
    print("Please register yourself")
else:
    print("You are not eligible to vote")
    print("Wait for some more years")

print("Thank you!")

# Example with nested indentation
marks = 85
if marks >= 90:
    print("Grade: A+")
    if marks == 100:
        print("Perfect score!")
    else:
        print("Excellent work!")
elif marks >= 80:
    print("Grade: A")
    print("Good job!")
else:
    print("Grade: B or below")
    print("Keep trying!")
```

**Output:**
```
You are eligible to vote
Please register yourself
Thank you!
Grade: A
Good job!
```

### Indentation Rules:
- Use 4 spaces per indentation level (recommended)
- Be consistent throughout your code
- All lines at the same level must have the same indentation
- Python will show `IndentationError` if indentation is incorrect

```python
# Example of function with proper indentation
def calculate_area(length, width):
    """Calculate area of rectangle"""
    area = length * width
    if area > 100:
        print("Large rectangle")
    else:
        print("Small rectangle")
    return area

result = calculate_area(10, 8)
print(f"Area: {result}")
```

**Output:**
```
Small rectangle
Area: 80
```

---

## Operators

Operators are symbols that perform operations on variables and values.

### 1. Arithmetic Operators:

```python
a = 10
b = 3

print("Arithmetic Operators:")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponent: {a} ** {b} = {a ** b}")
```

**Output:**
```
Arithmetic Operators:
Addition: 10 + 3 = 13
Subtraction: 10 - 3 = 7
Multiplication: 10 * 3 = 30
Division: 10 / 3 = 3.3333333333333335
Floor Division: 10 // 3 = 3
Modulus: 10 % 3 = 1
Exponent: 10 ** 3 = 1000
```

### 2. Comparison Operators:

```python
x = 15
y = 10

print("Comparison Operators:")
print(f"{x} == {y}: {x == y}")  # Equal to
print(f"{x} != {y}: {x != y}")  # Not equal to
print(f"{x} > {y}: {x > y}")    # Greater than
print(f"{x} < {y}: {x < y}")    # Less than
print(f"{x} >= {y}: {x >= y}")  # Greater than or equal
print(f"{x} <= {y}: {x <= y}")  # Less than or equal
```

**Output:**
```
Comparison Operators:
15 == 10: False
15 != 10: True
15 > 10: True
15 < 10: False
15 >= 10: True
15 <= 10: False
```

### 3. Logical Operators:

```python
p = True
q = False

print("Logical Operators:")
print(f"p and q: {p and q}")    # Logical AND
print(f"p or q: {p or q}")      # Logical OR
print(f"not p: {not p}")        # Logical NOT

# Practical example
age = 20
has_license = True

can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")
```

**Output:**
```
Logical Operators:
p and q: False
p or q: True
not p: False
Can drive: True
```

### 4. Assignment Operators:

```python
# Basic assignment
num = 10
print(f"Initial value: {num}")

# Compound assignment operators
num += 5    # num = num + 5
print(f"After += 5: {num}")

num -= 3    # num = num - 3
print(f"After -= 3: {num}")

num *= 2    # num = num * 2
print(f"After *= 2: {num}")

num /= 4    # num = num / 4
print(f"After /= 4: {num}")

num **= 2   # num = num ** 2
print(f"After **= 2: {num}")
```

**Output:**
```
Initial value: 10
After += 5: 15
After -= 3: 12
After *= 2: 24
After /= 4: 6.0
After **= 2: 36.0
```

---

## Conditions (If-Else Statements)

Conditional statements allow you to execute different code blocks based on certain conditions.

### Basic If-Else:

```python
# Simple if-else
temperature = 25

if temperature > 30:
    print("It's hot outside!")
else:
    print("Weather is pleasant")

# If-elif-else
marks = 78

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Marks: {marks}, Grade: {grade}")
```

**Output:**
```
Weather is pleasant
Marks: 78, Grade: B
```

### Nested If Statements:

```python
age = 20
has_id = True

if age >= 18:
    print("You are an adult")
    if has_id:
        print("You can enter the club")
    else:
        print("Please bring your ID")
else:
    print("You are a minor")
    print("Entry not allowed")
```

**Output:**
```
You are an adult
You can enter the club
```

### Practical Example - Calculator:

```python
def simple_calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    if operator == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operator == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operator == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid operator!")

# Example usage (simulated input)
num1, operator, num2 = 10, '+', 5
if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
```

**Output:**
```
10 + 5 = 15
```

---

## Loops

Loops are used to execute a block of code repeatedly.

### 1. For Loop:

```python
# Basic for loop with range
print("Numbers 1 to 5:")
for i in range(1, 6):
    print(f"Number: {i}")

print("\nEven numbers from 2 to 10:")
for i in range(2, 11, 2):
    print(f"Even: {i}")

# For loop with list
fruits = ["apple", "banana", "cherry", "date"]
print("\nFruits list:")
for fruit in fruits:
    print(f"I like {fruit}")

# For loop with string
word = "Python"
print(f"\nLetters in '{word}':")
for letter in word:
    print(letter)
```

**Output:**
```
Numbers 1 to 5:
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5

Even numbers from 2 to 10:
Even: 2
Even: 4
Even: 6
Even: 8
Even: 10

Fruits list:
I like apple
I like banana
I like cherry
I like date

Letters in 'Python':
P
y
t
h
o
n
```

### 2. While Loop:

```python
# Basic while loop
count = 1
print("Counting with while loop:")
while count <= 5:
    print(f"Count: {count}")
    count += 1

# While loop with condition
number = 16
print(f"\nFinding factors of {number}:")
i = 1
while i <= number:
    if number % i == 0:
        print(f"{i} is a factor of {number}")
    i += 1
```

**Output:**
```
Counting with while loop:
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5

Finding factors of 16:
1 is a factor of 16
2 is a factor of 16
4 is a factor of 16
8 is a factor of 16
16 is a factor of 16
```

### 3. Nested Loops:

```python
# Multiplication table
print("Multiplication Table (1-3):")
for i in range(1, 4):
    print(f"\nTable of {i}:")
    for j in range(1, 6):
        result = i * j
        print(f"{i} × {j} = {result}")

# Pattern printing
print("\nStar Pattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()  # New line after each row
```

**Output:**
```
Multiplication Table (1-3):

Table of 1:
1 × 1 = 1
1 × 2 = 2
1 × 3 = 3
1 × 4 = 4
1 × 5 = 5

Table of 2:
2 × 1 = 2
2 × 2 = 4
2 × 3 = 6
2 × 4 = 8
2 × 5 = 10

Table of 3:
3 × 1 = 3
3 × 2 = 6
3 × 3 = 9
3 × 4 = 12
3 × 5 = 15

Star Pattern:
* 
* * 
* * * 
* * * * 
* * * * * 
```

### 4. Break and Continue:

```python
# Break statement
print("Numbers 1 to 10, but stop at 6:")
for i in range(1, 11):
    if i == 6:
        break
    print(i)

# Continue statement
print("\nOdd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(i)

# Practical example: Finding first prime number after 10
print("\nFirst prime number after 10:")
num = 11
while True:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"First prime after 10 is: {num}")
        break
    num += 1
```

**Output:**
```
Numbers 1 to 10, but stop at 6:
1
2
3
4
5

Odd numbers from 1 to 10:
1
3
5
7
9

First prime number after 10:
First prime after 10 is: 11
```

---

## Practice Exercises

### Exercise 1: Grade Calculator
```python
# Calculate grade based on average marks
def calculate_grade(marks_list):
    average = sum(marks_list) / len(marks_list)
    
    if average >= 90:
        return 'A+', average
    elif average >= 80:
        return 'A', average
    elif average >= 70:
        return 'B', average
    elif average >= 60:
        return 'C', average
    else:
        return 'F', average

# Test the function
student_marks = [85, 78, 92, 88, 76]
grade, avg = calculate_grade(student_marks)
print(f"Marks: {student_marks}")
print(f"Average: {avg:.2f}")
print(f"Grade: {grade}")
```

**Output:**
```
Marks: [85, 78, 92, 88, 76]
Average: 83.80
Grade: A
```

### Exercise 2: Number Pattern
```python
# Create a number pyramid
def number_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces
        for j in range(rows - i):
            print(" ", end=" ")
        
        # Print numbers
        for k in range(1, i + 1):
            print(k, end=" ")
        
        print()  # New line

number_pyramid(5)
```

**Output:**
```
       1 
     1 2 
   1 2 3 
 1 2 3 4 
1 2 3 4 5 
```

---

## Summary

This study guide covers the fundamental concepts of Python programming:

1. **Identifiers**: Rules for naming variables and functions
2. **Variables**: Storing and managing data
3. **Comments**: Documenting your code
4. **Indentation**: Python's unique way of defining code blocks
5. **Operators**: Performing operations on data
6. **Conditions**: Making decisions in your code
7. **Loops**: Repeating code blocks efficiently

### Key Points to Remember:
- Python is case-sensitive
- Indentation is mandatory and defines code structure
- Comments make code readable and maintainable
- Use meaningful variable names
- Practice different types of loops and conditions
- Always test your code with different inputs

### Next Steps:
- Practice writing small programs using these concepts
- Try combining different concepts in single programs
- Experiment with different data types
- Learn about functions and modules

Happy Learning! 🐍