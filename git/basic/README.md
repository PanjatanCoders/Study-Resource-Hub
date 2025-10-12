# Git Tutorial - Basic Level

A comprehensive guide for Git beginners.

---

## Table of Contents
- [Installation & Configuration](#installation--configuration)
- [Creating a Repository](#creating-a-repository)
- [Basic Workflow](#basic-workflow)
- [Working with Remote Repositories](#working-with-remote-repositories)
- [Basic Branching](#basic-branching)
- [Basic .gitignore](#basic-gitignore)
- [Practice Exercises](#practice-exercises)

---

## Installation & Configuration

### What is Git?

Git is a distributed version control system that tracks changes in your code. Unlike centralized systems, every developer has a complete copy of the repository history, enabling offline work and faster operations.

**Key Concepts:**
- **Version Control**: Track changes over time
- **Distributed**: Every developer has full history
- **Branching**: Work on features independently
- **Collaboration**: Multiple developers can work together

### Why Configuration Matters

Git needs to know who you are to attribute commits correctly. The `--global` flag sets configuration for all repositories on your system. You can override this per-repository by omitting `--global`.

```bash
# Install Git (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install git

# Install Git (macOS with Homebrew)
brew install git

# Install Git (Windows)
# Download from https://git-scm.com/download/win

# Verify installation
git --version

# Configure user information (required)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# View all configuration
git config --list

# View specific configuration
git config user.name
git config user.email

# Configure default editor (optional)
git config --global core.editor "vim"
git config --global core.editor "code --wait"  # VS Code

# Set up line ending handling
git config --global core.autocrlf true    # Windows
git config --global core.autocrlf input   # Mac/Linux

# Enable colored output
git config --global color.ui auto

# Set default branch name to 'main'
git config --global init.defaultBranch main
```

---

## Creating a Repository

### Understanding Repositories

A Git repository is a directory that Git tracks. It contains a hidden `.git` folder with all version history and configuration. You can either create a new repository or clone an existing one.

**When to Use Each:**
- `git init`: Starting a new project from scratch
- `git clone`: Contributing to an existing project or backing up a repository

### Initialize a New Repository

```bash
# Navigate to your project directory
cd ~/projects/my-project

# Initialize a new repository
git init

# Initialize with specific branch name
git init -b main

# Check status
git status
```

### Clone an Existing Repository

```bash
# Clone via HTTPS
git clone https://github.com/user/repo.git

# Clone via SSH (requires SSH key setup)
git clone git@github.com:user/repo.git

# Clone to a specific folder
git clone https://github.com/user/repo.git my-custom-folder

# Clone only recent history (faster for large repos)
git clone --depth 1 https://github.com/user/repo.git

# Clone specific branch
git clone -b develop https://github.com/user/repo.git
```

---

## Basic Workflow

### The Three States

Git has three main states for your files:

1. **Working Directory**: Where you modify files
2. **Staging Area (Index)**: Where you prepare files for commit
3. **Repository**: Where Git permanently stores snapshots

**Workflow**: Working Directory → `git add` → Staging Area → `git commit` → Repository

### Understanding the Workflow

- `git status`: Shows which files are modified, staged, or untracked
- `git add`: Moves changes from working directory to staging area
- `git commit`: Saves staged changes to repository with a message
- The staging area lets you craft precise commits by selecting exactly what to include

### Check Status

```bash
# Check repository status
git status

# Short status format (more compact)
git status -s
# M  = Modified and staged
# MM = Modified, staged, and modified again
# A  = Added
# ?? = Untracked
```

### Add Files to Staging Area

```bash
# Add specific file
git add file.txt

# Add multiple files
git add file1.txt file2.txt file3.txt

# Add all files in current directory
git add .

# Add all files in repository
git add -A

# Add files by pattern
git add *.js
git add src/*.java

# Add entire directory
git add src/

# Add files interactively (choose what to stage)
git add -p file.txt
```

### Commit Changes

```bash
# Commit with message
git commit -m "Add login feature"

# Commit with detailed message (opens editor)
git commit

# Add and commit in one step (tracked files only)
git commit -am "Fix bug in authentication"

# Commit with both short and long message
git commit -m "Add user profile" -m "Detailed description here"
```

### Commit Message Best Practices

**Good commit messages:**
- Use imperative mood: "Add feature" not "Added feature"
- Keep first line under 50 characters
- Capitalize first letter
- No period at the end of subject
- Blank line between subject and body
- Wrap body at 72 characters
- Explain what and why, not how

**Example:**
```
Add user authentication feature

Implement JWT-based authentication system with login and logout
functionality. This enables secure user sessions and protects
sensitive endpoints.

Fixes #123
```

### View Commit History

```bash
# View commit history
git log

# Compact view (one line per commit)
git log --oneline

# Show last N commits
git log -5

# Visual branch graph
git log --graph --oneline --all

# Show commits with file changes
git log --stat

# Show commits with full diff
git log -p

# Search commits by message
git log --grep="bug fix"

# Show commits by author
git log --author="John Doe"

# Show commits in date range
git log --since="2 weeks ago"
git log --after="2024-01-01" --before="2024-12-31"
```

### View Changes

```bash
# Show unstaged changes
git diff

# Show specific file changes
git diff file.txt

# Show staged changes (what will be committed)
git diff --staged
git diff --cached  # Same as --staged
```

---

## Working with Remote Repositories

### What are Remotes?

Remotes are versions of your repository hosted on the internet or network. They enable collaboration by allowing multiple developers to push and pull changes. The default remote is typically named `origin`.

### Understanding Push vs Pull vs Fetch

- `git fetch`: Downloads changes but doesn't merge them (safe to run anytime)
- `git pull`: Downloads and automatically merges changes (fetch + merge)
- `git push`: Uploads your local commits to the remote repository

### Authentication

Modern Git uses:
- **Personal Access Tokens (PAT)** for HTTPS
- **SSH Keys** for SSH URLs

Setup SSH key:
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Add SSH key to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key (add to GitHub/GitLab/Bitbucket)
cat ~/.ssh/id_ed25519.pub
```

### Working with Remotes

```bash
# Add remote repository
git remote add origin https://github.com/user/repo.git

# View remote repositories
git remote -v

# Show detailed remote info
git remote show origin

# Change remote URL
git remote set-url origin https://github.com/user/new-repo.git

# Rename a remote
git remote rename origin upstream

# Remove a remote
git remote remove origin

# Add additional remote (e.g., for forked repo)
git remote add upstream https://github.com/original/repo.git
```

### Push Changes

```bash
# Push to remote (first time, set upstream)
git push -u origin main

# Push to remote (subsequent times)
git push

# Push specific branch
git push origin feature-branch

# Push all branches
git push --all

# Push tags
git push --tags

# Force push (use with caution!)
git push --force
git push --force-with-lease  # Safer alternative
```

### Pull Changes

```bash
# Pull from remote (fetch + merge)
git pull

# Pull from specific remote and branch
git pull origin main

# Pull with rebase instead of merge
git pull --rebase

# Pull all branches
git pull --all
```

### Fetch Changes

```bash
# Fetch changes without merging
git fetch origin

# Fetch all remotes
git fetch --all

# Fetch and prune deleted branches
git fetch --prune

# View remote branches
git branch -r

# View all branches (local and remote)
git branch -a
```

### Common Workflow

```bash
# 1. Clone repository
git clone https://github.com/user/repo.git
cd repo

# 2. Make changes
echo "Hello" > file.txt
git add file.txt
git commit -m "Add greeting"

# 3. Push changes
git push origin main

# 4. Pull latest changes (before starting new work)
git pull origin main
```

---

## Basic Branching

### Why Branches Matter

Branches allow you to work on features, fixes, or experiments without affecting the main codebase. Each branch is an independent line of development. Branches are lightweight in Git—they're just pointers to commits.

### Branch Naming Conventions

- `main` or `master`: Primary branch
- `feature/feature-name`: New features
- `bugfix/bug-description`: Bug fixes
- `hotfix/critical-fix`: Urgent production fixes
- `release/version-number`: Release preparation
- `experiment/idea-name`: Experimental changes

### Create and Switch Branches

```bash
# Create a new branch
git branch feature-login

# Switch to a branch (old syntax)
git checkout feature-login

# Switch to a branch (new syntax, Git 2.23+)
git switch feature-login

# Create and switch in one command (old syntax)
git checkout -b feature-login

# Create and switch (new syntax)
git switch -c feature-login

# Create branch from specific commit
git branch feature-login abc1234
```

### List Branches

```bash
# List all local branches (* indicates current)
git branch

# List with last commit info
git branch -v

# List remote branches
git branch -r

# List all branches (local and remote)
git branch -a

# List merged branches
git branch --merged

# List unmerged branches
git branch --no-merged
```

### Rename Branches

```bash
# Rename current branch
git branch -m new-branch-name

# Rename a different branch
git branch -m old-name new-name

# Rename and push to remote
git branch -m old-name new-name
git push origin -u new-name
git push origin --delete old-name
```

### Delete Branches

```bash
# Delete a branch (safe - prevents deletion if unmerged)
git branch -d feature-login

# Force delete a branch
git branch -D feature-login

# Delete remote branch
git push origin --delete feature-login
```

### Merge Branches

```bash
# Switch to target branch
git checkout main

# Merge feature branch into main
git merge feature-login

# Merge with commit message
git merge feature-login -m "Merge login feature"
```

### Typical Workflow

```bash
# 1. Create and switch to feature branch
git checkout -b feature/user-profile

# 2. Make changes and commit
echo "profile code" > profile.js
git add profile.js
git commit -m "Add user profile page"

# 3. Push branch to remote
git push -u origin feature/user-profile

# 4. Create pull request on GitHub/GitLab
# (Done via web interface)

# 5. After merge, switch back and update
git checkout main
git pull origin main

# 6. Delete local branch
git branch -d feature/user-profile
```

---

## Basic .gitignore

### What is .gitignore?

`.gitignore` tells Git which files or directories to ignore. This prevents committing sensitive data, build artifacts, or system files.

### Creating .gitignore

```bash
# Create .gitignore file in repository root
touch .gitignore

# Edit with your preferred editor
nano .gitignore
```

### Common Patterns

```gitignore
# Ignore specific file
config.env
secret.key

# Ignore all files with extension
*.log
*.tmp
*.class

# Ignore directory
node_modules/
build/
dist/
.cache/

# Ignore files in any directory
**/logs
**/temp

# Ignore files in specific location
src/temp/

# Exception - don't ignore this file
!important.log

# Ignore all .txt files except this one
*.txt
!readme.txt
```

### Language-Specific Examples

**Node.js:**
```gitignore
node_modules/
npm-debug.log
.env
dist/
build/
```

**Python:**
```gitignore
__pycache__/
*.pyc
*.pyo
.venv/
venv/
*.egg-info/
.pytest_cache/
```

**Java:**
```gitignore
*.class
*.jar
*.war
target/
build/
.gradle/
```

**General:**
```gitignore
# OS files
.DS_Store
Thumbs.db

# IDE files
.vscode/
.idea/
*.swp
*.swo
```

### Apply .gitignore to Already Tracked Files

```bash
# Remove file from Git but keep locally
git rm --cached file.txt

# Remove directory from Git but keep locally
git rm -r --cached node_modules/

# Commit the removal
git commit -m "Remove ignored files from repository"
```

### Global .gitignore

```bash
# Create global gitignore
touch ~/.gitignore_global

# Add common ignores (OS, IDE files)
echo ".DS_Store" >> ~/.gitignore_global
echo "Thumbs.db" >> ~/.gitignore_global
echo ".vscode/" >> ~/.gitignore_global

# Configure Git to use it
git config --global core.excludesfile ~/.gitignore_global
```

---

## Practice Exercises

### Exercise 1: First Repository

```bash
# 1. Create a new directory and initialize Git
mkdir my-first-repo
cd my-first-repo
git init

# 2. Create a README file
echo "# My First Repository" > README.md

# 3. Stage and commit
git add README.md
git commit -m "Initial commit"

# 4. View history
git log
```

### Exercise 2: Basic Workflow

```bash
# 1. Create multiple files
echo "print('Hello')" > hello.py
echo "print('World')" > world.py

# 2. Stage and commit separately
git add hello.py
git commit -m "Add hello script"

git add world.py
git commit -m "Add world script"

# 3. View history
git log --oneline

# 4. Make changes
echo "print('Hello Git')" > hello.py

# 5. View diff
git diff

# 6. Commit changes
git add hello.py
git commit -m "Update greeting"
```

### Exercise 3: Branching

```bash
# 1. Create and switch to new branch
git checkout -b feature/greeting

# 2. Make changes
echo "def greet():\n    print('Hello from branch')" > greet.py

# 3. Commit on branch
git add greet.py
git commit -m "Add greeting function"

# 4. Switch to main
git checkout main

# 5. Merge branch
git merge feature/greeting

# 6. Delete branch
git branch -d feature/greeting
```

### Exercise 4: Remote Repository

```bash
# 1. Create repository on GitHub

# 2. Add remote
git remote add origin https://github.com/yourusername/my-first-repo.git

# 3. Push to remote
git push -u origin main

# 4. Make changes locally
echo "Updated" >> README.md
git commit -am "Update README"

# 5. Push changes
git push

# 6. Pull changes (simulate other developer's work)
# Make changes on GitHub via web interface
git pull
```

---

## Common Commands Quick Reference

```bash
# Configuration
git config --global user.name "Name"
git config --global user.email "email"

# Initialize
git init
git clone <url>

# Basic workflow
git status
git add <file>
git commit -m "message"
git log

# Branching
git branch <name>
git checkout <branch>
git merge <branch>

# Remote
git remote add origin <url>
git push -u origin main
git pull
git fetch

# Help
git help
git help <command>
```

---

## Next Steps

Once you're comfortable with these basics, move on to:
- **Intermediate Level**: Advanced branching, rebasing, stashing, conflict resolution
- **Advanced Level**: History manipulation, hooks, submodules, advanced workflows

---

## Additional Resources

- [Official Git Documentation](https://git-scm.com/doc)
- [Pro Git Book (Free)](https://git-scm.com/book/en/v2)
- [GitHub Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Visualizing Git](https://git-school.github.io/visualizing-git/)
- [Learn Git Branching (Interactive)](https://learngitbranching.js.org/)

---

**Ready to level up? Check out the Intermediate Git Tutorial! 🚀**