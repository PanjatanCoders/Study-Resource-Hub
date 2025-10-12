# MLOps Learning Roadmap - Phase 1: Foundations (Detailed Guide)

**Duration:** 4-6 weeks  
**Commitment:** 15-20 hours per week  
**Goal:** Build a rock-solid technical foundation for MLOps career

---

## Table of Contents
1. [Introduction](#introduction)
2. [Week 1-2: Python Programming & Data Structures](#week-1-2-python-programming--data-structures)
3. [Week 2-3: Machine Learning Basics](#week-2-3-machine-learning-basics)
4. [Week 3-4: Git Version Control](#week-3-4-git-version-control)
5. [Week 4-5: Linux/Unix Fundamentals](#week-4-5-linuxunix-fundamentals)
6. [Week 5-6: Docker Basics](#week-5-6-docker-basics)
7. [Phase 1 Capstone Project](#phase-1-capstone-project)
8. [Assessment & Next Steps](#assessment--next-steps)

---

## Introduction

### Why Phase 1 Matters

Phase 1 establishes the technical foundation that all MLOps practices build upon. Without solid understanding of Python, ML basics, version control, Linux, and containers, you'll struggle with more advanced MLOps concepts.

### Learning Approach

- **Hands-on First**: Theory is important, but practice is essential
- **Build Projects**: Create something tangible each week
- **Document Everything**: Start good habits early
- **Join Communities**: Connect with other learners

### Prerequisites

- Basic programming knowledge (any language)
- Comfortable with command line basics
- Willingness to debug and troubleshoot
- Computer with 8GB+ RAM recommended

---

## Week 1-2: Python Programming & Data Structures

### Day 1-2: Python Fundamentals

#### Learning Objectives
- Write clean, efficient Python code
- Understand Python's data model and memory management
- Use list comprehensions and generators effectively

#### Core Concepts

**1. Variables and Data Types**
```python
# Type hints for better code clarity
def calculate_average(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)

# Multiple assignment
x, y, z = 1, 2, 3

# Unpacking
first, *middle, last = [1, 2, 3, 4, 5]
print(f"First: {first}, Middle: {middle}, Last: {last}")
```

**2. Control Flow and Iterations**
```python
# List comprehensions (efficient and Pythonic)
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Dictionary comprehensions
word_lengths = {word: len(word) for word in ['python', 'java', 'rust']}

# Generator expressions (memory efficient)
sum_of_squares = sum(x**2 for x in range(1000000))

# Enumerate for index + value
for idx, value in enumerate(['a', 'b', 'c'], start=1):
    print(f"{idx}: {value}")
```

**3. Functions and Decorators**
```python
from functools import wraps
import time

# Decorator for timing functions
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def train_model(data, epochs=100):
    # Simulate training
    time.sleep(0.1)
    return "Model trained"

# Lambda functions
multiply = lambda x, y: x * y
```

**4. Object-Oriented Programming**
```python
from abc import ABC, abstractmethod
from typing import Any

class BaseModel(ABC):
    """Abstract base class for ML models."""
    
    def __init__(self, name: str):
        self.name = name
        self.is_trained = False
    
    @abstractmethod
    def fit(self, X, y):
        """Train the model."""
        pass
    
    @abstractmethod
    def predict(self, X):
        """Make predictions."""
        pass
    
    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"

class LinearRegressionModel(BaseModel):
    def __init__(self, name: str = "LinearRegression"):
        super().__init__(name)
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        # Simplified training logic
        self.weights = [0.5] * X.shape[1]
        self.bias = 0.0
        self.is_trained = True
        return self
    
    def predict(self, X):
        if not self.is_trained:
            raise ValueError("Model must be trained before prediction")
        return X @ self.weights + self.bias
```

**5. Error Handling**
```python
class DataValidationError(Exception):
    """Custom exception for data validation errors."""
    pass

def validate_data(data):
    try:
        if data is None:
            raise DataValidationError("Data cannot be None")
        if len(data) == 0:
            raise DataValidationError("Data cannot be empty")
        return True
    except DataValidationError as e:
        print(f"Validation failed: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise
    finally:
        print("Validation attempt completed")
```

#### Daily Practice (Days 1-2)
- [ ] Write 5 functions using type hints
- [ ] Create 3 classes with inheritance
- [ ] Implement 2 decorators
- [ ] Handle errors in 3 different scenarios

---

### Day 3-5: NumPy for Numerical Computing

#### Learning Objectives
- Master NumPy array operations
- Understand vectorization and broadcasting
- Perform efficient numerical computations

#### Core Concepts

**1. Array Creation and Manipulation**
```python
import numpy as np

# Array creation
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
arr3 = np.linspace(0, 1, 5)  # 5 evenly spaced values
zeros = np.zeros((3, 4))
ones = np.ones((2, 3))
identity = np.eye(4)
random = np.random.randn(3, 3)  # Normal distribution

# Array properties
print(f"Shape: {arr1.shape}")
print(f"Dtype: {arr1.dtype}")
print(f"Size: {arr1.size}")
print(f"Ndim: {arr1.ndim}")

# Reshaping
matrix = np.arange(12).reshape(3, 4)
flattened = matrix.flatten()
transposed = matrix.T
```

**2. Vectorization and Broadcasting**
```python
# Vectorized operations (fast)
arr = np.arange(1000000)
squared = arr ** 2  # Much faster than loop

# Broadcasting example
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
row_vector = np.array([1, 0, -1])

# Broadcast addition
result = matrix + row_vector  # Adds row_vector to each row

# Column-wise operations
col_means = matrix.mean(axis=0)  # Mean of each column
row_means = matrix.mean(axis=1, keepdims=True)  # Mean of each row

# Standardization using broadcasting
standardized = (matrix - col_means) / matrix.std(axis=0)
```

**3. Indexing and Slicing**
```python
# Advanced indexing
arr = np.arange(20).reshape(4, 5)

# Basic slicing
print(arr[1:3, 2:4])  # Rows 1-2, columns 2-3

# Boolean indexing
mask = arr > 10
filtered = arr[mask]

# Fancy indexing
rows = [0, 2, 3]
cols = [1, 3, 4]
selected = arr[rows, cols]

# Where clause
result = np.where(arr > 10, arr, 0)  # Replace values ≤10 with 0
```

**4. Statistical Operations**
```python
data = np.random.randn(1000, 5)

# Basic statistics
mean = data.mean(axis=0)
std = data.std(axis=0)
median = np.median(data, axis=0)
percentile_95 = np.percentile(data, 95, axis=0)

# Correlation matrix
correlation = np.corrcoef(data.T)

# Linear algebra
A = np.random.randn(3, 3)
eigenvalues, eigenvectors = np.linalg.eig(A)
inverse = np.linalg.inv(A)
determinant = np.linalg.det(A)
```

**5. Practical ML Example: Implementing Linear Regression**
```python
def linear_regression_numpy(X, y, learning_rate=0.01, epochs=1000):
    """
    Implement linear regression using NumPy.
    
    Args:
        X: Features (m samples, n features)
        y: Target values (m samples,)
        learning_rate: Learning rate for gradient descent
        epochs: Number of training iterations
    
    Returns:
        weights: Trained weights
        bias: Trained bias
    """
    m, n = X.shape
    weights = np.zeros(n)
    bias = 0
    
    for epoch in range(epochs):
        # Forward pass
        y_pred = X @ weights + bias
        
        # Compute gradients
        dw = (1/m) * X.T @ (y_pred - y)
        db = (1/m) * np.sum(y_pred - y)
        
        # Update parameters
        weights -= learning_rate * dw
        bias -= learning_rate * db
        
        # Calculate loss every 100 epochs
        if epoch % 100 == 0:
            loss = np.mean((y_pred - y) ** 2)
            print(f"Epoch {epoch}, Loss: {loss:.4f}")
    
    return weights, bias

# Test the implementation
X_train = np.random.randn(100, 3)
true_weights = np.array([2, -1, 0.5])
y_train = X_train @ true_weights + 1 + np.random.randn(100) * 0.1

weights, bias = linear_regression_numpy(X_train, y_train)
print(f"Learned weights: {weights}")
print(f"True weights: {true_weights}")
```

#### Daily Practice (Days 3-5)
- [ ] Create 10 different array operations
- [ ] Implement matrix multiplication from scratch
- [ ] Build a simple neural network forward pass
- [ ] Compare vectorized vs loop performance

---

### Day 6-8: Pandas for Data Manipulation

#### Learning Objectives
- Master DataFrame operations
- Perform data cleaning and transformation
- Handle time series data

#### Core Concepts

**1. DataFrame Basics**
```python
import pandas as pd

# Creating DataFrames
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 28],
    'salary': [50000, 60000, 75000, 55000],
    'department': ['IT', 'HR', 'IT', 'Finance']
})

# Reading data
df_csv = pd.read_csv('data.csv')
df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1')
df_json = pd.read_json('data.json')

# Basic information
print(df.head())
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
print(df.dtypes)
```

**2. Data Selection and Filtering**
```python
# Column selection
ages = df['age']
subset = df[['name', 'age']]

# Row selection
first_row = df.iloc[0]
first_two = df.iloc[0:2]
by_index = df.loc[0:1]

# Conditional filtering
it_employees = df[df['department'] == 'IT']
high_earners = df[df['salary'] > 55000]
complex_filter = df[(df['age'] > 27) & (df['salary'] < 70000)]

# Query method (more readable)
result = df.query('age > 27 and salary < 70000')

# isin for multiple values
selected = df[df['department'].isin(['IT', 'HR'])]
```

**3. Data Cleaning**
```python
# Handling missing values
df_with_nulls = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
})

# Check for nulls
print(df_with_nulls.isnull().sum())

# Fill missing values
df_filled = df_with_nulls.fillna(0)
df_forward_fill = df_with_nulls.fillna(method='ffill')
df_mean_fill = df_with_nulls.fillna(df_with_nulls.mean())

# Drop missing values
df_dropped = df_with_nulls.dropna()
df_dropped_cols = df_with_nulls.dropna(axis=1)

# Remove duplicates
df_unique = df.drop_duplicates()
df_unique_subset = df.drop_duplicates(subset=['name'])

# Data type conversion
df['age'] = df['age'].astype('int32')
df['salary'] = df['salary'].astype('float64')

# String operations
df['name_upper'] = df['name'].str.upper()
df['name_length'] = df['name'].str.len()
```

**4. Data Transformation**
```python
# Groupby operations
dept_stats = df.groupby('department').agg({
    'salary': ['mean', 'min', 'max'],
    'age': 'mean'
})

# Custom aggregation
def age_range(ages):
    return ages.max() - ages.min()

custom_agg = df.groupby('department').agg({
    'salary': 'mean',
    'age': [age_range, 'count']
})

# Pivot tables
pivot = df.pivot_table(
    values='salary',
    index='department',
    aggfunc=['mean', 'count']
)

# Sorting
sorted_df = df.sort_values('salary', ascending=False)
multi_sort = df.sort_values(['department', 'age'])

# Adding calculated columns
df['salary_k'] = df['salary'] / 1000
df['age_group'] = pd.cut(df['age'], bins=[0, 30, 40, 100], 
                         labels=['Young', 'Middle', 'Senior'])

# Apply custom functions
df['bonus'] = df['salary'].apply(lambda x: x * 0.1 if x > 60000 else x * 0.05)

# Map and replace
dept_mapping = {'IT': 'Technology', 'HR': 'Human Resources'}
df['dept_full'] = df['department'].map(dept_mapping)
```

**5. Merging and Joining**
```python
# Sample datasets
employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'dept_id': [10, 20, 10, 30]
})

departments = pd.DataFrame({
    'dept_id': [10, 20, 30],
    'dept_name': ['IT', 'HR', 'Finance']
})

salaries = pd.DataFrame({
    'emp_id': [1, 2, 3, 4],
    'salary': [50000, 60000, 55000, 65000]
})

# Inner join
merged = employees.merge(departments, on='dept_id', how='inner')

# Left join
left_merged = employees.merge(departments, on='dept_id', how='left')

# Multiple merges
full_data = (employees
             .merge(departments, on='dept_id')
             .merge(salaries, on='emp_id'))

# Concat
combined = pd.concat([df, df_new], ignore_index=True)
```

**6. Time Series Data**
```python
# Create time series
dates = pd.date_range('2024-01-01', periods=100, freq='D')
ts_data = pd.DataFrame({
    'date': dates,
    'value': np.random.randn(100).cumsum()
})

# Set date as index
ts_data.set_index('date', inplace=True)

# Resampling
monthly = ts_data.resample('M').mean()
weekly = ts_data.resample('W').agg(['mean', 'min', 'max'])

# Rolling windows
ts_data['rolling_mean'] = ts_data['value'].rolling(window=7).mean()
ts_data['rolling_std'] = ts_data['value'].rolling(window=7).std()

# Time-based filtering
jan_data = ts_data['2024-01']
week_data = ts_data['2024-01-01':'2024-01-07']
```

**7. Practical Example: Complete Data Pipeline**
```python
def preprocess_dataset(filepath):
    """
    Complete preprocessing pipeline for ML datasets.
    """
    # Load data
    df = pd.read_csv(filepath)
    
    # Initial exploration
    print("Dataset shape:", df.shape)
    print("\nMissing values:\n", df.isnull().sum())
    print("\nData types:\n", df.dtypes)
    
    # Handle missing values
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    
    # Fill numeric with median
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    
    # Fill categorical with mode
    for col in categorical_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # Handle outliers (IQR method)
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    
    # Encode categorical variables
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    # Feature scaling
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    return df

# Usage
# processed_df = preprocess_dataset('raw_data.csv')
```

#### Daily Practice (Days 6-8)
- [ ] Load and explore 3 different datasets
- [ ] Perform 10 different data transformations
- [ ] Create a complete preprocessing pipeline
- [ ] Handle missing data in 5 different ways

---

### Day 9-10: Data Visualization

#### Learning Objectives
- Create effective visualizations with Matplotlib and Seaborn
- Understand when to use different chart types
- Build publication-quality figures

#### Core Concepts

**1. Matplotlib Basics**
```python
import matplotlib.pyplot as plt
import numpy as np

# Basic plotting
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sin(x)', linewidth=2)
plt.plot(x, y2, label='cos(x)', linewidth=2, linestyle='--')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('trig_functions.png', dpi=300, bbox_inches='tight')
plt.show()

# Subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(x, y1)
axes[0, 0].set_title('Sin')

axes[0, 1].plot(x, y2)
axes[0, 1].set_title('Cos')

axes[1, 0].scatter(x[::5], y1[::5])
axes[1, 0].set_title('Sin Scatter')

axes[1, 1].hist(y1, bins=30)
axes[1, 1].set_title('Sin Histogram')

plt.tight_layout()
plt.show()
```

**2. Seaborn for Statistical Plots**
```python
import seaborn as sns

# Set style
sns.set_style('whitegrid')
sns.set_palette('husl')

# Sample data
tips = sns.load_dataset('tips')

# Distribution plots
plt.figure(figsize=(12, 4))

plt.subplot(131)
sns.histplot(tips['total_bill'], kde=True)
plt.title('Distribution of Total Bill')

plt.subplot(132)
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Bill by Day')

plt.subplot(133)
sns.violinplot(x='day', y='total_bill', data=tips)
plt.title('Bill Distribution by Day')

plt.tight_layout()
plt.show()

# Relationship plots
plt.figure(figsize=(15, 5))

plt.subplot(131)
sns.scatterplot(x='total_bill', y='tip', hue='time', data=tips)
plt.title('Bill vs Tip')

plt.subplot(132)
sns.regplot(x='total_bill', y='tip', data=tips)
plt.title('Bill vs Tip with Regression')

plt.subplot(133)
sns.heatmap(tips.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')

plt.tight_layout()
plt.show()

# Categorical plots
g = sns.catplot(x='day', y='total_bill', hue='sex', 
                kind='bar', data=tips, height=5, aspect=1.5)
g.set_axis_labels('Day of Week', 'Total Bill ($)')
plt.show()
```

**3. ML Visualization Examples**
```python
from sklearn.datasets import make_classification
from sklearn.model_selection import learning_curve
from sklearn.ensemble import RandomForestClassifier

# Learning curves
def plot_learning_curves(estimator, X, y):
    train_sizes, train_scores, val_scores = learning_curve(
        estimator, X, y, cv=5, n_jobs=-1,
        train_sizes=np.linspace(0.1, 1.0, 10),
        scoring='accuracy'
    )
    
    train_mean = train_scores.mean(axis=1)
    train_std = train_scores.std(axis=1)
    val_mean = val_scores.mean(axis=1)
    val_std = val_scores.std(axis=1)
    
    plt.figure(figsize=(10, 6))
    plt.plot(train_sizes, train_mean, label='Training score', marker='o')
    plt.fill_between(train_sizes, train_mean - train_std,
                     train_mean + train_std, alpha=0.1)
    
    plt.plot(train_sizes, val_mean, label='Validation score', marker='s')
    plt.fill_between(train_sizes, val_mean - val_std,
                     val_mean + val_std, alpha=0.1)
    
    plt.xlabel('Training Set Size')
    plt.ylabel('Accuracy Score')
    plt.title('Learning Curves')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

# Feature importance
def plot_feature_importance(model, feature_names):
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
    
    plt.figure(figsize=(10, 6))
    plt.title('Feature Importances')
    plt.bar(range(len(importances)), importances[indices])
    plt.xticks(range(len(importances)), 
               [feature_names[i] for i in indices], rotation=45)
    plt.xlabel('Features')
    plt.ylabel('Importance')
    plt.tight_layout()
    plt.show()
```

#### Daily Practice (Days 9-10)
- [ ] Create 5 different plot types
- [ ] Visualize a dataset with 10+ plots
- [ ] Build a dashboard-style visualization
- [ ] Create publication-ready figures

---

### Week 1-2: Mini Project

**Project: Exploratory Data Analysis Dashboard**

Build a complete EDA pipeline for a dataset of your choice:

1. Load and clean data
2. Generate statistical summaries
3. Create 10+ visualizations
4. Document insights
5. Package as reusable functions

```python
# Example structure
class EDAAnalyzer:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        self.numeric_cols = None
        self.categorical_cols = None
        
    def clean_data(self):
        # Implement cleaning logic
        pass
    
    def generate_summary(self):
        # Generate statistical summary
        pass
    
    def plot_distributions(self):
        # Plot distributions
        pass
    
    def plot_correlations(self):
        # Plot correlation matrix
        pass
    
    def generate_report(self, output_path):
        # Generate complete HTML report
        pass
```

---

## Week 2-3: Machine Learning Basics

### Day 11-13: ML Fundamentals and scikit-learn

#### Learning Objectives
- Understand the ML workflow
- Master train-test splits and cross-validation
- Implement regression and classification models

#### Core Concepts

**1. The ML Workflow**
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Complete ML workflow
def ml_workflow(X, y):
    # 1. Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # 2. Create pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RandomForestClassifier(random_state=42))
    ])
    
    # 3. Train model
    pipeline.fit(X_train, y_train)
    
    # 4. Evaluate
    train_score = pipeline.score(X_train, y_train)
    test_score = pipeline.score(X_test, y_test)
    
    print(f"Train Score: {train_score:.4f}")
    print(f"Test Score: {test_score:.4f}")
    
    # 5. Predictions and detailed metrics
    y_pred = pipeline.predict(X_test)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    return pipeline

# Example usage
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=1000, n_features=20, 
                           n_informative=15, random_state=42)
model = ml_workflow(X, y)
```

**2. Regression Models**
```python
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def compare_regression_models(X_train, X_test, y_train, y_test):
    """Compare multiple regression models."""
    models = {
        'Linear Regression': LinearRegression(),
        'Ridge': Ridge(alpha=1.0),
        'Lasso': Lasso(alpha=1.0),
        'Decision Tree': DecisionTreeRegressor(max_depth=5, random_state=42),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42)
    }
    
    results = []
    
    for name, model in models.items():
        # Train
        model.fit(X_train, y_train)
        
        # Predict
        y_pred = model.predict(X_test)
        
        # Evaluate
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        results.append({
            'Model': name,
            'RMSE': rmse,
            'MAE': mae,
            'R2': r2
        })
        
        print(f"\n{name}:")
        print(f"  RMSE: {rmse:.4f}")
        print(f"  MAE: {mae:.4f}")
        print(f"  R²: {r2:.4f}")
    
    return pd.DataFrame(results)

# Example: Boston Housing
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(
    housing.data, housing.target, test_size=0.2, random_state=42
)

results_df = compare_regression_models(X_train, X_test, y_train, y_test)
```

**3. Classification Models**
```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

def compare_classification_models(X_train, X_test, y_train, y_test):
    """Compare multiple classification models."""
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
        'Decision Tree': DecisionTreeClassifier(max_depth=5, random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
        'SVM': SVC(kernel='rbf', random_state=42),
        'KNN': KNeighborsClassifier(n_neighbors=5),
        'Naive Bayes': GaussianNB()
    }
    
    results = []
    
    for name, model in models.items():
        # Train
        model.fit(X_train, y_train)
        
        # Predict
        y_pred = model.predict(X_test)
        
        # Evaluate
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
        
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        
        results.append({
            'Model': name,
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1-Score': f1
        })
        
        print(f"\n{name}:")
        print(f"  Accuracy: {accuracy:.4f}")
        print(f"  Precision: {precision:.4f}")
        print(f"  Recall: {recall:.4f}")
        print(f"  F1-Score: {f1:.4f}")
    
    return pd.DataFrame(results)
```

**4. Cross-Validation**
```python
from sklearn.model_selection import cross_val_score, cross_validate, KFold, StratifiedKFold

def perform_cross_validation(model, X, y, cv=5):
    """Perform comprehensive cross-validation."""
    
    # For classification, use StratifiedKFold
    if hasattr(y, 'unique') and len(np.unique(y)) < 20:
        cv_strategy = StratifiedKFold(n_splits=cv, shuffle=True, random_state=42)
    else:
        cv_strategy = KFold(n_splits=cv, shuffle=True, random_state=42)
    
    # Multiple metrics
    scoring = {
        'accuracy': 'accuracy',
        'precision': 'precision_weighted',
        'recall': 'recall_weighted',
        'f1': 'f1_weighted'
    }
    
    scores = cross_validate(model, X, y, cv=cv_strategy, 
                           scoring=scoring, return_train_score=True)
    
    print("Cross-Validation Results:")
    for metric in scoring.keys():
        train_scores = scores[f'train_{metric}']
        test_scores = scores[f'test_{metric}']
        print(f"\n{metric.upper()}:")
        print(f"  Train: {train_scores.mean():.4f} (+/- {train_scores.std():.4f})")
        print(f"  Test:  {test_scores.mean():.4f} (+/- {test_scores.std():.4f})")
    
    return scores
```

**5. Hyperparameter Tuning**
```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

def hyperparameter_tuning_grid(X_train, y_train):
    """Perform grid search for hyperparameter tuning."""
    
    # Define model and parameter grid
    model = RandomForestClassifier(random_state=42)
    
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [5, 10, 15, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'max_features': ['sqrt', 'log2']
    }
    
    # Grid search
    grid_search = GridSearchCV(
        model, param_grid, cv=5, 
        scoring='f1_weighted', 
        n_jobs=-1, 
        verbose=1
    )
    
    grid_search.fit(X_train, y_train)
    
    print("Best parameters:", grid_search.best_params_)
    print("Best cross-validation score:", grid_search.best_score_)
    
    return grid_search.best_estimator_

def hyperparameter_tuning_random(X_train, y_train):
    """Perform randomized search (faster for large spaces)."""
    from scipy.stats import randint, uniform
    
    model = RandomForestClassifier(random_state=42)
    
    param_distributions = {
        'n_estimators': randint(50, 200),
        'max_depth': [5, 10, 15, 20, None],
        'min_samples_split': randint(2, 20),
        'min_samples_leaf': randint(1, 10),
        'max_features': ['sqrt', 'log2', None]
    }
    
    random_search = RandomizedSearchCV(
        model, param_distributions, 
        n_iter=50, cv=5, 
        scoring='f1_weighted',
        n_jobs=-1, 
        random_state=42,
        verbose=1
    )
    
    random_search.fit(X_train, y_train)
    
    print("Best parameters:", random_search.best_params_)
    print("Best cross-validation score:", random_search.best_score_)
    
    return random_search.best_estimator_
```

**6. Model Evaluation and Interpretation**
```python
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_classification_model(model, X_test, y_test, class_names=None):
    """Comprehensive model evaluation."""
    
    # Predictions
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test) if hasattr(model, 'predict_proba') else None
    
    # 1. Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=class_names, yticklabels=class_names)
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.show()
    
    # 2. Classification Report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=class_names))
    
    # 3. ROC Curve (for binary classification)
    if len(np.unique(y_test)) == 2 and y_pred_proba is not None:
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba[:, 1])
        roc_auc = auc(fpr, tpr)
        
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, color='darkorange', lw=2, 
                label=f'ROC curve (AUC = {roc_auc:.2f})')
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver Operating Characteristic (ROC) Curve')
        plt.legend(loc="lower right")
        plt.show()
    
    # 4. Feature Importance (if available)
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
        indices = np.argsort(importances)[::-1][:20]  # Top 20
        
        plt.figure(figsize=(10, 6))
        plt.title('Top 20 Feature Importances')
        plt.bar(range(len(indices)), importances[indices])
        plt.xlabel('Feature Index')
        plt.ylabel('Importance')
        plt.show()
```

#### Daily Practice (Days 11-13)
- [ ] Implement 5 different ML algorithms from scratch
- [ ] Perform cross-validation on 3 datasets
- [ ] Tune hyperparameters for 2 models
- [ ] Create comprehensive evaluation reports

---

### Day 14: Clustering and Unsupervised Learning

#### Learning Objectives
- Understand unsupervised learning concepts
- Implement clustering algorithms
- Evaluate cluster quality

#### Core Concepts

```python
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.decomposition import PCA

def find_optimal_clusters(X, max_clusters=10):
    """Find optimal number of clusters using elbow method."""
    
    inertias = []
    silhouette_scores = []
    K = range(2, max_clusters + 1)
    
    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)
        inertias.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(X, kmeans.labels_))
    
    # Plot elbow curve
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    axes[0].plot(K, inertias, 'bo-')
    axes[0].set_xlabel('Number of Clusters')
    axes[0].set_ylabel('Inertia')
    axes[0].set_title('Elbow Method')
    axes[0].grid(True)
    
    axes[1].plot(K, silhouette_scores, 'ro-')
    axes[1].set_xlabel('Number of Clusters')
    axes[1].set_ylabel('Silhouette Score')
    axes[1].set_title('Silhouette Analysis')
    axes[1].grid(True)
    
    plt.tight_layout()
    plt.show()
    
    return K[np.argmax(silhouette_scores)]

