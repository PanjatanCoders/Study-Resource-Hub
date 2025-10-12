# Python Programming - Intermediate & Advanced Guide

## Table of Contents
9. [File I/O](#file-io)

---

## File I/O

File Input/Output operations allow you to read from and write to files.

### Basic File Operations:

```python
# Writing to a file
def write_sample_file():
    """Create a sample file with data."""
    data = [
        "Python Programming Tutorial",
        "Line 1: Introduction to Python",
        "Line 2: Variables and Data Types",
        "Line 3: Control Structures",
        "Line 4: Functions and Modules"
    ]
    
    try:
        with open("sample.txt", "w") as file:
            for line in data:
                file.write(line + "\n")
        print("File 'sample.txt' created successfully!")
    except IOError as e:
        print(f"Error writing file: {e}")

# Reading from a file
def read_file_content(filename):
    """Read and display file content."""
    try:
        with open(filename, "r") as file:
            print(f"Reading from {filename}:")
            print("=" * 40)
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File {filename} not found!")
    except IOError as e:
        print(f"Error reading file: {e}")

# Different ways to read files
def read_file_methods(filename):
    """Demonstrate different file reading methods."""
    try:
        # Method 1: Read entire file
        with open(filename, "r") as file:
            entire_content = file.read()
            print("Method 1 - Read entire file:")
            print(f"Total characters: {len(entire_content)}")
        
        # Method 2: Read line by line
        with open(filename, "r") as file:
            print("\nMethod 2 - Read line by line:")
            line_number = 1
            for line in file:
                print(f"Line {line_number}: {line.strip()}")
                line_number += 1
        
        # Method 3: Read all lines into a list
        with open(filename, "r") as file:
            lines = file.readlines()
            print(f"\nMethod 3 - All lines as list:")
            print(f"Total lines: {len(lines)}")
            
    except FileNotFoundError:
        print(f"File {filename} not found!")

# Demonstrate file operations
print("File I/O Operations:")
write_sample_file()
print()
read_file_content("sample.txt")
read_file_methods("sample.txt")
```

**Output:**
```
File I/O Operations:
File 'sample.txt' created successfully!

Reading from sample.txt:
========================================
Python Programming Tutorial
Line 1: Introduction to Python
Line 2: Variables and Data Types
Line 3: Control Structures
Line 4: Functions and Modules

Method 1 - Read entire file:
Total characters: 131

Method 2 - Read line by line:
Line 1: Python Programming Tutorial
Line 2: Line 1: Introduction to Python
Line 3: Line 2: Variables and Data Types
Line 4: Line 3: Control Structures
Line 5: Line 4: Functions and Modules

Method 3 - All lines as list:
Total lines: 5
```

### Working with CSV and JSON:

```python
import csv
import json

# Working with CSV files
def create_and_read_csv():
    """Demonstrate CSV file operations."""
    
    # Sample data
    students = [
        {"name": "Alice", "age": 20, "grade": "A"},
        {"name": "Bob", "age": 21, "grade": "B"},
        {"name": "Charlie", "age": 19, "grade": "A+"},
        {"name": "Diana", "age": 22, "grade": "B+"}
    ]
    
    # Writing CSV
    try:
        with open("students.csv", "w", newline="") as csvfile:
            fieldnames = ["name", "age", "grade"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(students)
        print("CSV file 'students.csv' created successfully!")
        
        # Reading JSON
        with open("course.json", "r") as jsonfile:
            loaded_data = json.load(jsonfile)
        
        print("\nReading from JSON:")
        print(f"Course: {loaded_data['course_name']}")
        print(f"Instructor: {loaded_data['instructor']}")
        print("Students:")
        for student in loaded_data['students']:
            print(f"  - {student['name']}: {student['progress']}% progress")
            
    except IOError as e:
        print(f"Error with JSON operations: {e}")

# Demonstrate file operations
print("CSV and JSON Operations:")
create_and_read_csv()
create_and_read_json()
```

**Output:**
```
CSV and JSON Operations:
CSV file 'students.csv' created successfully!

Reading from CSV:
Name: Alice, Age: 20, Grade: A
Name: Bob, Age: 21, Grade: B
Name: Charlie, Age: 19, Grade: A+
Name: Diana, Age: 22, Grade: B+

JSON file 'course.json' created successfully!

Reading from JSON:
Course: Python Programming
Instructor: Dr. Smith
Students:
  - Alice: 85% progress
  - Bob: 72% progress
  - Charlie: 93% progress
```

---
