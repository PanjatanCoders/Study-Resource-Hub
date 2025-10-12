# Git Advanced Tutorial - Part 1: History Manipulation

## Advanced History Manipulation

### What is History Manipulation?

History manipulation in Git refers to the process of modifying, rewriting, or reorganizing commit history. This powerful feature allows you to clean up your commit timeline, remove sensitive data, fix mistakes, or create a more logical and readable project history.

**Why Manipulate History?**

1. **Clean up before sharing**: Remove messy "work in progress" commits
2. **Remove sensitive data**: Delete accidentally committed passwords, API keys, or private files
3. **Logical organization**: Combine related changes into single commits
4. **Fix mistakes**: Correct typos in commit messages or wrong author information
5. **Professional presentation**: Create clean history for pull requests and code reviews

**When History Manipulation is Safe:**

✅ **SAFE to rewrite:**
- Commits that exist only on your local machine
- Personal feature branches not yet pushed
- Commits on branches where you're the only developer
- With explicit team agreement on shared branches

❌ **NEVER rewrite:**
- Commits already pushed to shared/public repositories
- Main/master branch with multiple contributors
- Any branch others have based work on
- Published release commits

**The Golden Rule:**
> Never rewrite public history! Once commits are shared, they become part of the team's history and rewriting them causes problems for everyone.

---

### Interactive Rebase - The Swiss Army Knife

Interactive rebase is the most powerful tool for history manipulation. It allows you to modify multiple commits in one session by replaying them one at a time and giving you control over each.

**How Interactive Rebase Works:**

1. Git creates a temporary branch
2. Goes back to the base commit you specified
3. Replays each commit one by one
4. Lets you modify each commit during replay
5. Creates new commits with new SHAs

**All Interactive Rebase Operations:**

| Command | Shortcut | What It Does |
|---------|----------|--------------|
| `pick` | `p` | Use commit as-is (default) |
| `reword` | `r` | Change commit message only |
| `edit` | `e` | Stop to modify commit content |
| `squash` | `s` | Combine with previous commit, keep both messages |
| `fixup` | `f` | Combine with previous commit, discard this message |
| `drop` | `d` | Remove commit entirely |
| `exec` | `x` | Run shell command after this commit |
| `break` | `b` | Pause rebase here (resume with `git rebase --continue`) |
| `label` | `l` | Mark this point in history with a name |
| `reset` | `t` | Reset HEAD to a labeled point |
| `merge` | `m` | Create a merge commit |

### Basic Interactive Rebase

```bash
# Rebase last 5 commits
git rebase -i HEAD~5

# This opens your editor with:
pick a1b2c3d Add login feature
pick d4e5f6g Fix typo in login
pick h7i8j9k Add tests
pick l0m1n2o WIP: debugging
pick p3q4r5s Update documentation

# Change operations and save
```

**Example 1: Clean Up Messy Commits**

**Before:**
```bash
git log --oneline
p3q4r5s Update documentation
l0m1n2o WIP: debugging
h7i8j9k Add tests
d4e5f6g Fix typo in login
a1b2c3d Add login feature
```

**Interactive Rebase:**
```bash
git rebase -i HEAD~5

# In editor, change to:
pick a1b2c3d Add login feature
fixup d4e5f6g Fix typo in login    # Merge into previous, discard message
squash h7i8j9k Add tests            # Merge into previous, combine messages
drop l0m1n2o WIP: debugging         # Remove entirely
reword p3q4r5s Update documentation # Change message
```

**After:**
```bash
git log --oneline
a1a1a1a Update login documentation
b2b2b2b Add login feature with tests
```

**Example 2: Reword Multiple Commit Messages**

```bash
git rebase -i HEAD~3

# Change all 'pick' to 'reword'
reword a1b2c3d Old message 1
reword d4e5f6g Old message 2
reword h7i8j9k Old message 3

# Git will stop at each commit, letting you edit the message
```

**Example 3: Split a Large Commit**

Sometimes one commit contains multiple unrelated changes. Here's how to split it:

```bash
# Start rebase
git rebase -i HEAD~3

# Change 'pick' to 'edit' for commit to split
edit a1b2c3d Large commit with multiple changes
pick d4e5f6g Another commit

# Git stops at the commit
# Reset to previous commit but keep changes
git reset HEAD^

# Now stage and commit separately
git add file1.js
git commit -m "Add feature A"

git add file2.js
git commit -m "Add feature B"

git add file3.js
git commit -m "Add feature C"

# Continue rebase
git rebase --continue
```

### Advanced Interactive Rebase with Exec

The `exec` command runs a shell command after each commit. Perfect for ensuring tests pass after each change.

```bash
git rebase -i HEAD~5

# In editor:
pick a1b2c3d Add feature
exec npm test                       # Run tests after this commit
pick d4e5f6g Refactor code
exec npm test                       # Run tests again
pick h7i8j9k Update docs

# If tests fail, rebase stops
# Fix the issue, then:
git add .
git commit --amend
git rebase --continue
```

**Example: Auto-test Each Commit**

```bash
# Rebase and test all commits
git rebase -i HEAD~10

# In editor, add exec after each pick:
pick a1b2c3d Commit 1
exec npm test
pick d4e5f6g Commit 2
exec npm test
pick h7i8j9k Commit 3
exec npm test
```

---