def compare_clustering_algorithms(X, n_clusters=3):
    """Compare different clustering algorithms."""
    
    algorithms = {
        'KMeans': KMeans(n_clusters=n_clusters, random_state=42),
        'DBSCAN': DBSCAN(eps=0.5, min_samples=5),
        'Agglomerative': AgglomerativeClustering(n_clusters=n_clusters)
    }
    
    # Dimensionality reduction for visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    for idx, (name, algorithm) in enumerate(algorithms.items()):
        labels = algorithm.fit_predict(X)
        
        # Calculate metrics
        if len(np.unique(labels)) > 1:
            silhouette = silhouette_score(X, labels)
            davies_bouldin = davies_bouldin_score(X, labels)
            
            print(f"\n{name}:")
            print(f"  Silhouette Score: {silhouette:.4f}")
            print(f"  Davies-Bouldin Index: {davies_bouldin:.4f}")
            print(f"  Number of clusters: {len(np.unique(labels))}")
        
        # Visualization
        scatter = axes[idx].scatter(X_pca[:, 0], X_pca[:, 1], 
                                   c=labels, cmap='viridis', alpha=0.6)
        axes[idx].set_title(f'{name}')
        axes[idx].set_xlabel('PC1')
        axes[idx].set_ylabel('PC2')
        plt.colorbar(scatter, ax=axes[idx])
    
    plt.tight_layout()
    plt.show()
