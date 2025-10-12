# Git Tutorial - Intermediate Level

Master intermediate Git concepts and workflows.

---

## Table of Contents
- [Prerequisites](#prerequisites)
- [Advanced Branching & Merging](#advanced-branching--merging)
- [Handling Merge Conflicts](#handling-merge-conflicts)
- [Rebasing](#rebasing)
- [Stashing Changes](#stashing-changes)
- [Undoing Changes](#undoing-changes)
- [Tagging](#tagging)
- [Viewing Differences](#viewing-differences)
- [Cherry-Picking](#cherry-picking)
- [Collaboration Workflows](#collaboration-workflows)
- [Practice Exercises](#practice-exercises)

---

## Prerequisites

Before starting this tutorial, you should be comfortable with:
- Basic Git commands (init, add, commit, push, pull)
- Creating and switching branches
- Basic merging
- Working with remote repositories

---

## Advanced Branching & Merging

### Understanding Merge Types

**1. Fast-Forward Merge**
- Simplest type of merge
- No merge commit created
- Simply moves branch pointer forward
- Occurs when target branch hasn't diverged

```bash
# Create and commit on feature branch
git checkout -b feature
echo "new feature" > feature.txt
git add feature.txt
git commit -m "Add feature"

# Fast-forward merge
git checkout main
git merge feature
# Result: main pointer moves to feature's commit
```

**2. Three-Way Merge**
- Creates a new merge commit
- Combines two branches with common ancestor
- Preserves complete history

```bash
# Both branches have commits
git checkout main
git merge feature
# Result: New merge commit created
```

**3. Squash Merge**
- Combines all feature commits into one
- Keeps main branch clean
- Loses individual commit history

```bash
git checkout main
git merge --squash feature
git commit -m "Add complete feature"
```

### Merge Strategies

```bash
# Standard merge (creates merge commit if needed)
git merge feature-branch

# No fast-forward (always create merge commit)
git merge --no-ff feature-branch

# Squash all commits into one
git merge --squash feature-branch

# Abort a merge in progress
git merge --abort

# View merged branches
git branch --merged

# View unmerged branches
git branch --no-merged

# Delete remote branch after merge
git push origin --delete feature-branch

# Merge with custom commit message
git merge feature-branch -m "Merge feature X into main"

# Merge using specific strategy
git merge -X theirs feature-branch   # Prefer their changes
git merge -X ours feature-branch     # Prefer our changes
```

### When to Use Each Merge Type

**Use Fast-Forward When:**
- Linear history is desired
- Feature branch is simple
- Working alone or in small teams

**Use No-Fast-Forward (--no-ff) When:**
- Want to preserve feature branch history
- Working in teams
- Need to track when features were integrated

**Use Squash When:**
- Want clean main branch history
- Feature has many small commits
- Individual commits aren't important

---

## Handling Merge Conflicts

### What Causes Conflicts?

Conflicts occur when Git cannot automatically merge changes because:
- Same lines modified differently in both branches
- File modified in one branch, deleted in another
- Binary files changed differently
- Rename conflicts

### Understanding Conflict Markers

```
<<<<<<< HEAD (Current Branch)
Your current changes
Content from the branch you're on
=======
Incoming changes from the branch being merged
Content from the branch being merged in
>>>>>>> feature-branch (Incoming Branch)
```

**Additional Conflict Marker (diff3 style):**
```
<<<<<<< HEAD
Your changes
||||||| base
Original content (common ancestor)
=======
Their changes
>>>>>>> feature-branch
```

### Resolution Steps

1. Identify conflicted files with `git status`
2. Open files and locate conflict markers
3. Decide which changes to keep (or combine both)
4. Remove ALL conflict markers
5. Test the code
6. Stage resolved files with `git add`
7. Complete merge with `git commit`

### Resolving Conflicts

```bash
# Start merge (conflicts occur)
git merge feature-branch

# Check which files have conflicts
git status
# Shows: both modified: file.txt

# View conflict in file
cat file.txt

# Option 1: Edit manually
nano file.txt
# Remove markers, keep desired content

# Option 2: Use merge tool
git mergetool

# Option 3: Choose one version entirely
git checkout --ours file.txt     # Keep your version
git checkout --theirs file.txt   # Keep their version

# After resolving conflicts
git add file.txt

# Continue the merge
git commit -m "Resolve merge conflicts between main and feature"

# Or if you want to abort
git merge --abort
```

### Configure Merge Tool

```bash
# Set VS Code as merge tool
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'

# Set diff3 conflict style (shows common ancestor)
git config --global merge.conflictstyle diff3

# Disable backup files (.orig)
git config --global mergetool.keepBackup false

# Use vimdiff
git config --global merge.tool vimdiff

# Use meld
git config --global merge.tool meld
```

### Conflict Resolution Example

**Original file (base):**
```python
def calculate(a, b):
    return a + b
```

**Your changes (HEAD):**
```python
def calculate(a, b):
    """Calculate sum of two numbers"""
    return a + b
```

**Their changes (feature-branch):**
```python
def calculate(a, b):
    result = a + b
    return result
```

**After merge conflict:**
```python
def calculate(a, b):
<<<<<<< HEAD
    """Calculate sum of two numbers"""
    return a + b
=======
    result = a + b
    return result
>>>>>>> feature-branch
```

**Resolution (combine both):**
```python
def calculate(a, b):
    """Calculate sum of two numbers"""
    result = a + b
    return result
```

### Best Practices

- **Communicate**: Discuss with team before merging large changes
- **Pull frequently**: Stay updated to minimize conflicts
- **Small commits**: Easier to understand conflicts
- **Test after resolving**: Ensure code still works
- **Keep branches short-lived**: Reduces conflict probability

---

## Rebasing

### Rebase vs Merge

**Merge:**
- ✅ Preserves complete history
- ✅ Safe for shared branches
- ❌ Can create complex history graph
- ❌ Creates merge commits

**Rebase:**
- ✅ Creates linear history
- ✅ Cleaner commit log
- ❌ Rewrites history (dangerous for shared branches)
- ❌ Can cause conflicts at each step

### When to Use Rebase

**DO use rebase for:**
- Cleaning up local commits before pushing
- Keeping feature branch updated with main
- Creating clean, linear history
- Squashing related commits

**DON'T use rebase for:**
- Commits already pushed to shared repository
- Public branches (main, develop)
- Collaborative feature branches

**⚠️ Golden Rule: Never rebase commits that have been pushed to a shared repository!**

### Basic Rebase

```bash
# Update feature branch with latest main
git checkout feature-branch
git rebase main

# If conflicts occur
# 1. Resolve conflicts in files
# 2. Stage resolved files
git add resolved-file.txt
# 3. Continue rebase
git rebase --continue

# Skip current commit if needed
git rebase --skip

# Abort rebase and return to original state
git rebase --abort
```

### Interactive Rebase

Interactive rebase allows you to modify commits during the rebase process.

**Operations:**
- `pick` (p): Keep commit as-is
- `reword` (r): Change commit message
- `edit` (e): Stop to amend commit
- `squash` (s): Combine with previous commit, keep both messages
- `fixup` (f): Combine with previous commit, discard this message
- `drop` (d): Remove commit
- `exec` (x): Run shell command

```bash
# Interactive rebase last 3 commits
git rebase -i HEAD~3

# Interactive rebase from specific commit
git rebase -i abc1234

# Example: Editor opens with
pick a1b2c3d First commit
pick d4e5f6g Second commit
pick h7i8j9k Third commit

# Change to:
pick a1b2c3d First commit
squash d4e5f6g Second commit  # Combine with first
reword h7i8j9k Third commit    # Change message
```

### Practical Rebase Examples

**Example 1: Clean up commits before PR**
```bash
# You have messy commits
git log --oneline
# h7i8j9k Fix typo
# d4e5f6g WIP
# a1b2c3d Add feature

# Clean up last 3 commits
git rebase -i HEAD~3

# In editor, change to:
pick a1b2c3d Add feature
fixup d4e5f6g WIP           # Merge into previous
fixup h7i8j9k Fix typo      # Merge into previous

# Result: One clean commit
```

**Example 2: Update feature with main**
```bash
# Feature branch is behind main
git checkout feature-branch
git fetch origin
git rebase origin/main

# If conflicts, resolve and continue
git add .
git rebase --continue

# Force push (since history changed)
git push --force-with-lease
```

**Example 3: Split a commit**
```bash
# Rebase to edit commit
git rebase -i HEAD~1

# Change 'pick' to 'edit'
edit a1b2c3d Combined changes

# Reset to previous commit (keep changes)
git reset HEAD^

# Stage and commit separately
git add file1.txt
git commit -m "Add file1"

git add file2.txt
git commit -m "Add file2"

# Continue rebase
git rebase --continue
```

### Autosquash

Automatically squash fixup commits.

```bash
# Create fixup commit for specific commit
git commit --fixup a1b2c3d

# Create squash commit
git commit --squash a1b2c3d

# Rebase with autosquash
git rebase -i --autosquash HEAD~5

# Configure autosquash by default
git config --global rebase.autosquash true
```

---

## Stashing Changes

### What is Stashing?

Stashing temporarily shelves changes so you can work on something else, then come back and re-apply them later.

### When to Use Stash

- Need to switch branches quickly
- Pull updates but have uncommitted changes
- Experiment without committing
- Context switching (urgent bug fix)

### Basic Stashing

```bash
# Stash tracked files
git stash

# Stash with descriptive message
git stash save "WIP: login feature"

# Stash including untracked files
git stash -u
git stash --include-untracked

# Stash including ignored files
git stash -a
git stash --all

# List all stashes
git stash list
# stash@{0}: WIP on main: a1b2c3d commit message
# stash@{1}: On feature: d4e5f6g another message

# Show stash contents
git stash show
git stash show -p              # Full diff
git stash show stash@{1}       # Specific stash
```

### Applying Stashes

```bash
# Apply most recent stash (keeps in stash list)
git stash apply

# Apply and remove (pop) most recent stash
git stash pop

# Apply specific stash
git stash apply stash@{2}

# Pop specific stash
git stash pop stash@{1}

# Apply stash to different branch
git stash branch new-branch stash@{0}
```

### Managing Stashes

```bash
# Delete specific stash
git stash drop stash@{1}

# Clear all stashes
git stash clear

# Create branch from stash
git stash branch feature-from-stash
```

### Partial Stashing

```bash
# Stash interactively (choose what to stash)
git stash -p

# For each hunk, choose:
# y - stash this hunk
# n - don't stash this hunk
# q - quit
# a - stash this and remaining hunks
# d - don't stash this and remaining hunks
```

### Practical Example

```bash
# Working on feature
git checkout feature-branch
echo "work in progress" > file.txt
git add file.txt

# Urgent bug needs fixing!
git stash save "Half-done login feature"

# Fix bug on main
git checkout main
git checkout -b hotfix
# ... fix bug ...
git commit -am "Fix urgent bug"

# Return to feature work
git checkout feature-branch
git stash pop

# Continue where you left off
```

---

## Undoing Changes

### Understanding Undo Levels

1. **Working Directory**: `git restore` / `git checkout`
2. **Staging Area**: `git restore --staged` / `git reset`
3. **Repository**: `git revert` / `git reset`

### Reset Types

- `--soft`: Moves HEAD, keeps staging and working directory
- `--mixed` (default): Moves HEAD, keeps working directory
- `--hard`: Moves HEAD, resets staging and working directory (⚠️ DANGEROUS!)

### Discard Working Directory Changes

```bash
# Discard changes in file (old syntax)
git checkout -- file.txt

# Discard changes (new syntax, Git 2.23+)
git restore file.txt

# Discard all changes
git restore .

# Discard changes in directory
git restore src/
```

### Unstage Files

```bash
# Unstage file (old syntax)
git reset HEAD file.txt

# Unstage file (new syntax)
git restore --staged file.txt

# Unstage all files
git restore --staged .
```

### Amend Last Commit

```bash
# Add forgotten file to last commit
git add forgotten-file.txt
git commit --amend --no-edit

# Change last commit message
git commit --amend -m "Better commit message"

# Amend and edit message in editor
git commit --amend
```

### Reset Commits

```bash
# Undo last commit, keep changes staged
git reset --soft HEAD~1

# Undo last commit, keep changes unstaged
git reset HEAD~1
git reset --mixed HEAD~1    # Same as above

# Undo last commit, discard all changes (DANGEROUS!)
git reset --hard HEAD~1

# Reset to specific commit
git reset --hard abc1234

# Undo last 3 commits, keep changes
git reset HEAD~3
```

### Revert Commits (Safe for Shared Branches)

```bash
# Revert a commit (creates new commit)
git revert abc1234

# Revert without auto-commit
git revert -n abc1234
git revert --no-commit abc1234

# Revert a range of commits
git revert HEAD~3..HEAD

# Revert merge commit (specify parent)
git revert -m 1 merge-commit-hash
```

### When to Use Each

| Command | Use Case | Safe for Shared? |
|---------|----------|------------------|
| `git restore` | Discard working changes | ✅ Yes |
| `git reset --soft` | Redo last commit | ❌ No (if pushed) |
| `git reset --mixed` | Unstage files | ❌ No (if pushed) |
| `git reset --hard` | Start over | ❌ No (if pushed) |
| `git revert` | Undo pushed commits | ✅ Yes |

### Practical Examples

**Undo last commit, redo with more changes:**
```bash
git reset --soft HEAD~1
git add forgotten-file.txt
git commit -m "Complete feature implementation"
```

**Accidentally committed to wrong branch:**
```bash
# On wrong-branch
git log --oneline  # Note commit hash

# Move commit to correct branch
git checkout correct-branch
git cherry-pick abc1234

# Remove from wrong branch
git checkout wrong-branch
git reset --hard HEAD~1
```

---

## Tagging

### What are Tags?

Tags mark specific points in history, typically for releases. Unlike branches, tags don't move.

### Tag Types

**Lightweight Tags:**
- Simple pointer to a commit
- Like a branch that doesn't move
- No additional metadata

**Annotated Tags (Recommended):**
- Full Git objects with metadata
- Tagger name, email, date
- Tag message
- Can be signed with GPG

### Semantic Versioning

Format: `vMAJOR.MINOR.PATCH` (e.g., v1.4.2)
- **MAJOR**: Breaking changes
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes

### Creating Tags

```bash
# Lightweight tag
git tag v1.0.0

# Annotated tag (recommended)
git tag -a v1.0.0 -m "Release version 1.0.0"

# Annotated tag with detailed message
git tag -a v1.0.0
# Opens editor for multi-line message

# Tag specific commit
git tag -a v1.0.0 abc1234 -m "Version 1.0.0"

# Tag with current date
git tag -a v1.0.0 -m "Release $(date +%Y-%m-%d)"
```

### Listing and Viewing Tags

```bash
# List all tags
git tag

# List tags matching pattern
git tag -l "v1.8.*"
git tag -l "v2.*"

# Show tag information
git show v1.0.0

# List tags with commit messages
git tag -n
git tag -n3  # Show first 3 lines of annotation

# List tags sorted by version
git tag --sort=version:refname

# List tags with dates
git log --tags --simplify-by-decoration --pretty="format:%ai %d"
```

### Pushing Tags

```bash
# Push single tag
git push origin v1.0.0

# Push all tags
git push origin --tags

# Push only annotated tags
git push origin --follow-tags

# Configure to always push annotated tags
git config --global push.followTags true
```

### Deleting Tags

```bash
# Delete local tag
git tag -d v1.0.0

# Delete remote tag
git push origin --delete v1.0.0
git push origin :refs/tags/v1.0.0  # Alternative
```

### Checking Out Tags

```bash
# Checkout tag (creates detached HEAD)
git checkout v1.0.0

# Create branch from tag
git checkout -b version1-bugfix v1.0.0

# View files at tag without checkout
git show v1.0.0:path/to/file.txt
```

### Release Workflow

```bash
# 1. Ensure you're on main with latest code
git checkout main
git pull origin main

# 2. Run tests
npm test

# 3. Update version in files if needed
# (package.json, version.txt, etc.)

# 4. Commit version bump
git commit -am "Bump version to 1.2.0"

# 5. Create annotated tag
git tag -a v1.2.0 -m "Release 1.2.0: Added user authentication

- Implement JWT-based authentication
- Add login/logout endpoints
- Update user profile management"

# 6. Push commits and tags
git push origin main
git push origin v1.2.0
```

---

## Viewing Differences

### Understanding Diff

Diff shows changes between:
- Working directory and staging
- Staging and last commit
- Two commits
- Two branches

### Basic Diff

```bash
# Show unstaged changes
git diff

# Show staged changes
git diff --staged
git diff --cached

# Show all changes (staged + unstaged)
git diff HEAD

# Show changes for specific file
git diff file.txt
git diff --staged file.txt
```

### Comparing Commits and Branches

```bash
# Compare two commits
git diff abc1234 def5678

# Compare with previous commit
git diff HEAD~1 HEAD

# Compare branches
git diff main..feature-branch

# Show changes in feature since branching from main
git diff main...feature-branch

# Compare specific file across branches
git diff main:file.txt feature:file.txt
```

### Diff Output Options

```bash
# Show only filenames
git diff --name-only

# Show filenames with status (A=Added, M=Modified, D=Deleted)
git diff --name-status

# Show statistics
git diff --stat

# Word-level diff (not line-level)
git diff --word-diff

# Character-level diff
git diff --word-diff=color --word-diff-regex=.

# Ignore whitespace
git diff -w
git diff --ignore-all-space

# Show function/class names
git diff -p
```

### Show Command

```bash
# Show last commit
git show HEAD

# Show specific commit
git show abc1234

# Show file from specific commit
git show abc1234:path/to/file.txt

# Show commit with stats
git show --stat abc1234

# Show only files changed
git show --name-only abc1234
```

### Diff Tools

```bash
# Configure external diff tool
git config --global diff.tool vimdiff

# Use external diff tool
git difftool

# Compare branches with tool
git difftool main..feature-branch

# Configure VS Code as difftool
git config --global diff.tool vscode
git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'
```

### Practical Examples

**Review before committing:**
```bash
git add .
git diff --staged
```

**Compare your branch with main:**
```bash
git diff main...feature-branch --stat
```

**Find what changed in last week:**
```bash
git diff HEAD@{1.week.ago} HEAD
```

---

## Cherry-Picking

### What is Cherry-Picking?

Cherry-picking applies specific commits from one branch to another, copying the commit rather than moving it.

### When to Use

- Apply hotfix to multiple branches
- Port feature to release branch
- Recover specific commits after rebase
- Apply bug fix without merging entire branch

### Basic Cherry-Pick

```bash
# Cherry-pick single commit
git cherry-pick abc1234

# Cherry-pick multiple commits
git cherry-pick abc1234 def5678 ghi9012

# Cherry-pick range of commits (exclusive start)
git cherry-pick abc1234..def5678

# Cherry-pick without auto-commit
git cherry-pick -n abc1234
git cherry-pick --no-commit abc1234
```

### Handling Cherry-Pick Conflicts

```bash
# Start cherry-pick (conflict occurs)
git cherry-pick abc1234

# Resolve conflicts
# Edit files, then:
git add resolved-file.txt

# Continue cherry-pick
git cherry-pick --continue

# Abort cherry-pick
git cherry-pick --abort

# Skip this commit
git cherry-pick --skip
```

### Cherry-Pick Options

```bash
# Cherry-pick with different commit message
git cherry-pick abc1234 -e

# Cherry-pick and add "cherry picked from" note
git cherry-pick -x abc1234

# Cherry-pick using merge strategy
git cherry-pick -X theirs abc1234

# Cherry-pick and sign off
git cherry-pick -s abc1234
```

### Practical Example

**Apply hotfix to multiple release branches:**
```bash
# Hotfix committed to main
git checkout main
git log --oneline  # Note hotfix commit: abc1234

# Apply to release-2.0
git checkout release-2.0
git cherry-pick abc1234

# Apply to release-1.9
git checkout release-1.9
git cherry-pick abc1234

# Push all branches
git push origin main release-2.0 release-1.9
```

---

## Collaboration Workflows

### Feature Branch Workflow

```bash
# 1. Create feature branch
git checkout -b feature/user-authentication

# 2. Make changes and commit
git add .
git commit -m "Implement JWT authentication"

# 3. Keep branch updated with main
git fetch origin
git rebase origin/main

# 4. Push to remote
git push -u origin feature/user-authentication

# 5. Create Pull Request (on GitHub/GitLab)

# 6. Address review comments
git add .
git commit -m "Address review feedback"
git push

# 7. After PR is merged, clean up
git checkout main
git pull origin main
git branch -d feature/user-authentication
```

### Gitflow Workflow

**Branches:**
- `main`: Production-ready code
- `develop`: Integration branch
- `feature/*`: New features
- `release/*`: Release preparation
- `hotfix/*`: Urgent production fixes

```bash
# Start new feature
git checkout develop
git checkout -b feature/new-feature

# Work on feature
git add .
git commit -m "Add new feature"

# Finish feature
git checkout develop
git merge --no-ff feature/new-feature
git branch -d feature/new-feature
git push origin develop

# Start release
git checkout -b release/1.2.0 develop
# Bump version, fix bugs
git commit -am "Prepare release 1.2.0"

# Finish release
git checkout main
git merge --no-ff release/1.2.0
git tag -a v1.2.0 -m "Release 1.2.0"
git push origin main --tags

git checkout develop
git merge --no-ff release/1.2.0
git push origin develop

git branch -d release/1.2.0

# Hotfix
git checkout -b hotfix/critical-bug main
git commit -am "Fix critical bug"

git checkout main
git merge --no-ff hotfix/critical-bug
git tag -a v1.2.1 -m "Hotfix 1.2.1"

git checkout develop
git merge --no-ff hotfix/critical-bug

git branch -d hotfix/critical-bug
```

### Forking Workflow

```bash
# 1. Fork repository on GitHub

# 2. Clone your fork
git clone https://github.com/yourname/repo.git
cd repo

# 3. Add upstream remote
git remote add upstream https://github.com/original/repo.git

# 4. Create feature branch
git checkout -b feature/my-feature

# 5. Make changes
git add .
git commit -m "Add my feature"

# 6. Fetch upstream changes
git fetch upstream
git rebase upstream/main

# 7. Push to your fork
git push origin feature/my-feature

# 8. Create Pull Request to upstream

# 9. Keep fork updated
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

---

## Practice Exercises

### Exercise 1: Merge Conflict Resolution

```bash
# Setup
git init conflict-practice
cd conflict-practice
echo "Line 1" > file.txt
git add file.txt
git commit -m "Initial commit"

# Create branch and modify
git checkout -b feature
echo "Line 1 - Feature change" > file.txt
git commit -am "Feature change"

# Modify on main
git checkout main
echo "Line 1 - Main change" > file.txt
git commit -am "Main change"

# Create conflict
git merge feature
# Resolve conflict, then commit
```

### Exercise 2: Interactive Rebase

```bash
# Create messy commits
git checkout -b cleanup
echo "a" > file1.txt && git add . && git commit -m "Add file1"
echo "b" > file2.txt && git add . && git commit -m "WIP"
echo "c" > file3.txt && git add . && git commit -m "Add file3"
echo "d" >> file1.txt && git add . && git commit -m "Fix typo"

# Clean up with interactive rebase
git rebase -i HEAD~4
# Squash "WIP" and "Fix typo" into previous commits
```

### Exercise 3: Stash Workflow

```bash
# Start work
git checkout -b feature/stash-test
echo "work in progress" > wip.txt
git add wip.txt

# Emergency: stash and switch
git stash save "WIP on feature"
git checkout main

# Do urgent work
echo "hotfix" > fix.txt
git add fix.txt
git commit -m "Urgent hotfix"

# Return to feature
git checkout feature/stash-test
git stash pop
```

### Exercise 4: Cherry-Pick Practice

```bash
# Create branches with commits
git checkout -b branch-a
echo "feature A" > a.txt && git add . && git commit -m "Feature A"
echo "bugfix" > fix.txt && git add . && git commit -m "Bug fix"

git checkout main
git checkout -b branch-b

# Cherry-pick just the bug fix
git log branch-a --oneline  # Note bug fix commit hash
git cherry-pick <bugfix-hash>
```

---

## Common Pitfalls and Solutions

### Committed to Wrong Branch

```bash
# Reset on wrong branch
git reset --soft HEAD~1

# Switch and commit
git checkout correct-branch
git commit -m "Commit message"
```

### Accidentally Reset Hard

```bash
# Use reflog to recover
git reflog
git reset --hard HEAD@{1}
```

### Merge When Should Have Rebased

```bash
# Undo merge
git reset --hard ORIG_HEAD

# Rebase instead
git rebase main
```

### Pushed Broken Code

```bash
# Fix and force push (if no one pulled)
git commit --amend
git push --force-with-lease

# Or revert (if others pulled)
git revert HEAD
git push
```

---

## Quick Reference

```bash
# Merging
git merge <branch>           # Standard merge
git merge --no-ff <branch>   # Force merge commit
git merge --squash <branch>  # Squash merge

# Rebasing
git rebase main              # Rebase onto main
git rebase -i HEAD~3         # Interactive rebase
git rebase --continue        # Continue after conflict

# Stashing
git stash                    # Stash changes
git stash pop                # Apply and remove
git stash list               # List stashes

# Undoing
git reset --soft HEAD~1      # Undo commit, keep staged
git reset HEAD~1             # Undo commit, keep changes
git reset --hard HEAD~1      # Undo commit, discard changes
git revert <commit>          # Revert commit safely

# Tagging
git tag -a v1.0.0 -m "msg"  # Annotated tag
git push origin v1.0.0       # Push tag

# Cherry-picking
git cherry-pick <commit>     # Apply commit
```

---

## Next Steps

Ready for advanced topics?
- History manipulation and filtering
- Git hooks for automation
- Submodules and worktrees
- Advanced reflog usage
- Performance optimization

**Continue to the Advanced Git Tutorial! 🚀**