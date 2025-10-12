# Python Programming - Intermediate & Advanced Guide

## Table of Contents
1. [Data Types and Structures](#data-types-and-structures)
2. [Strings](#strings)
3. [Lists](#lists)
4. [Tuples](#tuples)
5. [Dictionaries](#dictionaries)
6. [Sets](#sets)

---

## Data Types and Structures

Python has several built-in data types. Understanding them is crucial for effective programming.

### Basic Data Types:

```python
# Numeric Types
integer_num = 42
float_num = 3.14159
complex_num = 3 + 4j

# Text Type
text = "Hello, Python!"

# Boolean Type
is_python_fun = True

# None Type
empty_value = None

print("Data Types Demo:")
print(f"Integer: {integer_num} - Type: {type(integer_num)}")
print(f"Float: {float_num} - Type: {type(float_num)}")
print(f"Complex: {complex_num} - Type: {type(complex_num)}")
print(f"String: {text} - Type: {type(text)}")
print(f"Boolean: {is_python_fun} - Type: {type(is_python_fun)}")
print(f"None: {empty_value} - Type: {type(empty_value)}")

# Type conversion
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)

print(f"\nType Conversion:")
print(f"String '123' to int: {num_int}")
print(f"String '123' to float: {num_float}")
print(f"Int to string: {str(num_int)}")
```

**Output:**
```
Data Types Demo:
Integer: 42 - Type: <class 'int'>
Float: 3.14159 - Type: <class 'float'>
Complex: (3+4j) - Type: <class 'complex'>
String: Hello, Python! - Type: <class 'str'>
Boolean: True - Type: <class 'bool'>
None: None - Type: <class 'NoneType'>

Type Conversion:
String '123' to int: 123
String '123' to float: 123.0
Int to string: 123
```

---

## Strings

Strings are sequences of characters and are immutable in Python.

### String Operations:

```python
# String creation
name = "Python Programming"
description = 'A powerful language'
multiline = """This is a
multiline string
example"""

print("String Creation:")
print(f"Name: {name}")
print(f"Description: {description}")
print(f"Multiline:\n{multiline}")

# String indexing and slicing
text = "Hello, World!"
print(f"\nString Indexing:")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"Substring (0:5): {text[0:5]}")
print(f"Substring (7:): {text[7:]}")
print(f"Every 2nd character: {text[::2]}")

# String methods
sample = "  Python is Amazing  "
print(f"\nString Methods:")
print(f"Original: '{sample}'")
print(f"Upper: {sample.upper()}")
print(f"Lower: {sample.lower()}")
print(f"Strip: '{sample.strip()}'")
print(f"Replace: {sample.replace('Amazing', 'Awesome')}")
print(f"Split: {sample.strip().split()}")
print(f"Length: {len(sample.strip())}")
```

**Output:**
```
String Creation:
Name: Python Programming
Description: A powerful language
Multiline:
This is a
multiline string
example

String Indexing:
First character: H
Last character: !
Substring (0:5): Hello
Substring (7:): World!
Every 2nd character: Hlo ol!

String Methods:
Original: '  Python is Amazing  '
Upper:   PYTHON IS AMAZING  
Lower:   python is amazing  
Strip: 'Python is Amazing'
Replace:   Python is Awesome  
Split: ['Python', 'is', 'Amazing']
Length: 17
```

### String Formatting:

```python
# Different ways to format strings
name = "Alice"
age = 25
salary = 50000.75

# Old style formatting
old_format = "Name: %s, Age: %d, Salary: %.2f" % (name, age, salary)

# .format() method
new_format = "Name: {}, Age: {}, Salary: {:.2f}".format(name, age, salary)

# f-strings (recommended)
f_string = f"Name: {name}, Age: {age}, Salary: {salary:.2f}"

print("String Formatting:")
print(f"Old style: {old_format}")
print(f"New format: {new_format}")
print(f"F-string: {f_string}")

# Advanced f-string formatting
import datetime
now = datetime.datetime.now()
print(f"\nAdvanced f-string:")
print(f"Current date: {now:%Y-%m-%d}")
print(f"Current time: {now:%H:%M:%S}")
print(f"Number with commas: {salary:,}")
print(f"Percentage: {0.85:.2%}")
```

**Output:**
```
String Formatting:
Old style: Name: Alice, Age: 25, Salary: 50000.75
New format: Name: Alice, Age: 25, Salary: 50000.75
F-string: Name: Alice, Age: 25, Salary: 50000.75

Advanced f-string:
Current date: 2025-01-15
Current time: 10:30:45
Number with commas: 50,000.75
Percentage: 85.00%
```

---

## Lists

Lists are ordered, mutable collections that can store different data types.

### List Operations:

```python
# List creation
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]

print("List Creation:")
print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")
print(f"Nested: {nested}")

# List indexing and slicing
print(f"\nList Indexing:")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"First two fruits: {fruits[:2]}")
print(f"Numbers from index 2: {numbers[2:]}")

# List methods
shopping_list = ["milk", "bread", "eggs"]
print(f"\nList Methods:")
print(f"Original list: {shopping_list}")

shopping_list.append("butter")
print(f"After append: {shopping_list}")

shopping_list.insert(1, "cheese")
print(f"After insert: {shopping_list}")

removed_item = shopping_list.pop()
print(f"After pop: {shopping_list}, Removed: {removed_item}")

shopping_list.remove("bread")
print(f"After remove: {shopping_list}")

shopping_list.extend(["yogurt", "juice"])
print(f"After extend: {shopping_list}")
```

**Output:**
```
List Creation:
Numbers: [1, 2, 3, 4, 5]
Fruits: ['apple', 'banana', 'cherry']
Mixed: [1, 'hello', 3.14, True]
Nested: [[1, 2], [3, 4], [5, 6]]

List Indexing:
First fruit: apple
Last fruit: cherry
First two fruits: ['apple', 'banana']
Numbers from index 2: [3, 4, 5]

List Methods:
Original list: ['milk', 'bread', 'eggs']
After append: ['milk', 'bread', 'eggs', 'butter']
After insert: ['milk', 'cheese', 'bread', 'eggs', 'butter']
After pop: ['milk', 'cheese', 'bread', 'eggs'], Removed: butter
After remove: ['milk', 'cheese', 'eggs']
After extend: ['milk', 'cheese', 'eggs', 'yogurt', 'juice']
```

### List Comprehensions:

```python
# Basic list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in numbers]
even_numbers = [x for x in numbers if x % 2 == 0]

print("List Comprehensions:")
print(f"Original: {numbers}")
print(f"Squares: {squares}")
print(f"Even numbers: {even_numbers}")

# Advanced list comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Matrix: {matrix}")
print(f"Flattened: {flattened}")

# Conditional list comprehension
words = ["hello", "world", "python", "programming"]
long_words = [word.upper() for word in words if len(word) > 5]
print(f"Words: {words}")
print(f"Long words (>5 chars): {long_words}")
```

**Output:**
```
List Comprehensions:
Original: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Even numbers: [2, 4, 6, 8, 10]
Matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Flattened: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Words: ['hello', 'world', 'python', 'programming']
Long words (>5 chars): ['PYTHON', 'PROGRAMMING']
```

---

## Tuples

Tuples are ordered, immutable collections of items.

### Tuple Operations:

```python
# Tuple creation
coordinates = (10, 20)
colors = ("red", "green", "blue")
mixed_tuple = (1, "hello", 3.14, True)
single_item = (42,)  # Note the comma for single item tuple

print("Tuple Creation:")
print(f"Coordinates: {coordinates}")
print(f"Colors: {colors}")
print(f"Mixed: {mixed_tuple}")
print(f"Single item: {single_item}")

# Tuple unpacking
x, y = coordinates
first_color, second_color, third_color = colors

print(f"\nTuple Unpacking:")
print(f"X: {x}, Y: {y}")
print(f"First color: {first_color}")

# Tuple methods
numbers = (1, 2, 3, 2, 2, 4, 5)
print(f"\nTuple Methods:")
print(f"Numbers: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")
print(f"Length: {len(numbers)}")

# Named tuples
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])
student = Person('Alice', 20, 'New York')

print(f"\nNamed Tuple:")
print(f"Student: {student}")
print(f"Name: {student.name}")
print(f"Age: {student.age}")
print(f"City: {student.city}")
```

**Output:**
```
Tuple Creation:
Coordinates: (10, 20)
Colors: ('red', 'green', 'blue')
Mixed: (1, 'hello', 3.14, True)
Single item: (42,)

Tuple Unpacking:
X: 10, Y: 20
First color: red

Tuple Methods:
Numbers: (1, 2, 3, 2, 2, 4, 5)
Count of 2: 3
Index of 3: 2
Length: 7

Named Tuple:
Student: Person(name='Alice', age=20, city='New York')
Name: Alice
Age: 20
City: New York
```

---

## Dictionaries

Dictionaries are unordered collections of key-value pairs.

### Dictionary Operations:

```python
# Dictionary creation
student = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

# Different ways to create dictionaries
empty_dict = {}
dict_constructor = dict(name="Alice", age=25)
dict_from_tuples = dict([("name", "Bob"), ("age", 30)])

print("Dictionary Creation:")
print(f"Student: {student}")
print(f"Dict constructor: {dict_constructor}")
print(f"From tuples: {dict_from_tuples}")

# Dictionary operations
print(f"\nDictionary Operations:")
print(f"Name: {student['name']}")
print(f"Age: {student.get('age', 'Not found')}")
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# Modifying dictionaries
student["email"] = "john@example.com"
student["age"] = 21
print(f"\nAfter modifications: {student}")

# Dictionary methods
print(f"\nDictionary Methods:")
student_copy = student.copy()
print(f"Copy created")

removed_grade = student.pop("grade")
print(f"Removed grade: {removed_grade}")
print(f"After pop: {student}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dict: {squares_dict}")

# Filtering dictionary
filtered_dict = {k: v for k, v in student.items() if isinstance(v, str)}
print(f"String values only: {filtered_dict}")
```

**Output:**
```
Dictionary Creation:
Student: {'name': 'John', 'age': 20, 'grade': 'A', 'subjects': ['Math', 'Science', 'English']}
Dict constructor: {'name': 'Alice', 'age': 25}
From tuples: {'name': 'Bob', 'age': 30}

Dictionary Operations:
Name: John
Age: 20
Keys: ['name', 'age', 'grade', 'subjects']
Values: ['John', 20, 'A', ['Math', 'Science', 'English']]
Items: [('name', 'John'), ('age', 20), ('grade', 'A'), ('subjects', ['Math', 'Science', 'English'])]

After modifications: {'name': 'John', 'age': 21, 'grade': 'A', 'subjects': ['Math', 'Science', 'English'], 'email': 'john@example.com'}

Dictionary Methods:
Copy created
Removed grade: A
After pop: {'name': 'John', 'age': 21, 'subjects': ['Math', 'Science', 'English'], 'email': 'john@example.com'}
Squares dict: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
String values only: {'name': 'John', 'email': 'john@example.com'}
```

---

## Sets

Sets are unordered collections of unique items.

### Set Operations:

```python
# Set creation
fruits = {"apple", "banana", "cherry", "apple"}  # Duplicates removed
numbers = set([1, 2, 3, 4, 5, 2])  # Using set() constructor

print("Set Creation:")
print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"\nSet Operations:")
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")
print(f"Symmetric difference: {set1 ^ set2}")

# Set methods
programming_languages = {"Python", "Java", "C++"}
print(f"\nSet Methods:")
print(f"Original: {programming_languages}")

programming_languages.add("JavaScript")
print(f"After add: {programming_languages}")

programming_languages.update(["Go", "Rust"])
print(f"After update: {programming_languages}")

programming_languages.discard("C++")
print(f"After discard: {programming_languages}")

# Set comprehension
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")
```

**Output:**
```
Set Creation:
Fruits: {'cherry', 'apple', 'banana'}
Numbers: {1, 2, 3, 4, 5}

Set Operations:
Set1: {1, 2, 3, 4, 5}
Set2: {4, 5, 6, 7, 8}
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}
Difference: {1, 2, 3}
Symmetric difference: {1, 2, 3, 6, 7, 8}

Set Methods:
Original: {'C++', 'Java', 'Python'}
After add: {'C++', 'Java', 'JavaScript', 'Python'}
After update: {'C++', 'Go', 'Java', 'JavaScript', 'Python', 'Rust'}
After discard: {'Go', 'Java', 'JavaScript', 'Python', 'Rust'}
Even squares: {0, 4, 16, 36, 64}
```

---