```

#### Daily Practice (Day 14)
- [ ] Implement K-Means from scratch
- [ ] Apply 3 clustering algorithms to a dataset
- [ ] Visualize clusters using PCA/t-SNE
- [ ] Evaluate cluster quality with multiple metrics

---

## Week 3-4: Git Version Control

### Day 15-17: Git Fundamentals

#### Learning Objectives
- Master Git commands and workflows
- Understand branching strategies
- Collaborate effectively on projects

#### Core Concepts

**1. Git Basics**
```bash
# Repository initialization
git init
git clone https://github.com/username/repo.git

# Basic workflow
git status
git add file.py
git add .  # Add all files
git commit -m "feat: add data preprocessing module"

# View history
git log
git log --oneline --graph --all
git log --author="Your Name"
git log --since="2 weeks ago"

# Viewing changes
git diff
git diff HEAD~1  # Compare with previous commit
git diff branch1..branch2

# Undoing changes
git restore file.py  # Discard changes
git restore --staged file.py  # Unstage
git reset HEAD~1  # Undo last commit (keep changes)
git reset --hard HEAD~1  # Undo last commit (discard changes)
```

**2. Branching and Merging**
```bash
# Branch operations
git branch  # List branches
git branch feature/new-model  # Create branch
git checkout feature/new-model  # Switch to branch
git checkout -b feature/new-model  # Create and switch

# Modern alternative
git switch feature/new-model
git switch -c feature/new-model

# Merging
git checkout main
git merge feature/new-model

# Handling merge conflicts
# 1. Edit conflicted files
# 2. Mark as resolved
git add conflicted_file.py
git commit -m "merge: resolve conflicts in feature branch"

# Rebasing (alternative to merging)
git checkout feature/new-model
git rebase main

# Interactive rebase (clean up commits)
git rebase -i HEAD~3
```

**3. Remote Operations**
```bash
# Remote management
git remote -v
git remote add origin https://github.com/username/repo.git
git remote set-url origin https://github.com/username/new-repo.git

# Fetch and pull
git fetch origin
git pull origin main
git pull --rebase origin main

# Push
git push origin main
git push -u origin feature/new-model
git push --force-with-lease  # Safer force push

# Tracking branches
git branch -vv
git branch --set-upstream-to=origin/main main
```

**4. Advanced Git**
```bash
# Stashing changes
git stash
git stash save "work in progress on feature X"
git stash list
git stash pop
git stash apply stash@{0}
git stash drop stash@{0}

# Cherry-picking
git cherry-pick <commit-hash>

# Tags
git tag v1.0.0
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
git push origin --tags

# Git hooks
# Create .git/hooks/pre-commit
#!/bin/bash
echo "Running tests before commit..."
python -m pytest tests/
if [ $? -ne 0 ]; then
    echo "Tests failed. Commit aborted."
    exit 1
fi
```

**5. .gitignore Best Practices**
```bash
# .gitignore for ML projects
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/

# Jupyter Notebook
.ipynb_checkpoints

