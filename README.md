# Task 1: Introduction to Version Control and Git Basics

## Task Overview

This task focused on understanding version control fundamentals and exploring Git through hands-on practice. Key activities included Git installation, repository management, branching, conflict resolution, and remote repository integration with AI-assisted cheatsheet creation.

---

## Theory of Version Control

Version control tracks and manages file changes over time, enabling collaboration, history tracking, and error recovery.

**Version Control Types:**
- **Local VCS**: Single computer tracking
- **Centralized VCS**: Central server (SVN) - single point of failure
- **Distributed VCS**: Complete local copies (Git) - best for collaboration

**Git Benefits:** Complete local history, powerful branching, offline work, and industry-standard adoption.

---

## Git Installation and Configuration

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Hands-on Git Commands

### Basic Workflow
```bash
# Initialize repository
git init
echo "# Project" > README.md
git add .
git commit -m "Initial commit"

# Check status and history
git status
git log --oneline
```

### Branching and Merging
```bash
# Create feature branch
git checkout -b feature-navbar
echo "<nav>Menu</nav>" > navbar.html
git add navbar.html
git commit -m "Add navbar"

# Merge to main
git checkout main
git merge feature-navbar
```

### Merge Conflicts
```bash
# Create conflict, resolve manually, then:
git add resolved-file.txt
git commit -m "Resolve conflict"
```

### Git Revert (Undo Mistakes)
```bash
echo "Bug" > bug.js
git add bug.js
git commit -m "Buggy feature"
git revert HEAD  # Safely undo
```

### Cherry-Pick (Selective Commits)
```bash
git checkout -b experimental
# Multiple commits...
git checkout main
git cherry-pick <commit-hash>  # Apply specific commit only
```

---

## Remote Repository Interaction

```bash
# Connect to GitHub/GitLab
git remote add origin https://github.com/username/repo.git
git push -u origin main

# Clone and pull
git clone https://github.com/username/repo.git
git pull origin main
```

---

## Git Commands Cheatsheet (AI-Assisted)

A comprehensive cheatsheet covering 100+ Git commands was created using AI assistance, organized by categories with practical examples.

**📋 Access Cheatsheet:**  
[Git Commands Cheatsheet](https://github.com/28d33/Cheatsheets/blob/main/git.md)

---

## Learning Outcome

**Skills Achieved:**
- Mastered Git installation and configuration
- Proficient in basic workflow (add, commit, push, pull)
- Successfully managed branches and resolved conflicts
- Applied `git revert` for safe rollbacks
- Used `git cherry-pick` for selective integration
- Integrated local and remote repositories

**Challenges Overcome:**
- Understood merge conflict markers through practice
- Learned staging area concept via selective commits
- Distinguished revert (safe for shared) vs reset (local only)

**Proficiency Summary:**

| Skill | Level |
|-------|-------|
| Basic Commands | Advanced |
| Branching/Merging | Advanced |
| Remote Operations | Intermediate |
| Error Recovery | Intermediate |

---

**Task Status:** ✅ Completed  
**Next:** Task 2 - Advanced Git Operations

*Report demonstrates practical Git proficiency and AI-assisted learning.*
