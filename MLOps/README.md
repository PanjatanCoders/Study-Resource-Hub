# MLOps Learning Roadmap - Phase 1: Foundations

**Duration:** 4-6 weeks  
**Goal:** Build the essential technical foundation for MLOps

---

## Week 1-2: Python Programming & Data Structures

### Learning Objectives
- Master Python fundamentals for ML and data processing
- Understand data structures and algorithms relevant to ML
- Work with NumPy and Pandas for data manipulation

### Topics to Cover
1. **Python Basics**
    - Variables, data types, control flow
    - Functions, lambda expressions, decorators
    - Object-oriented programming (classes, inheritance)
    - Error handling and exceptions

2. **Essential Libraries**
    - **NumPy**: Arrays, vectorization, broadcasting
    - **Pandas**: DataFrames, data cleaning, transformations
    - **Matplotlib/Seaborn**: Data visualization basics

3. **Data Structures & Algorithms**
    - Lists, dictionaries, sets, tuples
    - Time complexity (Big O notation)
    - Common algorithms: sorting, searching, recursion

### Hands-on Practice
```python
# Example: Data preprocessing pipeline
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    # Handle missing values
    df = df.fillna(df.mean())
    
    # Feature scaling
    scaler = StandardScaler()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    return df
```

### Resources
- **Book:** "Python for Data Analysis" by Wes McKinney
- **Course:** Real Python (realpython.com)
- **Practice:** LeetCode Easy problems, Kaggle datasets

### Checkpoint
- [ ] Build a data preprocessing script
- [ ] Create 3 different data visualizations
- [ ] Solve 10 algorithm problems

---

## Week 2-3: Machine Learning Basics

### Learning Objectives
- Understand core ML concepts and workflows
- Implement basic ML algorithms
- Evaluate model performance

### Topics to Cover
1. **ML Fundamentals**
    - Supervised vs unsupervised learning
    - Training, validation, test splits
    - Overfitting and underfitting
    - Bias-variance tradeoff

2. **Key Algorithms**
    - Linear/Logistic Regression
    - Decision Trees & Random Forests
    - K-Nearest Neighbors
    - K-Means Clustering

3. **Model Evaluation**
    - Metrics: accuracy, precision, recall, F1, RMSE, MAE
    - Cross-validation techniques
    - Confusion matrices and ROC curves

### Hands-on Practice
```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load and split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
scores = cross_val_score(model, X_train, y_train, cv=5)
print(f"CV Accuracy: {scores.mean():.3f} (+/- {scores.std():.3f})")

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
```

### Resources
- **Course:** Andrew Ng's Machine Learning (Coursera)
- **Book:** "Hands-On Machine Learning" by Aurélien Géron
- **Practice:** Kaggle competitions (Titanic, House Prices)

### Checkpoint
- [ ] Train 3 different models on a dataset
- [ ] Compare model performance with proper metrics
- [ ] Complete 1 end-to-end ML project

---

## Week 3-4: Git Version Control

### Learning Objectives
- Master Git for code versioning
- Collaborate effectively using Git workflows
- Understand branching strategies

### Topics to Cover
1. **Git Basics**
    - Initialize repos, commits, branches
    - Staging and committing changes
    - `.gitignore` and repository structure

2. **Collaboration**
    - Remote repositories (GitHub/GitLab)
    - Pull requests and code reviews
    - Merge vs rebase
    - Resolving conflicts

3. **Best Practices**
    - Commit message conventions
    - Branch naming strategies (feature/, bugfix/, release/)
    - Git hooks for automation

### Hands-on Practice
```bash
# Basic workflow
git init
git add .
git commit -m "feat: add data preprocessing module"

# Branching
git checkout -b feature/model-training
git push origin feature/model-training

# Collaboration
git pull origin main
git merge feature/model-training
git push origin main

# Viewing history
git log --oneline --graph --all
```

### Resources
- **Tutorial:** Atlassian Git Tutorials
- **Interactive:** learngitbranching.js.org
- **Book:** "Pro Git" by Scott Chacon

### Checkpoint
- [ ] Create a GitHub repository for your ML project
- [ ] Practice branching and merging with conflicts
- [ ] Submit a pull request with code review

---

## Week 4-5: Linux/Unix Fundamentals

### Learning Objectives
- Navigate and operate in Linux environments
- Use shell scripting for automation
- Understand file permissions and processes

### Topics to Cover
1. **Command Line Basics**
    - Navigation: `cd`, `ls`, `pwd`, `find`
    - File operations: `cp`, `mv`, `rm`, `chmod`
    - Text processing: `grep`, `sed`, `awk`, `cat`
    - Process management: `ps`, `top`, `kill`