# Data files
data/raw/*
data/processed/*
!data/raw/.gitkeep
!data/processed/.gitkeep
*.csv
*.h5
*.pkl

# Models
models/*.h5
models/*.pkl
models/*.pt
!models/.gitkeep

# Logs
logs/
*.log

# Environment
.env
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# MLflow
mlruns/

# Experiments
experiments/
outputs/
```

**6. Git Workflow for ML Projects**
```bash
# Feature branch workflow
git checkout -b feature/experiment-transformer-model
# Make changes, commit
git add src/models/transformer.py
git commit -m "feat: implement transformer model architecture"

# Regular commits during experimentation
git commit -m "exp: try learning_rate=0.001"
git commit -m "exp: add dropout layer, accuracy improved to 0.85"

# Push and create pull request
git push -u origin feature/experiment-transformer-model

# After review and approval
git checkout main
git pull origin main
git merge feature/experiment-transformer-model
git push origin main

# Clean up
git branch -d feature/experiment-transformer-model
git push origin --delete feature/experiment-transformer-model
```

**7. Commit Message Conventions**
```bash
# Format: <type>(<scope>): <subject>

# Types:
# feat: New feature
# fix: Bug fix
# docs: Documentation changes
# style: Code style changes (formatting)
# refactor: Code refactoring
# test: Adding tests
# chore: Maintenance tasks
# exp: Experiments (for ML)

# Examples:
git commit -m "feat(models): add BERT-based classifier"
git commit -m "fix(preprocessing): handle missing values in date columns"
git commit -m "exp(hyperparams): test learning_rate=0.0001, batch_size=64"
git commit -m "docs(readme): update installation instructions"
git commit -m "refactor(utils): simplify data loading function"
git commit -m "test(models): add unit tests for transformer model"
```

#### Daily Practice (Days 15-17)
- [ ] Create a repository and practice 20 Git commands
- [ ] Simulate merge conflicts and resolve them
- [ ] Create branches for 3 different features
- [ ] Set up Git hooks for your project
- [ ] Practice interactive rebase to clean history

---

### Day 18-19: GitHub Collaboration

#### Learning Objectives
- Use GitHub features effectively
- Create and review pull requests
- Manage issues and project boards

#### Core Concepts

**1. GitHub Workflow**
```bash
# Fork and clone
# 1. Fork repository on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/repo-name.git
cd repo-name

# 3. Add upstream remote
git remote add upstream https://github.com/ORIGINAL-OWNER/repo-name.git

# 4. Keep your fork updated
git fetch upstream
git checkout main
git merge upstream/main
git push origin main

# 5. Create feature branch
git checkout -b feature/add-new-model

# 6. Make changes and push
git add .
git commit -m "feat: add CNN model for image classification"
git push origin feature/add-new-model

# 7. Create Pull Request on GitHub
```

**2. Pull Request Best Practices**
```markdown
# PR Title: feat: Add CNN model for image classification

## Description
Implements a Convolutional Neural Network for image classification tasks.

## Changes
- Added CNN architecture in `src/models/cnn.py`
- Implemented data augmentation in `src/preprocessing/augmentation.py`
- Added unit tests in `tests/test_cnn.py`
- Updated documentation in `docs/models.md`

## Testing
- [x] Unit tests pass
- [x] Integration tests pass
- [x] Model achieves >85% accuracy on validation set
- [x] Code follows style guidelines

## Performance
- Training time: ~2 hours on GPU
- Validation accuracy: 87.3%
- Test accuracy: 86.8%

## Screenshots
![Model Architecture](images/cnn_architecture.png)
![Training Curves](images/training_curves.png)

## Related Issues
Closes #42

## Checklist
- [x] Code follows project style guidelines
- [x] Self-review completed
- [x] Comments added for complex logic
- [x] Documentation updated
- [x] Tests added/updated
- [x] All tests passing
```

**3. Code Review Guidelines**
```markdown
# Code Review Checklist

## Functionality
- [ ] Code does what it's supposed to do
- [ ] Edge cases handled
- [ ] No obvious bugs

## Code Quality
- [ ] Follows project coding standards
- [ ] Functions/classes are focused and single-purpose
- [ ] Appropriate error handling
- [ ] No code duplication
- [ ] Efficient algorithms used

## Testing
- [ ] Adequate test coverage
- [ ] Tests are meaningful
- [ ] All tests pass

## Documentation
- [ ] Code is self-documenting or well-commented
- [ ] README updated if needed
- [ ] API documentation complete

## ML-Specific
- [ ] Data preprocessing is reproducible
- [ ] Model architecture is documented
- [ ] Hyperparameters are configurable
- [ ] Evaluation metrics are appropriate
- [ ] Results are reproducible with random seed

## Security
- [ ] No sensitive data exposed
- [ ] No hardcoded credentials
- [ ] Dependencies are secure
```

**4. GitHub Actions for ML Projects**
```yaml
# .github/workflows/ml-pipeline.yml
name: ML Pipeline CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Cache dependencies
      uses: actions/cache@v3
      with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov flake8
    
    - name: Lint with flake8
      run: |
        flake8 src/ --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 src/ --count --max-complexity=10 --max-line-length=127 --statistics
    
    - name: Run tests
      run: |
        pytest tests/ --cov=src --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
```

#### Daily Practice (Days 18-19)
- [ ] Create 3 pull requests with proper descriptions
- [ ] Review 3 PRs from others (or your own)
- [ ] Set up GitHub Actions for automated testing
- [ ] Create issues and link them to PRs

---

### Day 20-21: Project Structure and Documentation

#### Learning Objectives
- Organize ML projects effectively
- Write comprehensive documentation
- Create reproducible environments

#### Core Concepts

**1. ML Project Structure**
```
ml-project/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│   ├── raw/              # Original, immutable data
│   ├── processed/        # Cleaned, transformed data
│   ├── external/         # Third-party data
│   └── interim/          # Intermediate transformations
│
├── models/               # Trained models
│   ├── model_v1.pkl
│   └── model_v2.h5
│
├── notebooks/            # Jupyter notebooks
│   ├── 01_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
│
├── src/                  # Source code
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── load_data.py
│   │   └── preprocess.py
│   ├── features/
│   │   ├── __init__.py
│   │   └── build_features.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── train.py
│   │   ├── predict.py
│   │   └── evaluate.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── tests/                # Unit tests
│   ├── __init__.py
│   ├── test_data.py
│   ├── test_features.py
│   └── test_models.py
│
├── docs/                 # Documentation
│   ├── api.md
│   ├── model_card.md
│   └── data_dictionary.md
│
├── configs/              # Configuration files
│   ├── config.yaml
│   └── hyperparameters.yaml
│
├── scripts/              # Standalone scripts
│   ├── download_data.sh
│   └── train_model.py
│
├── .gitignore
├── .env.example
├── requirements.txt
├── setup.py
├── README.md
├── LICENSE
└── Dockerfile
```

**2. Comprehensive README.md**
```markdown
# Project Name

Brief description of what the project does.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data](#data)
- [Models](#models)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview

Detailed description of the problem, approach, and solution.

### Key Features
- Feature 1
- Feature 2
- Feature 3

## Installation

### Prerequisites
- Python 3.9+
- CUDA 11.0+ (for GPU support)

### Setup
```bash
# Clone the repository
git clone https://github.com/username/project.git
cd project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .
```

## Usage

### Training
```bash
python scripts/train_model.py --config configs/config.yaml
```

### Prediction
```python
from src.models.predict import predict

model = load_model('models/model_v1.pkl')
predictions = predict(model, new_data)
```

### API
```bash
python src/api/app.py
curl -X POST http://localhost:8000/predict -d @sample_data.json
```

## Project Structure
```
[Include tree structure here]
```

## Data

### Dataset Description
- **Source**: Kaggle Competition
- **Size**: 50,000 samples
- **Features**: 20 numerical, 5 categorical
- **Target**: Binary classification

### Data Processing
1. Handle missing values
2. Feature engineering
3. Normalization

## Models

### Model 1: Random Forest
- Accuracy: 87%
- Precision: 85%
- Recall: 89%

### Model 2: XGBoost
- Accuracy: 89%
- Precision: 88%
- Recall: 90%

## Results

| Model | Accuracy | F1-Score | Training Time |
|-------|----------|----------|---------------|
| RF    | 0.87     | 0.86     | 2 min         |
| XGB   | 0.89     | 0.88     | 5 min         |

![Results Visualization](docs/images/results.png)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

## Contact

Your Name - email@example.com
```

**3. requirements.txt Management**
```txt
# Core dependencies
numpy==1.24.0
pandas==2.0.0
scikit-learn==1.3.0

# Deep learning
torch==2.0.0
tensorflow==2.12.0

# Data visualization
matplotlib==3.7.0
seaborn==0.12.0

# ML utilities
jupyter==1.0.0
mlflow==2.3.0
optuna==3.1.0

# API
fastapi==0.95.0
uvicorn==0.22.0

# Testing
pytest==7.3.0
pytest-cov==4.0.0

# Linting
flake8==6.0.0
black==23.3.0

# Generate with:
# pip freeze > requirements.txt

# Or use pip-tools:
# pip-compile requirements.in
```

**4. Model Card Template**
```markdown
# Model Card: [Model Name]

## Model Details
- **Model Name**: XGBoost Classifier v1.0
- **Model Version**: 1.0.0
- **Date**: 2024-01-15
- **Model Type**: Gradient Boosting Classifier
- **Framework**: XGBoost 1.7.0
- **License**: MIT

## Intended Use
- **Primary Use**: Customer churn prediction
- **Out-of-Scope Uses**: Real-time prediction (model is batch-oriented)

## Training Data
- **Dataset**: Customer transaction data
- **Size**: 100,000 samples
- **Date Range**: 2022-01-01 to 2023-12-31
- **Features**: 35 (demographic, behavioral, transaction)

## Evaluation Data
- **Test Set Size**: 20,000 samples
- **Distribution**: Stratified split, 80/20

## Metrics
| Metric    | Value |
|-----------|-------|
| Accuracy  | 0.89  |
| Precision | 0.87  |
| Recall    | 0.85  |
| F1-Score  | 0.86  |
| AUC-ROC   | 0.92  |

## Ethical Considerations
- Model may have bias toward certain customer segments
- Regular monitoring required for fairness
- Not to be used for discriminatory practices

## Limitations
- Performance degrades for customers with <6 months history
- Requires monthly retraining
- Limited to US market data

## Recommendations
- Use ensemble with other models for critical decisions
- Implement human review for borderline cases
- Monitor for data drift monthly
```

#### Daily Practice (Days 20-21)
- [ ] Restructure an existing project
- [ ] Write comprehensive README
- [ ] Create model cards for your models
- [ ] Document all functions with docstrings

---

## Week 4-5: Linux/Unix Fundamentals

### Day 22-24: Command Line Mastery

#### Learning Objectives
- Navigate Linux systems efficiently
- Use command-line tools for data processing
- Automate tasks with shell scripts

#### Core Concepts

**1. Essential Commands**
```bash
# Navigation
pwd                    # Print working directory
cd /path/to/directory  # Change directory
cd ~                   # Home directory
cd -                   # Previous directory
ls -lah                # List with details, hidden files, human-readable

# File operations
cp source dest         # Copy
cp -r dir1 dir2        # Copy directory recursively
mv old new             # Move/rename
rm file               # Remove file
rm -rf directory      # Remove directory (be careful!)
mkdir -p path/to/dir  # Create nested directories
touch file.txt        # Create empty file

# File viewing
cat file.txt          # Display entire file
less file.txt         # Paginated view
head -n 20 file.txt   # First 20 lines
tail -n 20 file.txt   # Last 20 lines
tail -f log.txt       # Follow file (live updates)

# Searching
find . -name "*.py"   # Find files by name
find . -type f -size +10M  # Files larger than 10MB
grep "error" log.txt  # Search in file
grep -r "TODO" src/   # Recursive search
grep -i "error" log.txt  # Case-insensitive

# Text processing
wc -l file.txt        # Count lines
wc -w file.txt        # Count words
sort file.txt         # Sort lines
uniq file.txt         # Remove duplicates (requires sorted input)
cut -d',' -f1,3 data.csv  # Extract columns 1 and 3

# Permissions
chmod +x script.sh    # Make executable
chmod 755 script.sh   # rwxr-xr-x
chmod 644 file.txt    # rw-r--r--
chown user:group file # Change ownership

# Process management
ps aux                # List all processes
ps aux | grep python  # Find Python processes
top                   # Interactive process viewer
htop                  # Better process viewer (install separately)
kill PID              # Terminate process
kill -9 PID           # Force kill
pkill python          # Kill by name

# Disk usage
df -h                 # Disk space
du -sh directory      # Directory size
du -h --max-depth=1   # Size of subdirectories
```

**2. Text Processing with sed and awk**
```bash
# sed (stream editor)
sed 's/old/new/g' file.txt              # Replace all occurrences
sed -i 's/old/new/g' file.txt           # In-place replacement
sed -n '10,20p' file.txt                # Print lines 10-20
sed '/pattern/d' file.txt               # Delete lines matching pattern
sed '1d' file.txt                       # Delete first line

# awk (pattern scanning and processing)
awk '{print $1}' file.txt               # Print first column
awk -F',' '{print $1,$3}' data.csv      # CSV: print columns 1 and 3
awk '$3 > 100' data.txt                 # Filter rows where column 3 > 100
awk '{sum+=$1} END {print sum}' file    # Sum first column
awk 'NR==1{print} NR>1{print | "sort"}' # Keep header, sort rest

# Processing ML log files
grep "Epoch" train.log | awk '{print $2, $4}' > results.txt
tail -f train.log | grep --line-buffered "loss" | awk '{print $NF}'

# Data preprocessing with command line
cut -d',' -f2,3,5 data.csv | tail -n +2 | sort -t',' -k2 -n
```

**3. Pipes and Redirection**
```bash
# Redirection
command > file.txt    # Redirect stdout (overwrite)
command >> file.txt   # Redirect stdout (append)
command 2> error.log  # Redirect stderr
command &> all.log    # Redirect both stdout and stderr
command < input.txt   # Redirect stdin

# Pipes
ls -l | grep ".py"
cat file.txt | sort | uniq | wc -l
ps aux | grep python | awk '{print $2}' | xargs kill

# Practical examples
# Find large Python files
find . -name "*.py" -exec du -h {} \; | sort -h | tail -10

# Count lines in all Python files
find . -name "*.py" | xargs wc -l | tail -1

# Search for TODO comments
find . -name "*.py" -exec grep -Hn "TODO" {} \;

# Monitor GPU usage
watch -n 1 nvidia-smi

# Analyze log file
cat train.log | grep "loss" | awk '{print $NF}' | \
  awk '{sum+=$1; count++} END {print "Avg loss:", sum/count}'
```

**4. Environment Variables**
```bash
# View environment variables
env
printenv
echo $PATH
echo $HOME

# Set environment variables
export MY_VAR="value"
export PATH=$PATH:/new/path

# Permanent environment variables (add to ~/.bashrc or ~/.zshrc)
echo 'export MY_VAR="value"' >> ~/.bashrc
source ~/.bashrc

# Common ML environment variables
export CUDA_VISIBLE_DEVICES=0,1
export OMP_NUM_THREADS=4
export PYTHONPATH="${PYTHONPATH}:/path/to/project"
export MODEL_PATH="/path/to/models"
```

**5. SSH and Remote Access**
```bash
# Basic SSH
ssh user@hostname
ssh -p 2222 user@hostname  # Custom port
ssh -i ~/.ssh/id_rsa user@hostname  # Specific key

# Copy files with scp
scp file.txt user@hostname:/path/
scp -r directory user@hostname:/path/
scp user@hostname:/path/file.txt ./

# Better alternative: rsync
rsync -avz source/ user@hostname:/dest/
rsync -avz --progress large_file user@hostname:/dest/

# SSH keys
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
ssh-copy-id user@hostname

# SSH config (~/.ssh/config)
Host mlserver
    HostName 192.168.1.100
    User ubuntu
    Port 22
    IdentityFile ~/.ssh/ml_server_key

# Usage: ssh mlserver

# Run command on remote server
ssh user@hostname "python train.py"

# Keep process running after disconnect
nohup python train.py &
# or use tmux/screen
```

**6. Package Management**
```bash
# Ubuntu/Debian (apt)
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
sudo apt install nvidia-cuda-toolkit
sudo apt remove package_name
sudo apt autoremove

# RedHat/CentOS (yum)
sudo yum update
sudo yum install python3
sudo yum remove package_name

# Check installed packages
dpkg -l
dpkg -l | grep python

# Check package details
apt show python3-pip
```

#### Daily Practice (Days 22-24)
- [ ] Practice 50 different Linux commands
- [ ] Process a CSV file using only command-line tools
- [ ] Set up SSH keys for remote access
- [ ] Create aliases for common commands
- [ ] Monitor system resources during model training

---

### Day 25-27: Shell Scripting

#### Learning Objectives
- Write robust shell scripts
- Automate ML workflows
- Handle errors and edge cases

#### Core Concepts

**1. Basic Shell Script Structure**
```bash
#!/bin/bash
# Script: train_pipeline.sh
# Description: Complete ML training pipeline
# Author: Your Name
# Date: 2024-01-15

# Exit on error
set -e

# Exit on undefined variable
set -u

# Exit on pipe failure
set -o pipefail

# Variables
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="${SCRIPT_DIR}/.."
DATA_DIR="${PROJECT_ROOT}/data"
MODEL_DIR="${PROJECT_ROOT}/models"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Functions
log_info() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] INFO: $1"
}

log_error() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] ERROR: $1" >&2
}

# Main script
log_info "Starting training pipeline"

# Create directories
mkdir -p "${MODEL_DIR}/${TIMESTAMP}"
mkdir -p "${DATA_DIR}/processed"

log_info "Training complete"
```

**2. Control Flow**
```bash
#!/bin/bash

# If statements
if [ -f "data.csv" ]; then
    echo "Data file exists"
elif [ -d "data" ]; then
    echo "Data directory exists"
else
    echo "No data found"
fi

# Test operators
# -f: file exists
# -d: directory exists
# -z: string is empty
# -n: string is not empty
# -eq, -ne, -lt, -le, -gt, -ge: numeric comparisons

# For loops
for file in *.py; do
    echo "Processing $file"
    python "$file"
done

for i in {1..5}; do
    echo "Iteration $i"
done

# While loop
counter=0
while [ $counter -lt 5 ]; do
    echo "Count: $counter"
    ((counter++))
done

# Case statement
case "$1" in
    train)
        echo "Training model..."
        ;;
    predict)
        echo "Making predictions..."
        ;;
    evaluate)
        echo "Evaluating model..."
        ;;
    *)
        echo "Usage: $0 {train|predict|evaluate}"
        exit 1
        ;;
esac
```

**3. Function and Arguments**
```bash
#!/bin/bash

# Function definition
train_model() {
    local model_name=$1
    local data_path=$2
    local epochs=${3:-100}  # Default value: 100
    
    echo "Training $model_name with $data_path for $epochs epochs"
    python train.py \
        --model "$model_name" \
        --data "$data_path" \
        --epochs "$epochs"
    
    return $?
}

# Using functions
train_model "random_forest" "data/train.csv" 50

# Parse command-line arguments
while getopts "m:d:e:h" opt; do
    case $opt in
        m)
            MODEL_NAME="$OPTARG"
            ;;
        d)
            DATA_PATH="$OPTARG"
            ;;
        e)
            EPOCHS="$OPTARG"
            ;;
        h)
            echo "Usage: $0 -m model_name -d data_path -e epochs"
            exit 0
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            exit 1
            ;;
    esac
done

# Alternative: positional arguments
MODEL_NAME=${1:-"random_forest"}
DATA_PATH=${2:-"data/train.csv"}
EPOCHS=${3:-100}
```

**4. Error Handling**
```bash
#!/bin/bash

# Trap errors
trap 'log_error "Script failed at line $LINENO"' ERR
trap 'cleanup' EXIT

cleanup() {
    log_info "Cleaning up temporary files..."
    rm -f /tmp/temp_data_$
}

# Check command success
if python train.py; then
    log_info "Training successful"
else
    log_error "Training failed"
    exit 1
fi

# Check file existence before processing
if [ ! -f "data.csv" ]; then
    log_error "data.csv not found"
    exit 1
fi

# Validate inputs
validate_input() {
    if [ -z "$1" ]; then
        log_error "Model name is required"
        return 1
    fi
    
    if [ ! -d "$2" ]; then
        log_error "Data directory does not exist: $2"
        return 1
    fi
    
    return 0
}
```

**5. Complete ML Pipeline Script**
```bash
#!/bin/bash
# complete_ml_pipeline.sh
# End-to-end ML training pipeline

set -euo pipefail

# Configuration
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly PROJECT_ROOT="${SCRIPT_DIR}/.."
readonly DATA_DIR="${PROJECT_ROOT}/data"
readonly MODEL_DIR="${PROJECT_ROOT}/models"
readonly LOG_DIR="${PROJECT_ROOT}/logs"
readonly TIMESTAMP=$(date +%Y%m%d_%H%M%S)
readonly LOG_FILE="${LOG_DIR}/pipeline_${TIMESTAMP}.log"

# Logging functions
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log_info() {
    log "INFO: $1"
}

log_error() {
    log "ERROR: $1" >&2
}

log_success() {
    log "SUCCESS: $1"
}

# Error handling
trap 'log_error "Pipeline failed at line $LINENO"; exit 1' ERR
trap cleanup EXIT

cleanup() {
    log_info "Cleaning up..."
    # Remove temporary files
    find /tmp -name "ml_temp_*" -user $(whoami) -delete 2>/dev/null || true
}

# Validation
validate_environment() {
    log_info "Validating environment..."
    
    # Check Python
    if ! command -v python &> /dev/null; then
        log_error "Python not found"
        return 1
    fi
    
    # Check required directories
    for dir in "$DATA_DIR" "$MODEL_DIR" "$LOG_DIR"; do
        if [ ! -d "$dir" ]; then
            log_info "Creating directory: $dir"
            mkdir -p "$dir"
        fi
    done
    
    # Check GPU availability
    if command -v nvidia-smi &> /dev/null; then
        log_info "GPU detected"
        nvidia-smi --query-gpu=name,memory.total --format=csv,noheader | \
            tee -a "$LOG_FILE"
    else
        log_info "No GPU detected, using CPU"
    fi
    
    return 0
}

# Data download
download_data() {
    log_info "Downloading data..."
    
    local data_url="$1"
    local output_file="${DATA_DIR}/raw/data.csv"
    
    if [ -f "$output_file" ]; then
        log_info "Data already exists, skipping download"
        return 0
    fi
    
    mkdir -p "${DATA_DIR}/raw"
    
    if command -v wget &> /dev/null; then
        wget -O "$output_file" "$data_url"
    elif command -v curl &> /dev/null; then
        curl -o "$output_file" "$data_url"
    else
        log_error "Neither wget nor curl found"
        return 1
    fi
    
    log_success "Data downloaded to $output_file"
}

# Data preprocessing
preprocess_data() {
    log_info "Preprocessing data..."
    
    python -c "
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv('${DATA_DIR}/raw/data.csv')
print(f'Loaded {len(df)} samples')

# Basic preprocessing
df = df.dropna()
df = df.drop_duplicates()

# Split data
train, test = train_test_split(df, test_size=0.2, random_state=42)

# Save
train.to_csv('${DATA_DIR}/processed/train.csv', index=False)
test.to_csv('${DATA_DIR}/processed/test.csv', index=False)

print(f'Train: {len(train)}, Test: {len(test)}')
"
    
    log_success "Data preprocessing complete"
}

# Model training
train_model() {
    log_info "Training model..."
    
    local model_type="${1:-random_forest}"
    local output_dir="${MODEL_DIR}/${TIMESTAMP}"
    
    mkdir -p "$output_dir"
    
    python "${PROJECT_ROOT}/src/models/train.py" \
        --data "${DATA_DIR}/processed/train.csv" \
        --model-type "$model_type" \
        --output "$output_dir" \
        --log-file "$LOG_FILE" \
        2>&1 | tee -a "$LOG_FILE"
    
    if [ $? -eq 0 ]; then
        log_success "Model trained successfully"
        echo "$output_dir" > "${MODEL_DIR}/latest.txt"
    else
        log_error "Model training failed"
        return 1
    fi
}

# Model evaluation
evaluate_model() {
    log_info "Evaluating model..."
    
    local model_path=$(cat "${MODEL_DIR}/latest.txt")
    
    python "${PROJECT_ROOT}/src/models/evaluate.py" \
        --model "$model_path/model.pkl" \
        --data "${DATA_DIR}/processed/test.csv" \
        --output "$model_path/evaluation.json" \
        2>&1 | tee -a "$LOG_FILE"
    
    # Display results
    if [ -f "$model_path/evaluation.json" ]; then
        log_info "Evaluation results:"
        cat "$model_path/evaluation.json" | python -m json.tool | tee -a "$LOG_FILE"
        log_success "Model evaluation complete"
    else
        log_error "Evaluation failed"
        return 1
    fi
}

# Send notification
send_notification() {
    local status="$1"
    local message="$2"
    
    # Example: send Slack notification
    # curl -X POST -H 'Content-type: application/json' \
    #     --data "{\"text\":\"$message\"}" \
    #     "$SLACK_WEBHOOK_URL"
    
    log_info "Notification: $status - $message"
}

# Main pipeline
main() {
    log_info "Starting ML pipeline"
    log_info "Timestamp: $TIMESTAMP"
    log_info "Log file: $LOG_FILE"
    
    # Parse arguments
    local data_url="${1:-}"
    local model_type="${2:-random_forest}"
    
    # Execute pipeline steps
    validate_environment || exit 1
    
    if [ -n "$data_url" ]; then
        download_data "$data_url" || exit 1
    fi
    
    preprocess_data || exit 1
    train_model "$model_type" || exit 1
    evaluate_model || exit 1
    
    log_success "Pipeline completed successfully!"
    send_notification "SUCCESS" "ML pipeline completed at $TIMESTAMP"
    
    # Summary
    echo ""
    echo "========================================"
    echo "Pipeline Summary"
    echo "========================================"
    echo "Status: SUCCESS"
    echo "Timestamp: $TIMESTAMP"
    echo "Model: $model_type"
    echo "Output: ${MODEL_DIR}/${TIMESTAMP}"
    echo "Log: $LOG_FILE"
    echo "========================================"
}

# Run main function
main "$@"
```

**6. Cron Jobs for Automation**
```bash
# Edit crontab
crontab -e

# Cron syntax: minute hour day month weekday command
# Examples:

# Run every day at 2 AM
0 2 * * * /path/to/train_pipeline.sh

# Run every Monday at 9 AM
0 9 * * 1 /path/to/weekly_report.sh

# Run every hour
0 * * * * /path/to/check_model.sh

# Run every 15 minutes
*/15 * * * * /path/to/monitor.sh