### Autosquash - Automated Fixup Commits

Autosquash is a workflow that automatically squashes fixup commits into their parent commits during rebase.

**How Autosquash Works:**

1. You make a commit
2. Later, you find a bug in that commit
3. Create a fixup commit that references the original
4. During interactive rebase, Git automatically squashes them

**Creating Fixup Commits:**

```bash
# Original commit
git add feature.js
git commit -m "Add user authentication"
# Commit hash: a1b2c3d

# Later, find bug in that commit
git add feature.js
git commit --fixup a1b2c3d

# This creates commit with message: "fixup! Add user authentication"
```

**Creating Squash Commits:**

```bash
# Similar but keeps commit message
git commit --squash a1b2c3d
# Creates: "squash! Add user authentication"
```

**Using Autosquash:**

```bash
# Manual rebase with autosquash
git rebase -i --autosquash HEAD~10

# Git automatically organizes fixup commits:
pick a1b2c3d Add user authentication
fixup d4e5f6g fixup! Add user authentication  # Auto-placed here
pick h7i8j9k Another feature
```

**Enable Autosquash by Default:**

```bash
# Always use autosquash in interactive rebase
git config --global rebase.autosquash true

# Now you can just do:
git rebase -i HEAD~10
# Fixups are automatically organized
```

**Complete Workflow Example:**

```bash
# Day 1: Implement feature
git add auth.js
git commit -m "Add JWT authentication"
# Hash: abc1234

git add profile.js
git commit -m "Add user profile page"
# Hash: def5678

# Day 2: Find bugs
git add auth.js
git commit --fixup abc1234

git add profile.js
git commit --fixup def5678

# Day 3: Another bug in auth
git add auth.js
git commit --fixup abc1234

# Before pushing, clean up:
git rebase -i --autosquash HEAD~5

# Git automatically creates:
pick abc1234 Add JWT authentication
fixup ghi9012 fixup! Add JWT authentication
fixup jkl3456 fixup! Add JWT authentication
pick def5678 Add user profile page
fixup mno7890 fixup! Add user profile page

# Result: Clean history with just 2 commits
```

---

### Handling Rebase Conflicts

When rebasing, conflicts can occur just like with merges. Here's how to handle them effectively.

**Conflict During Rebase:**

```bash
# Start rebase
git rebase -i HEAD~5

# Conflict occurs
Auto-merging file.js
CONFLICT (content): Merge conflict in file.js
error: could not apply a1b2c3d... Add feature

# Git stops and shows:
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".
```

**Resolving Rebase Conflicts:**

```bash
# 1. Check which files have conflicts
git status

# 2. Open conflicted files and fix conflicts
# Look for conflict markers:
<<<<<<< HEAD
Current changes
=======
Incoming changes
>>>>>>> a1b2c3d... Add feature

# 3. After fixing conflicts, stage files
git add file.js

# 4. Continue rebase
git rebase --continue

# Git will continue replaying remaining commits
```

**Other Rebase Options:**

```bash
# Skip current commit (if you don't want it)
git rebase --skip

# Abort entire rebase (start over)
git rebase --abort

# Edit commit message after resolving conflicts
git rebase --continue
# Editor opens for commit message
```

**Pro Tips for Rebase Conflicts:**

1. **Small, frequent rebases**: Rebase often to avoid large conflict sets
2. **Use rerere**: Git can remember how you resolved conflicts
   ```bash
   git config --global rerere.enabled true
   ```
3. **Three-way diff**: Shows original, yours, and theirs
   ```bash
   git config --global merge.conflictstyle diff3
   ```

**Example: Complete Conflict Resolution**

```bash
# Start rebase
git rebase -i HEAD~10

# Conflict in commit 3
Auto-merging app.js
CONFLICT (content): Merge conflict in app.js

# Check status
git status
# Shows: both modified: app.js

# Open app.js, fix conflicts
# Remove conflict markers
<<<<<<< HEAD
function newImplementation() { ... }
=======
function oldImplementation() { ... }
>>>>>>> abc1234

# Choose one or combine both
function combinedImplementation() { ... }

# Stage resolved file
git add app.js

# Continue
git rebase --continue

# If another conflict, repeat
# If no more conflicts, rebase completes
```

---

### Best Practices for History Manipulation

**1. Always Work on a Branch**
```bash
# Create backup branch before rebase
git branch backup-before-rebase

# Do your rebase
git rebase -i HEAD~10

# If something goes wrong
git reset --hard backup-before-rebase
```

**2. Test After Rebasing**
```bash
# After rebase, ensure code still works
npm test
npm run build

# If tests fail, you may have introduced issues during rebase
```

**3. Rebase Before Pull Request**
```bash
# Update with main branch
git fetch origin
git rebase origin/main

# Clean up your commits
git rebase -i origin/main

# Force push to your branch
git push --force-with-lease
```

**4. Use --force-with-lease Instead of --force**
```bash
# Safer force push (fails if remote changed)
git push --force-with-lease

# Regular force push (dangerous, overwrites everything)
git push --force
```

**5. Document Major Rebases**
```bash
# Before major rebase, document what you're doing
git log --oneline > pre-rebase-commits.txt

# After rebase
git log --oneline > post-rebase-commits.txt

# Compare
diff pre-rebase-commits.txt post-rebase-commits.txt
```

