# Python Programming - Intermediate & Advanced Guide

## Table of Contents
10. [Object-Oriented Programming](#object-oriented-programming)

---

## Object-Oriented Programming

OOP is a programming paradigm that uses objects and classes to organize code.

### Classes and Objects:

```python
# Basic class definition
class Student:
    """A class representing a student."""
    
    # Class variable (shared by all instances)
    school_name = "Python Academy"
    
    def __init__(self, name, age, student_id):
        """Initialize a new student."""
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        """Add a grade to the student's record."""
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return f"Grade {grade} added for {self.name}"
        else:
            return "Invalid grade! Must be between 0 and 100."
    
    def get_average(self):
        """Calculate the average grade."""
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0
    
    def get_info(self):
        """Get student information."""
        avg = self.get_average()
        return f"Student: {self.name}, ID: {self.student_id}, Average: {avg:.2f}"
    
    def __str__(self):
        """String representation of the student."""
        return f"Student({self.name}, {self.age})"
    
    def __repr__(self):
        """Developer representation of the student."""
        return f"Student(name='{self.name}', age={self.age}, student_id='{self.student_id}')"

# Creating and using objects
print("Object-Oriented Programming:")
student1 = Student("Alice", 20, "S001")
student2 = Student("Bob", 21, "S002")

print(f"Student 1: {student1}")
print(f"Student 2: {student2}")

# Adding grades
print(f"\n{student1.add_grade(85)}")
print(f"{student1.add_grade(92)}")
print(f"{student1.add_grade(78)}")

print(f"{student2.add_grade(88)}")
print(f"{student2.add_grade(95)}")

# Getting information
print(f"\n{student1.get_info()}")
print(f"{student2.get_info()}")

# Accessing class variable
print(f"\nSchool: {Student.school_name}")
```

**Output:**
```
Object-Oriented Programming:
Student 1: Student(Alice, 20)
Student 2: Student(Bob, 21)

Grade 85 added for Alice
Grade 92 added for Alice
Grade 78 added for Alice
Grade 88 added for Bob
Grade 95 added for Bob

Student: Alice, ID: S001, Average: 85.00
Student: Bob, ID: S002, Average: 91.50

School: Python Academy
```

### Inheritance and Polymorphism:

```python
# Base class
class Animal:
    """Base class for all animals."""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        """Base method for making sound."""
        return f"{self.name} makes a sound"
    
    def info(self):
        """Get animal information."""
        return f"{self.name} is a {self.species}"

# Derived classes
class Dog(Animal):
    """Dog class inheriting from Animal."""
    
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        """Override the make_sound method."""
        return f"{self.name} barks: Woof! Woof!"
    
    def fetch(self):
        """Dog-specific method."""
        return f"{self.name} fetches the ball"

class Cat(Animal):
    """Cat class inheriting from Animal."""
    
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        """Override the make_sound method."""
        return f"{self.name} meows: Meow! Meow!"
    
    def climb(self):
        """Cat-specific method."""
        return f"{self.name} climbs the tree"

# Polymorphism example
class AnimalShelter:
    """Class to manage animals in a shelter."""
    
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        """Add an animal to the shelter."""
        self.animals.append(animal)
        return f"{animal.name} added to the shelter"
    
    def make_all_sounds(self):
        """Make all animals make their sounds."""
        print("All animals making sounds:")
        for animal in self.animals:
            print(f"  {animal.make_sound()}")

# Demonstrate inheritance and polymorphism
print("\nInheritance and Polymorphism:")
dog1 = Dog("Buddy", "Golden Retriever")
cat1 = Cat("Whiskers", "Orange")
dog2 = Dog("Max", "German Shepherd")

print(f"Dog info: {dog1.info()}")
print(f"Cat info: {cat1.info()}")

# Polymorphism in action
shelter = AnimalShelter()
shelter.add_animal(dog1)
shelter.add_animal(cat1)
shelter.add_animal(dog2)

print()
shelter.make_all_sounds()

# Specific methods
print(f"\n{dog1.fetch()}")
print(f"{cat1.climb()}")
```

**Output:**
```
Inheritance and Polymorphism:
Dog info: Buddy is a Dog
Cat info: Whiskers is a Cat

All animals making sounds:
  Buddy barks: Woof! Woof!
  Whiskers meows: Meow! Meow!
  Max barks: Woof! Woof!

Buddy fetches the ball
Whiskers climbs the tree
```

### Special Methods and Properties:

```python
class BankAccount:
    """A class representing a bank account with special methods."""
    
    def __init__(self, account_holder, initial_balance=0):
        self._account_holder = account_holder
        self._balance = initial_balance
        self._transaction_history = []
    
    @property
    def balance(self):
        """Get the current balance."""
        return self._balance
    
    @property
    def account_holder(self):
        """Get the account holder name."""
        return self._account_holder
    
    def deposit(self, amount):
        """Deposit money to the account."""
        if amount > 0:
            self._balance += amount
            self._transaction_history.append(f"Deposited: ${amount}")
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transaction_history.append(f"Withdrew: ${amount}")
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        return "Insufficient funds or invalid amount"
    
    def __str__(self):
        """String representation."""
        return f"BankAccount({self._account_holder}, ${self._balance})"
    
    def __len__(self):
        """Return number of transactions."""
        return len(self._transaction_history)
    
    def __add__(self, other):
        """Add two account balances."""
        if isinstance(other, BankAccount):
            return self._balance + other._balance
        return NotImplemented
    
    def __eq__(self, other):
        """Check if two accounts have equal balance."""
        if isinstance(other, BankAccount):
            return self._balance == other._balance
        return False

# Demonstrate special methods
print("\nSpecial Methods and Properties:")
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

print(f"Account 1: {account1}")
print(f"Account 2: {account2}")

print(f"\n{account1.deposit(200)}")
print(f"{account2.withdraw(100)}")

print(f"\nTotal transactions in Account 1: {len(account1)}")
print(f"Combined balance: ${account1 + account2}")
print(f"Accounts have equal balance: {account1 == account2}")

# Property access
print(f"\nAccount holder: {account1.account_holder}")
print(f"Current balance: ${account1.balance}")
```

**Output:**
```
Special Methods and Properties:
Account 1: BankAccount(Alice, $1000)
Account 2: BankAccount(Bob, $500)

Deposited $200. New balance: $1200
Withdrew $100. New balance: $400

Total transactions in Account 1: 1
Combined balance: $1600
Accounts have equal balance: False

Account holder: Alice
Current balance: $1200
```

---