# Example ML cron jobs
# Daily model retraining
0 3 * * * cd /home/user/ml-project && ./scripts/train_pipeline.sh >> logs/cron.log 2>&1

# Hourly data sync
0 * * * * rsync -az remote:/data/ /local/data/

# Weekly model evaluation
0 10 * * 0 /home/user/ml-project/scripts/evaluate_all_models.sh

# Monitor logs
cat /var/log/syslog | grep CRON
```

**7. Practical Examples**
```bash
# Example 1: Batch prediction script
#!/bin/bash
for input_file in data/input/*.csv; do
    output_file="data/output/$(basename "$input_file" .csv)_predictions.csv"
    python predict.py --input "$input_file" --output "$output_file"
    echo "Processed: $input_file -> $output_file"
done

# Example 2: Model comparison
#!/bin/bash
models=("random_forest" "xgboost" "logistic_regression")
for model in "${models[@]}"; do
    echo "Training $model..."
    python train.py --model "$model" --output "models/$model"
    python evaluate.py --model "models/$model" >> results.txt
done

# Example 3: Data quality check
#!/bin/bash
check_data_quality() {
    local file=$1
    echo "Checking $file..."
    
    # Check file size
    size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null)
    if [ "$size" -lt 1000 ]; then
        echo "WARNING: File too small: $size bytes"
        return 1
    fi
    
    # Check row count
    rows=$(wc -l < "$file")
    if [ "$rows" -lt 100 ]; then
        echo "WARNING: Too few rows: $rows"
        return 1
    fi
    
    # Check for nulls
    nulls=$(grep -c "null\|NA\|NaN" "$file" || true)
    echo "Found $nulls potential null values"
    
    echo "Quality check passed"
    return 0
}
```

#### Daily Practice (Days 25-27)
- [ ] Write 5 shell scripts for different tasks
- [ ] Create a complete ML pipeline script
- [ ] Set up cron jobs for automation
- [ ] Add error handling to all scripts
- [ ] Test scripts with different edge cases

---

## Week 5-6: Docker Basics

### Day 28-30: Docker Fundamentals

#### Learning Objectives
- Understand containerization concepts
- Create and manage Docker images
- Run containerized ML applications

#### Core Concepts

**1. Docker Basics**
```bash
# Check Docker installation
docker --version
docker info

# Pull images
docker pull python:3.9
docker pull ubuntu:22.04
docker pull tensorflow/tensorflow:latest-gpu

# List images
docker images
docker images -a

# Remove images
docker rmi image_name
docker rmi $(docker images -q)  # Remove all

# Run containers
docker run hello-world
docker run -it ubuntu:22.04 /bin/bash
docker run -d -p 8080:80 nginx

# Container management
docker ps                # Running containers
docker ps -a            # All containers
docker stop container_id
docker start container_id
docker restart container_id
docker rm container_id
docker rm $(docker ps -aq)  # Remove all

# Execute commands in running container
docker exec -it container_id /bin/bash
docker exec container_id python script.py

# View logs
docker logs container_id
docker logs -f container_id  # Follow logs

# Inspect container
docker inspect container_id
docker stats container_id
```

**2. Creating Dockerfiles**
```dockerfile
# Dockerfile for ML application
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/
COPY models/ ./models/
COPY configs/ ./configs/

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV MODEL_PATH=/app/models/model.pkl

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["python", "src/api/app.py"]
```

**3. Multi-stage Builds**
```dockerfile
# Multi-stage build for smaller images
# Stage 1: Builder
FROM python:3.9 as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

COPY src/ ./src/

# Stage 2: Runtime
FROM python:3.9-slim

WORKDIR /app

# Copy only necessary files from builder
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/src ./src
COPY models/ ./models/

# Update PATH
ENV PATH=/root/.local/bin:$PATH

CMD ["python", "src/api/app.py"]
```

**4. Docker for Different ML Frameworks**
```dockerfile
# TensorFlow Dockerfile
FROM tensorflow/tensorflow:2.12.0-gpu

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "train.py"]

# ----

# PyTorch Dockerfile
FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "train.py"]

# ----

# Jupyter Notebook Dockerfile
FROM jupyter/scipy-notebook:latest

USER root

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

USER jovyan

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /home/jovyan/work

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]
```

**5. Building and Running**
```bash
# Build image
docker build -t ml-app:v1 .
docker build -t ml-app:latest --no-cache .
docker build -f Dockerfile.gpu -t ml-app:gpu .

# Run container
docker run -d --name ml-container ml-app:v1

# Run with port mapping
docker run -d -p 8000:8000 --name ml-api ml-app:v1

# Run with volume mounting
docker run -v $(pwd)/data:/app/data ml-app:v1

# Run with GPU support
docker run --gpus all ml-app:gpu

# Run with environment variables
docker run -e MODEL_PATH=/models/model.pkl ml-app:v1

# Run with resource limits
docker run --memory="4g" --cpus="2" ml-app:v1

# Interactive mode
docker run -it --rm ml-app:v1 /bin/bash
```

**6. Docker Compose**
```yaml
# docker-compose.yml
version: '3.8'

services:
  # ML API service
  ml-api:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: ml-api
    ports:
      - "8000:8000"
    volumes:
      - ./data:/app/data
      - ./models:/app/models
      - ./logs:/app/logs
    environment:
      - MODEL_PATH=/app/models/model.pkl
      - LOG_LEVEL=INFO
    depends_on:
      - database
    restart: unless-stopped
    networks:
      - ml-network

  # Database service
  database:
    image: postgres:14
    container_name: ml-database
    environment:
      - POSTGRES_USER=mluser
      - POSTGRES_PASSWORD=mlpass
      - POSTGRES_DB=mldb
    volumes:
      - db-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    networks:
      - ml-network

  # Redis for caching
  redis:
    image: redis:7-alpine
    container_name: ml-redis
    ports:
      - "6379:6379"
    networks:
      - ml-network

  # Monitoring with Prometheus
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus-data:/prometheus
    ports:
      - "9090:9090"
    networks:
      - ml-network

volumes:
  db-data:
  prometheus-data:

networks:
  ml-network:
    driver: bridge
```

**7. Docker Compose Commands**
```bash
# Start services
docker-compose up
docker-compose up -d  # Detached mode
docker-compose up --build  # Rebuild images

# Stop services
docker-compose down
docker-compose down -v  # Remove volumes

# View logs
docker-compose logs
docker-compose logs -f ml-api

# List services
docker-compose ps

# Execute commands
docker-compose exec ml-api python train.py
docker-compose exec database psql -U mluser -d mldb

# Scale services
docker-compose up -d --scale ml-api=3

# Restart service
docker-compose restart ml-api
```

**8. Best Practices**
```dockerfile
# Best practices Dockerfile
FROM python:3.9-slim

# Use specific versions
FROM python:3.9.16-slim

# Create non-root user
RUN useradd -m -u 1000 mluser
USER mluser

# Minimize layers
RUN apt-get update && apt-get install -y \
    package1 \
    package2 \
    && rm -rf /var/lib/apt/lists/*

# Use .dockerignore
# .dockerignore content:
# __pycache__
# *.pyc
# .git
# .env
# data/
# *.log

# Layer caching - copy requirements first
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Use COPY instead of ADD
COPY file.txt /app/

# Specify explicit versions
RUN pip install numpy==1.24.0 pandas==2.0.0

# Use multi-stage builds for smaller images
FROM python:3.9 AS builder
# ... build steps ...
FROM python:3.9-slim
COPY --from=builder ...
```

**9. Complete ML Project Docker Setup**
```dockerfile
# Dockerfile.train
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY src/ ./src/
COPY configs/ ./configs/

# Create directories for outputs
RUN mkdir -p /app/models /app/logs

# Training script
ENTRYPOINT ["python", "src/models/train.py"]
```

```dockerfile
# Dockerfile.serve
FROM python:3.9-slim

WORKDIR /app

# Install serving dependencies
COPY requirements-serve.txt .
RUN pip install --no-cache-dir -r requirements-serve.txt

# Copy model and serving code
COPY src/api/ ./src/api/
COPY models/ ./models/

EXPOSE 8000

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# docker-compose.ml.yml
version: '3.8'

services:
  train:
    build:
      context: .
      dockerfile: Dockerfile.train
    volumes:
      - ./data:/app/data
      - ./models:/app/models
      - ./logs:/app/logs
    command: >
      --data /app/data/train.csv
      --output /app/models
      --epochs 100

  serve:
    build:
      context: .
      dockerfile: Dockerfile.serve
    ports:
      - "8000:8000"
    volumes:
      - ./models:/app/models:ro
    environment:
      - MODEL_PATH=/app/models/model.pkl
    restart: always
```

#### Daily Practice (Days 28-30)
- [ ] Create Dockerfiles for 3 different ML projects
- [ ] Build and run containers with different configurations
- [ ] Set up a multi-container application with Docker Compose
- [ ] Practice debugging inside containers
- [ ] Optimize Docker images for size
- [ ] Implement health checks and monitoring

---

### Day 31-33: Advanced Docker Topics

#### Learning Objectives
- Optimize Docker images for production
- Implement security best practices
- Work with Docker registries

#### Core Concepts

**1. Docker Image Optimization**
```dockerfile
# Before optimization (large image)
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

# After optimization (smaller image)
FROM python:3.9-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY src/ ./src/
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "-m", "src.app"]

# Size comparison techniques
# 1. Use alpine images (smallest)
FROM python:3.9-alpine

# 2. Use slim images (better compatibility)
FROM python:3.9-slim

# 3. Clean up in same layer
RUN apt-get update && \
    apt-get install -y package && \
    rm -rf /var/lib/apt/lists/*

# 4. Use .dockerignore
# Add to .dockerignore:
# __pycache__
# *.pyc
# .git
# .pytest_cache
# .coverage
# *.log
# data/
# models/*.h5
```

**2. Docker Security**
```dockerfile
# Security best practices

# 1. Run as non-root user
FROM python:3.9-slim

RUN groupadd -r mluser && useradd -r -g mluser mluser
RUN mkdir /app && chown mluser:mluser /app

WORKDIR /app
USER mluser

COPY --chown=mluser:mluser . .

# 2. Scan for vulnerabilities
# Use: docker scan image-name

# 3. Use specific image versions
FROM python:3.9.16-slim  # Not python:3.9 or python:latest

# 4. Minimize installed packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    package1 \
    package2 && \
    rm -rf /var/lib/apt/lists/*

# 5. Don't store secrets in images
# Bad:
# COPY .env .
# Good: Use environment variables or secrets management

# 6. Use read-only root filesystem
# docker run --read-only --tmpfs /tmp image-name

# 7. Limit resources
# docker run --memory="1g" --cpus="1" image-name
```

**3. Docker Registry and Image Management**
```bash
# Docker Hub
docker login
docker tag ml-app:v1 username/ml-app:v1
docker push username/ml-app:v1
docker pull username/ml-app:v1

# Tag conventions
docker tag ml-app:v1 username/ml-app:latest
docker tag ml-app:v1 username/ml-app:1.0.0
docker tag ml-app:v1 username/ml-app:stable

# Private registry
# Run local registry
docker run -d -p 5000:5000 --name registry registry:2

# Push to local registry
docker tag ml-app:v1 localhost:5000/ml-app:v1
docker push localhost:5000/ml-app:v1

# AWS ECR
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin \
  123456789.dkr.ecr.us-east-1.amazonaws.com

docker tag ml-app:v1 123456789.dkr.ecr.us-east-1.amazonaws.com/ml-app:v1
docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/ml-app:v1

# Google Container Registry
gcloud auth configure-docker
docker tag ml-app:v1 gcr.io/project-id/ml-app:v1
docker push gcr.io/project-id/ml-app:v1

# Azure Container Registry
az acr login --name myregistry
docker tag ml-app:v1 myregistry.azurecr.io/ml-app:v1
docker push myregistry.azurecr.io/ml-app:v1
```

**4. Docker Networking**
```bash
# List networks
docker network ls

# Create network
docker network create ml-network
docker network create --driver bridge ml-bridge

# Run containers on same network
docker run -d --name api --network ml-network ml-api:v1
docker run -d --name db --network ml-network postgres:14

# Containers can communicate using service names
# In api container: curl http://db:5432

# Inspect network
docker network inspect ml-network

# Connect running container to network
docker network connect ml-network container-name

# Disconnect
docker network disconnect ml-network container-name

# Remove network
docker network rm ml-network
```

**5. Docker Volumes**
```bash
# Named volumes (managed by Docker)
docker volume create model-data
docker volume ls
docker volume inspect model-data
docker volume rm model-data

# Use named volume
docker run -v model-data:/app/models ml-app:v1

# Bind mounts (host filesystem)
docker run -v $(pwd)/models:/app/models ml-app:v1
docker run -v /host/path:/container/path:ro ml-app:v1  # read-only

# tmpfs mounts (in memory)
docker run --tmpfs /app/tmp ml-app:v1

# Volume best practices for ML
# Store data
docker run -v ml-data:/app/data ml-app:v1

# Store models
docker run -v ml-models:/app/models ml-app:v1

# Store logs
docker run -v $(pwd)/logs:/app/logs ml-app:v1

# Backup volumes
docker run --rm -v ml-data:/data -v $(pwd):/backup \
  ubuntu tar czf /backup/backup.tar.gz /data

# Restore volumes
docker run --rm -v ml-data:/data -v $(pwd):/backup \
  ubuntu tar xzf /backup/backup.tar.gz -C /data
```

**6. Production-Ready ML Docker Setup**
```dockerfile
# Dockerfile.production
FROM python:3.9-slim as base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -r mluser && \
    useradd -r -g mluser -u 1000 mluser && \
    mkdir -p /app /app/logs /app/models && \
    chown -R mluser:mluser /app

WORKDIR /app

# Install dependencies
FROM base as dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Production image
FROM base as production
COPY --from=dependencies /root/.local /root/.local
COPY --chown=mluser:mluser src/ ./src/
COPY --chown=mluser:mluser configs/ ./configs/

USER mluser

ENV PATH=/root/.local/bin:$PATH

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000

# Use exec form for proper signal handling
CMD ["python", "-m", "uvicorn", "src.api.main:app", \
     "--host", "0.0.0.0", "--port", "8000", \
     "--workers", "4", "--log-config", "configs/logging.yaml"]
```

**7. Complete Production Docker Compose**
```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  # ML API Service
  api:
    build:
      context: .
      dockerfile: Dockerfile.production
      target: production
    image: ml-app:latest
    container_name: ml-api
    restart: unless-stopped
    ports:
      - "8000:8000"
    volumes:
      - model-data:/app/models:ro
      - log-data:/app/logs
    environment:
      - MODEL_PATH=/app/models/latest.pkl
      - LOG_LEVEL=INFO
      - DATABASE_URL=postgresql://mluser:${DB_PASSWORD}@db:5432/mldb
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    networks:
      - frontend
      - backend
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G
        reservations:
          cpus: '1'
          memory: 2G
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 30s
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  # PostgreSQL Database
  db:
    image: postgres:14-alpine
    container_name: ml-database
    restart: unless-stopped
    environment:
      - POSTGRES_USER=mluser
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=mldb
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - db-data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    networks:
      - backend
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U mluser -d mldb"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis Cache
  redis:
    image: redis:7-alpine
    container_name: ml-redis
    restart: unless-stopped
    command: redis-server --appendonly yes
    volumes:
      - redis-data:/data
    networks:
      - backend
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 3

  # Nginx Reverse Proxy
  nginx:
    image: nginx:alpine
    container_name: ml-nginx
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - api
    networks:
      - frontend
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  # Prometheus Monitoring
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    restart: unless-stopped
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
    ports:
      - "9090:9090"
    networks:
      - monitoring

  # Grafana Dashboard
  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    restart: unless-stopped
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_PASSWORD}
    volumes:
      - grafana-data:/var/lib/grafana
      - ./grafana/dashboards:/etc/grafana/provisioning/dashboards:ro
    ports:
      - "3000:3000"
    depends_on:
      - prometheus
    networks:
      - monitoring

volumes:
  db-data:
    driver: local
  redis-data:
    driver: local
  model-data:
    driver: local
  log-data:
    driver: local
  prometheus-data:
    driver: local
  grafana-data:
    driver: local

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true
  monitoring:
    driver: bridge
```

**8. Deployment Scripts**
```bash
#!/bin/bash
# deploy.sh - Production deployment script

set -euo pipefail

# Configuration
readonly ENV_FILE=".env.prod"
readonly COMPOSE_FILE="docker-compose.prod.yml"
readonly IMAGE_TAG="${1:-latest}"

# Colors for output
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly NC='\033[0m' # No Color

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check prerequisites
check_prerequisites() {
    log_info "Checking prerequisites..."
    
    if ! command -v docker &> /dev/null; then
        log_error "Docker is not installed"
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null; then
        log_error "Docker Compose is not installed"
        exit 1
    fi
    
    if [ ! -f "$ENV_FILE" ]; then
        log_error "Environment file not found: $ENV_FILE"
        exit 1
    fi
    
    log_info "Prerequisites check passed"
}

# Build images
build_images() {
    log_info "Building Docker images..."
    docker-compose -f "$COMPOSE_FILE" build --no-cache
    log_info "Images built successfully"
}

# Run tests
run_tests() {
    log_info "Running tests..."
    docker-compose -f docker-compose.test.yml up --abort-on-container-exit
    local exit_code=$?
    docker-compose -f docker-compose.test.yml down
    
    if [ $exit_code -ne 0 ]; then
        log_error "Tests failed"
        exit 1
    fi
    
    log_info "Tests passed"
}

# Backup current deployment
backup_deployment() {
    log_info "Backing up current deployment..."
    
    if docker-compose -f "$COMPOSE_FILE" ps | grep -q "Up"; then
        docker-compose -f "$COMPOSE_FILE" exec -T db \
            pg_dump -U mluser mldb > "backup_$(date +%Y%m%d_%H%M%S).sql"
        log_info "Database backed up"
    fi
}

# Deploy services
deploy_services() {
    log_info "Deploying services..."
    
    # Pull latest images
    docker-compose -f "$COMPOSE_FILE" pull
    
    # Start services with zero-downtime deployment
    docker-compose -f "$COMPOSE_FILE" up -d --no-deps --build
    
    log_info "Services deployed"
}

# Health check
health_check() {
    log_info "Performing health checks..."
    
    local max_attempts=30
    local attempt=0
    
    while [ $attempt -lt $max_attempts ]; do
        if curl -sf http://localhost:8000/health > /dev/null; then
            log_info "Health check passed"
            return 0
        fi
        
        attempt=$((attempt + 1))
        log_warn "Health check attempt $attempt/$max_attempts failed, retrying..."
        sleep 2
    done
    
    log_error "Health check failed after $max_attempts attempts"
    return 1
}

# Rollback
rollback() {
    log_error "Deployment failed, rolling back..."
    
    docker-compose -f "$COMPOSE_FILE" down
    # Restore from backup if needed
    
    log_info "Rollback completed"
    exit 1
}

# Main deployment process
main() {
    log_info "Starting deployment process..."
    
    check_prerequisites
    build_images
    run_tests
    backup_deployment
    deploy_services
    
    if health_check; then
        log_info "Deployment completed successfully!"
        
        # Show running services
        docker-compose -f "$COMPOSE_FILE" ps
    else
        rollback
    fi
}

# Trap errors
trap 'rollback' ERR

# Run deployment
main "$@"
```

#### Daily Practice (Days 31-33)
- [ ] Optimize 3 Docker images for size
- [ ] Implement security best practices
- [ ] Set up a production Docker Compose stack
- [ ] Create deployment scripts with rollback capability
- [ ] Monitor container resource usage
- [ ] Push images to Docker Hub or cloud registry

---

## Phase 1 Capstone Project

### Project Overview
Build a complete end-to-end ML system that demonstrates all Phase 1 skills.

### Project Requirements

**1. Problem Statement**
Choose one of the following projects:
- Customer churn prediction system
- House price prediction API
- Image classification service
- Sentiment analysis pipeline
- Fraud detection system

**2. Technical Requirements**

**Python & Data Processing**
- [ ] Clean and preprocess raw data using Pandas
- [ ] Perform exploratory data analysis
- [ ] Create reusable preprocessing functions
- [ ] Implement data validation

**Machine Learning**
- [ ] Train at least 3 different models
- [ ] Perform cross-validation
- [ ] Tune hyperparameters
- [ ] Create evaluation reports with visualizations
- [ ] Save best model with proper versioning

**Git Version Control**
- [ ] Organize code in GitHub repository
- [ ] Use meaningful commit messages
- [ ] Create feature branches
- [ ] Write comprehensive README
- [ ] Include .gitignore for ML projects

**Linux/Unix**
- [ ] Write shell scripts for automation
- [ ] Create data download script
- [ ] Implement training pipeline script
- [ ] Set up logging

**Docker**
- [ ] Create Dockerfile for the application
- [ ] Use Docker Compose for multi-service setup
- [ ] Implement health checks
- [ ] Optimize image size
- [ ] Document deployment process

**3. Project Structure**
```
ml-capstone-project/
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
│   ├── raw/
│   ├── processed/
│   └── .gitkeep
├── models/
│   └── .gitkeep
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── load_data.py
│   │   └── preprocess.py
│   ├── features/
│   │   ├── __init__.py
│   │   └── build_features.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── train.py
│   │   ├── predict.py
│   │   └── evaluate.py
│   └── api/
│       ├── __init__.py
│       └── app.py
├── tests/
│   ├── test_data.py
│   ├── test_features.py
│   └── test_models.py
├── scripts/
│   ├── download_data.sh
│   ├── train_pipeline.sh
│   └── deploy.sh
├── configs/
│   └── config.yaml
├── docs/
│   ├── model_card.md
│   └── api_docs.md
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── LICENSE
```

**4. Deliverables**
- [ ] GitHub repository with clean code
- [ ] Jupyter notebooks with analysis
- [ ] Trained model with evaluation metrics
- [ ] Shell scripts for automation
- [ ] Docker containers for deployment
- [ ] Comprehensive documentation
- [ ] API documentation (if applicable)
- [ ] Demo video or screenshots

**5. Evaluation Criteria**
- **Code Quality (25%)**: Clean, modular, well-documented code
- **ML Implementation (25%)**: Proper workflow, evaluation, model selection
- **DevOps Practices (25%)**: Git usage, scripts, Docker setup
- **Documentation (15%)**: README, comments, model card
- **Reproducibility (10%)**: Easy to run and replicate results

### Example API Implementation
```python
# src/api/app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from typing import List

app = FastAPI(title="ML Prediction API")

# Load model at startup
model = joblib.load("models/model.pkl")

class PredictionInput(BaseModel):
    features: List[float]

class PredictionOutput(BaseModel):
    prediction: float
    probability: float = None

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    try:
        features = np.array(input_data.features).reshape(1, -1)
        prediction = model.predict(features)[0]
        
        response = {"prediction": float(prediction)}
        
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(features)[0]
            response["probability"] = float(max(proba))
        
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/model/info")
def model_info():
    return {
        "model_type": type(model).__name__,
        "features": getattr(model, "n_features_in_", None)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

## Assessment & Next Steps

### Phase 1 Self-Assessment Checklist

**Python & Data Processing**
- [ ] Can write efficient Python code with type hints
- [ ] Comfortable with NumPy array operations
- [ ] Can manipulate data with Pandas
- [ ] Can create meaningful visualizations
- [ ] Understand data preprocessing pipelines

**Machine Learning**
- [ ] Understand ML workflow and best practices
- [ ] Can implement and evaluate multiple models
- [ ] Know when to use different algorithms
- [ ] Can perform cross-validation and hyperparameter tuning
- [ ] Understand model evaluation metrics

**Git Version Control**
- [ ] Can use Git for version control
- [ ] Understand branching strategies
- [ ] Can create and review pull requests
- [ ] Follow commit message conventions
- [ ] Can resolve merge conflicts

**Linux/Unix**
- [ ] Comfortable with command-line operations
- [ ] Can write shell scripts for automation
- [ ] Understand file permissions and processes
- [ ] Can use SSH for remote access
- [ ] Know text processing tools (grep, sed, awk)

**Docker**
- [ ] Can create Dockerfiles
- [ ] Understand image layers and optimization
- [ ] Can use Docker Compose
- [ ] Know container networking and volumes
- [ ] Can deploy containerized applications

### Moving to Phase 2: ML Engineering

Once you've completed Phase 1, you're ready for Phase 2, which covers:

**Phase 2 Topics (6-8 weeks)**
1. **Deep Learning Frameworks**
    - TensorFlow and Keras
    - PyTorch fundamentals
    - Model architecture design
    - Transfer learning

2. **Experiment Tracking**
    - MLflow for experiment management
    - Weights & Biases
    - Model versioning
    - Hyperparameter optimization with Optuna

3. **Feature Engineering**
    - Advanced feature selection
    - Feature stores (Feast)
    - Feature engineering pipelines
    - Automated feature engineering

4. **Model Packaging**
    - Model serialization (pickle, joblib, ONNX)
    - Model optimization
    - Model documentation
    - Model registry

### Additional Resources

**Books**
- "Hands-On Machine Learning" by Aurélien Géron
- "Python for Data Analysis" by Wes McKinney
- "The Docker Book" by James Turnbull
- "Pro Git" by Scott Chacon

**Online Courses**
- Fast.ai Practical Deep Learning
- Coursera: Machine Learning by Andrew Ng
- Docker Mastery (Udemy)
- Linux Command Line Bootcamp (Udemy)

**Websites & Blogs**
- Machine Learning Mastery
- Towards Data Science
- Real Python
- Docker Documentation

**Communities**
- Reddit: r/MachineLearning, r/learnmachinelearning
- Stack Overflow
- GitHub Discussions
- MLOps Community Discord

### Final Tips

1. **Practice Consistently**: Dedicate 2-3 hours daily
2. **Build Projects**: Theory is important, but practice is essential
3. **Document Everything**: Good documentation saves time later
4. **Join Communities**: Learn from others and share your knowledge
5. **Stay Updated**: ML and DevOps evolve rapidly
6. **Focus on Fundamentals**: Don't skip the basics
7. **Debug Actively**: Embrace errors as learning opportunities
8. **Version Everything**: Code, data, models, experiments

---

## Congratulations! 🎉

You've completed the Phase 1 foundation guide for MLOps. You now have the essential skills to:
- Write production-quality Python code
- Build and evaluate ML models
- Use version control effectively
- Automate workflows with shell scripts
- Deploy applications with Docker

**Next step**: Complete your capstone project and move on to Phase 2: ML Engineering!

**Remember**: MLOps is a journey, not a destination. Keep learning, building, and improving!

---

**Document Version**: 1.0  
**Last Updated**: 2024-01-15  
**Estimated Completion Time**: 4-6 weeks (15-20 hours/week)

Good luck with your MLOps journey! 🚀