2. **Shell Scripting**
    - Variables and environment
    - Loops and conditionals
    - Functions and arguments
    - Cron jobs for scheduling

3. **System Administration**
    - Package management (apt, yum)
    - SSH and remote access
    - File permissions and ownership
    - Environment variables

### Hands-on Practice
```bash
#!/bin/bash
# Example: Model training automation script

MODEL_DIR="./models"
DATA_DIR="./data"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Create directories
mkdir -p $MODEL_DIR/$TIMESTAMP

# Run training
python train.py \
  --data $DATA_DIR/train.csv \
  --output $MODEL_DIR/$TIMESTAMP/model.pkl \
  --epochs 100

# Log results
echo "Training completed at $TIMESTAMP" >> training.log
```

### Resources
- **Course:** "Linux Command Line Basics" (Udacity)
- **Book:** "The Linux Command Line" by William Shotts
- **Practice:** OverTheWire Bandit wargame

### Checkpoint
- [ ] Write 3 shell scripts for ML workflow automation
- [ ] Set up a cron job for scheduled tasks
- [ ] Practice SSH and remote server operations

---

## Week 5-6: Docker Basics

### Learning Objectives
- Containerize ML applications
- Create and manage Docker images
- Understand Docker networking and volumes

### Topics to Cover
1. **Docker Fundamentals**
    - Images vs containers
    - Dockerfile syntax and best practices
    - Docker commands: `build`, `run`, `exec`, `logs`

2. **ML Application Containerization**
    - Multi-stage builds
    - Managing dependencies (requirements.txt)
    - Environment variables and secrets
    - Volume mounting for data

3. **Docker Compose**
    - Multi-container applications
    - Service definitions
    - Networking between containers

### Hands-on Practice
```dockerfile
# Dockerfile for ML application
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["python", "serve_model.py"]
```

```bash
# Build and run
docker build -t ml-model:v1 .
docker run -p 8000:8000 -v $(pwd)/data:/app/data ml-model:v1

# Docker Compose example
docker-compose up -d
docker-compose logs -f
```

### Resources
- **Course:** Docker for Beginners (Docker official)
- **Documentation:** docs.docker.com
- **Practice:** Containerize your ML projects

### Checkpoint
- [ ] Create a Dockerfile for an ML application
- [ ] Use Docker Compose for a multi-service setup
- [ ] Push an image to Docker Hub

---

## Phase 1 Project: End-to-End ML Pipeline

### Project Requirements
Build a complete ML pipeline that demonstrates all Phase 1 skills:

1. **Data Processing** (Python/Pandas)
    - Load and clean a dataset
    - Perform exploratory data analysis
    - Create feature engineering pipeline

2. **Model Training** (scikit-learn)
    - Train multiple models
    - Perform cross-validation
    - Select best model based on metrics

3. **Version Control** (Git)
    - Organize code in a GitHub repository
    - Use branches for different features
    - Write clear commit messages

4. **Automation** (Bash)
    - Create scripts for data download
    - Automate training workflow
    - Set up logging and monitoring

5. **Containerization** (Docker)
    - Containerize the entire pipeline
    - Create reproducible environment
    - Document deployment instructions

### Suggested Datasets
- Kaggle: Heart Disease, Credit Card Fraud, Customer Churn
- UCI ML Repository: Wine Quality, Adult Income
- Your own domain-specific dataset

### Deliverables
- [ ] GitHub repository with clean code structure
- [ ] README with setup and usage instructions
- [ ] Docker image that runs the complete pipeline
- [ ] Documentation of results and findings

---

## Assessment Checklist

Before moving to Phase 2, ensure you can:

- [ ] Write efficient Python code for data processing
- [ ] Implement and evaluate ML models using scikit-learn
- [ ] Use Git for version control and collaboration
- [ ] Navigate Linux systems and write shell scripts
- [ ] Create Docker containers for ML applications
- [ ] Complete an end-to-end ML project

---

## Next Steps

Once you've completed Phase 1, you'll be ready for **Phase 2: ML Engineering**, where you'll dive deeper into:
- Advanced ML frameworks (TensorFlow, PyTorch)
- Experiment tracking and model management
- Feature stores and data versioning
- Model packaging and serialization

**Estimated completion:** 4-6 weeks  
**Next phase:** ML Engineering (6-8 weeks)

---

## Additional Resources

### Communities
- Reddit: r/MachineLearning, r/MLOps
- Discord: MLOps Community
- LinkedIn: MLOps groups

### Blogs & Newsletters
- Made With ML (madewithml.com)
- MLOps.community blog
- Neptune.ai blog

### Tools to Explore
- Jupyter Notebooks for experimentation
- VS Code with Python extensions
- PyCharm for professional development

---

**Good luck with your MLOps journey!** 🚀