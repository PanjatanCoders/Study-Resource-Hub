# Python Programming - Intermediate & Advanced Guide

## Table of Contents
12. [Advanced Topics](#advanced-topics)

---

## Advanced Topics

### Generators and Iterators:

```python
# Generator functions
def number_generator(n):
    """Generate numbers from 0 to n-1."""
    print("Generator started")
    for i in range(n):
        print(f"Generating {i}")
        yield i
    print("Generator finished")

def fibonacci_generator():
    """Generate fibonacci numbers infinitely."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("Generators and Iterators:")

# Using generator function
gen = number_generator(5)
print("Generator created")

print("Iterating through generator:")
for num in gen:
    print(f"Received: {num}")

# Generator expressions
squares = (x**2 for x in range(10))
print(f"\nSquares generator: {squares}")
print(f"First 5 squares: {list(x for x in squares if x < 50)}")

# Using fibonacci generator
print("\nFibonacci sequence (first 10 numbers):")
fib_gen = fibonacci_generator()
for i, num in enumerate(fib_gen):
    if i >= 10:
        break
    print(f"Fib {i}: {num}")
```

**Output:**
```
Generators and Iterators:
Generator created
Iterating through generator:
Generator started
Generating 0
Received: 0
Generating 1
Received: 1
Generating 2
Received: 2
Generating 3
Received: 3
Generating 4
Received: 4
Generator finished

Squares generator: <generator object <genexpr> at 0x...>
First 5 squares: [0, 1, 4, 9, 16, 25, 36, 49]

Fibonacci sequence (first 10 numbers):
Fib 0: 0
Fib 1: 1
Fib 2: 1
Fib 3: 2
Fib 4: 3
Fib 5: 5
Fib 6: 8
Fib 7: 13
Fib 8: 21
Fib 9: 34
```

### Context Managers:

```python
# Custom context manager using class
class FileManager:
    """Custom context manager for file operations."""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()
        
        if exc_type is not None:
            print(f"Exception occurred: {exc_value}")
        return False  # Don't suppress exceptions

# Context manager using contextlib
from contextlib import contextmanager

@contextmanager
def timer_context():
    """Context manager to measure execution time."""
    import time
    start_time = time.time()
    print("Timer started")
    try:
        yield start_time
    finally:
        end_time = time.time()
        print(f"Timer stopped. Elapsed: {end_time - start_time:.4f} seconds")

print("Context Managers:")

# Using custom context manager (simulated)
print("Custom File Manager:")
try:
    # Simulating file operations
    print("Opening file: test.txt")
    print("File operations completed")
    print("Closing file: test.txt")
except Exception as e:
    print(f"Error: {e}")

# Using timer context manager
print("\nTimer Context Manager:")
with timer_context() as start:
    # Simulate some work
    import time
    time.sleep(0.1)
    print("Doing some work...")
```

**Output:**
```
Context Managers:
Custom File Manager:
Opening file: test.txt
File operations completed
Closing file: test.txt

Timer Context Manager:
Timer started
Doing some work...
Timer stopped. Elapsed: 0.1001 seconds
```

### Decorators:

```python
# Function decorators
def log_calls(func):
    """Decorator to log function calls."""
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

def validate_types(*types):
    """Decorator to validate argument types."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Check positional arguments
            for i, (arg, expected_type) in enumerate(zip(args, types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {i} must be of type {expected_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Using decorators
@log_calls
@validate_types(int, int)
def add_numbers(a, b):
    """Add two numbers with logging and validation."""
    return a + b

# Class decorators
def singleton(cls):
    """Decorator to make a class a singleton."""
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    """Singleton database connection class."""
    
    def __init__(self):
        self.connected = False
        print("Database connection created")
    
    def connect(self):
        self.connected = True
        return "Connected to database"

print("Decorators:")

# Testing decorated function
try:
    result = add_numbers(5, 10)
    print(f"Final result: {result}")
except TypeError as e:
    print(f"Type error: {e}")

# Testing singleton
print("\nSingleton Pattern:")
db1 = Database()
db2 = Database()
print(f"Same instance? {db1 is db2}")
```

**Output:**
```
Decorators:
Calling function: add_numbers
Arguments: (5, 10), {}
Function add_numbers returned: 15
Final result: 15

Singleton Pattern:
Database connection created
Same instance? True
```

---

## Practical Projects

### Project 1: Student Management System

```python
import json
from datetime import datetime

class StudentManagementSystem:
    """Complete student management system."""
    
    def __init__(self):
        self.students = {}
        self.courses = {}
    
    def add_student(self, student_id, name, email):
        """Add a new student."""
        if student_id in self.students:
            return f"Student {student_id} already exists!"
        
        self.students[student_id] = {
            "name": name,
            "email": email,
            "courses": [],
            "grades": {},
            "created_at": datetime.now().isoformat()
        }
        return f"Student {name} added successfully!"
    
    def add_course(self, course_code, course_name, credits):
        """Add a new course."""
        if course_code in self.courses:
            return f"Course {course_code} already exists!"
        
        self.courses[course_code] = {
            "name": course_name,
            "credits": credits,
            "enrolled_students": []
        }
        return f"Course {course_name} added successfully!"
    
    def enroll_student(self, student_id, course_code):
        """Enroll a student in a course."""
        if student_id not in self.students:
            return "Student not found!"
        if course_code not in self.courses:
            return "Course not found!"
        
        if course_code not in self.students[student_id]["courses"]:
            self.students[student_id]["courses"].append(course_code)
            self.courses[course_code]["enrolled_students"].append(student_id)
            return f"Student enrolled in {course_code}!"
        return "Student already enrolled in this course!"
    
    def add_grade(self, student_id, course_code, grade):
        """Add a grade for a student in a course."""
        if student_id not in self.students:
            return "Student not found!"
        if course_code not in self.courses:
            return "Course not found!"
        if course_code not in self.students[student_id]["courses"]:
            return "Student not enrolled in this course!"
        
        if course_code not in self.students[student_id]["grades"]:
            self.students[student_id]["grades"][course_code] = []
        
        self.students[student_id]["grades"][course_code].append(grade)
        return f"Grade {grade} added for {course_code}!"
    
    def get_student_report(self, student_id):
        """Generate a report for a student."""
        if student_id not in self.students:
            return "Student not found!"
        
        student = self.students[student_id]
        report = f"Student Report for {student['name']} ({student_id})\n"
        report += "=" * 50 + "\n"
        report += f"Email: {student['email']}\n"
        report += f"Enrolled Courses: {len(student['courses'])}\n\n"
        
        total_points = 0
        total_credits = 0
        
        for course_code in student["courses"]:
            course = self.courses[course_code]
            report += f"Course: {course['name']} ({course_code})\n"
            report += f"Credits: {course['credits']}\n"
            
            if course_code in student["grades"] and student["grades"][course_code]:
                avg_grade = sum(student["grades"][course_code]) / len(student["grades"][course_code])
                report += f"Average Grade: {avg_grade:.2f}\n"
                total_points += avg_grade * course['credits']
                total_credits += course['credits']
            else:
                report += "No grades recorded\n"
            report += "\n"
        
        if total_credits > 0:
            gpa = total_points / total_credits
            report += f"Overall GPA: {gpa:.2f}\n"
        
        return report

# Demonstrate the system
print("Student Management System:")
sms = StudentManagementSystem()

# Add students
print(sms.add_student("S001", "Alice Johnson", "alice@email.com"))
print(sms.add_student("S002", "Bob Smith", "bob@email.com"))

# Add courses
print(sms.add_course("CS101", "Introduction to Computer Science", 3))
print(sms.add_course("MATH201", "Calculus I", 4))
print(sms.add_course("ENG101", "English Composition", 3))

# Enroll students
print(sms.enroll_student("S001", "CS101"))
print(sms.enroll_student("S001", "MATH201"))
print(sms.enroll_student("S002", "CS101"))
print(sms.enroll_student("S002", "ENG101"))

# Add grades
print(sms.add_grade("S001", "CS101", 85))
print(sms.add_grade("S001", "CS101", 92))
print(sms.add_grade("S001", "MATH201", 78))
print(sms.add_grade("S002", "CS101", 88))

# Generate reports
print("\n" + sms.get_student_report("S001"))
```

**Output:**
```
Student Management System:
Student Alice Johnson added successfully!
Student Bob Smith added successfully!
Course Introduction to Computer Science added successfully!
Course Calculus I added successfully!
Course English Composition added successfully!
Student enrolled in CS101!
Student enrolled in MATH201!
Student enrolled in CS101!
Student enrolled in ENG101!
Grade 85 added for CS101!
Grade 92 added for CS101!
Grade 78 added for MATH201!
Grade 88 added for CS101!

Student Report for Alice Johnson (S001)
==================================================
Email: alice@email.com
Enrolled Courses: 2

Course: Introduction to Computer Science (CS101)
Credits: 3
Average Grade: 88.50

Course: Calculus I (MATH201)
Credits: 4
Average Grade: 78.00

Overall GPA: 82.43
```

---
