# Git Theory for Beginners

This guide explains Git and GitHub concepts from beginner to basic professional usage.

---

## 1. What is Git?

Git is a **Distributed Version Control System (DVCS)**.

Git helps developers:

- Track changes
- Maintain project history
- Create branches
- Collaborate safely
- Compare changes
- Restore previous versions
- Merge work

Without Git, developers might create files like:

```text
document.txt
document-final.txt
document-final-v2.txt
document-final-real-final.txt
```

With Git, versions are represented by commits:

```text
Project
   |
   +-- Commit 1
   |
   +-- Commit 2
   |
   +-- Commit 3
```

---

## 2. Git vs GitHub

Git and GitHub are different.

### Git

Git is the version-control software installed on your computer.

Examples:

```bash
git status
git add
git commit
git branch
```

### GitHub

GitHub is a platform for hosting Git repositories and collaborating with other people.

GitHub provides:

* Remote repositories
* Pull Requests
* Code Reviews
* Issues
* GitHub Actions
* Repository permissions
* Project management

Simple model:

```text
Your Computer
     |
     | Git
     v
Local Repository
     |
     | git push
     v
GitHub Repository
     |
     | Pull Request
     v
Code Review
```

---

## 3. Git Repository

A Git repository is a project tracked by Git.

Running:

```bash
git init
```

creates a hidden `.git` directory.

Example:

```text
my-project/
├── README.md
├── application/
└── .git/
```

The `.git` directory contains Git's internal information such as:

* Commit history
* Branch information
* Configuration
* Git objects
* HEAD information

Do not manually modify `.git` unless you understand Git internals.

---

## 4. Working Directory

The **working directory** contains the files you are currently editing.

Example:

```text
devops-learning-project/
├── README.md
└── docs/
```

When a file changes, Git can detect that change.

---

## 5. Staging Area

The staging area contains changes selected for the next commit.

The basic model is:

```text
Working Directory
       |
       | git add
       v
Staging Area
       |
       | git commit
       v
Local Repository
```

Example:

```bash
git add README.md
```

---

## 6. Commit

A **commit** is a snapshot of staged changes.

Example:

```bash
git commit -m "Fix README"
```

A good commit normally represents one logical change.

Each commit has a unique commit hash.

Example:

```text
72ca30c
```

---

## 7. Branch

A branch is an independent line of development.

Example:

```text
main
 |
 +---- feature/login
 |
 +---- feature/payment
 |
 +---- fix/configuration
```

Create a branch:

```bash
git switch -c feature/my-feature
```

Switch branches:

```bash
git switch main
```

List branches:

```bash
git branch
```

---

## 8. Why Use Branches?

Branches allow developers to work without directly changing stable code.

Example:

```text
main
 |
 +---- feature/new-feature
          |
          +---- commits
```

After development:

```text
feature/new-feature
        |
        | Pull Request
        v
       main
```

---

## 9. Main Branch

`main` is commonly the primary branch.

It should generally contain stable and reviewed code.

A common workflow is:

```text
main
 |
 +---- feature branch
          |
          +---- Pull Request
                    |
                    v
                   main
```

---

## 10. Remote Repository

A remote repository is another copy of the repository, usually hosted on GitHub.

The conventional remote name is:

```text
origin
```

Check it:

```bash
git remote -v
```

Model:

```text
Local Repository
       |
       | origin
       v
GitHub Repository
```

---

## 11. Local vs Remote

Your local repository is on your computer.

The remote repository is hosted elsewhere, such as GitHub.

They can temporarily have different commits.

```text
Local main     → Commit A

GitHub main    → Commit B
```

Git provides commands to synchronize them.

---

## 12. git push

`git push` sends local commits to the remote repository.

```bash
git push
```

Model:

```text
Local Repository
       |
       | git push
       v
GitHub
```

---

## 13. git fetch

`git fetch` downloads information about changes from a remote repository.

```bash
git fetch origin
```

Important:

`git fetch` normally does not change your current working files or current branch.

Model:

```text
GitHub
   |
   | git fetch
   v
Local remote-tracking information
```

---

## 14. git pull

`git pull` gets remote changes and integrates them into the current branch.

Simplified model:

```text
git pull
   =
git fetch
   +
integrate changes
```

Example:

```bash
git pull
```

---

## 15. git merge

`git merge` combines changes from one branch into another.

Example:

```bash
git switch main
git merge feature/my-feature
```

Git may perform a fast-forward merge when possible.

---

## 16. Pull Request

A Pull Request (PR) is a request to merge changes from one branch into another on GitHub.

Typical workflow:

```text
Feature Branch
      |
      | git push
      v
GitHub
      |
      | Pull Request
      v
Code Review
      |
      v
Automated Checks
      |
      v
Approval
      |
      v
Merge
      |
      v
main
```

PRs allow teams to:

* Review code
* Discuss changes
* Run automated checks
* Approve changes
* Maintain an audit trail

---

## 17. git status

`git status` shows the current state of the repository.

It can show:

* Current branch
* Modified files
* Untracked files
* Staged changes
* Unstaged changes
* Remote tracking state

Example:

```bash
git status
```

A clean repository may show:

```text
nothing to commit, working tree clean
```

When unsure what is happening, start with:

```bash
git status
```

---

## 18. git diff

`git diff` shows changes.

Unstaged changes:

```bash
git diff
```

Staged changes:

```bash
git diff --staged
```

Compare branches:

```bash
git diff main...feature/my-feature
```

Review changes before committing.

---

## 19. git log

`git log` shows commit history.

Basic:

```bash
git log
```

Short:

```bash
git log --oneline
```

Graph:

```bash
git log --oneline --decorate --graph --all
```

The graph is useful for understanding branches and merges.

---

## 20. HEAD

`HEAD` represents the current location in Git history.

Example:

```text
HEAD -> main
```

means the current branch is `main`.

Simplified model:

```text
HEAD
 |
 v
main
 |
 v
Latest Commit
```

---

## 21. Tracking Branch

A local branch can track a remote branch.

Example:

```text
main
 |
 +---- origin/main
```

Git can then tell you whether your branch is:

* Up to date
* Ahead
* Behind
* Diverged

---

## 22. Fast-Forward Merge

A fast-forward merge moves a branch pointer forward without creating a separate merge commit.

Before:

```text
A---B---C
        ^
        main

A---B---C---D
            ^
            feature
```

After:

```text
A---B---C---D
            ^
            main
```

---

## 23. Merge Commit

A merge commit combines two different lines of development.

Example:

```text
       C---D
      /     \
A---B       M
      \     /
       E---F
```

`M` is the merge commit.

---

## 24. Merge Conflict

A merge conflict occurs when Git cannot automatically combine changes.

Example:

```text
<<<<<<< HEAD
Hello DevOps
=======
Hello Cloud
>>>>>>> feature
```

The developer must decide the correct final content.

After resolving the file:

```bash
git add <file>
git commit
```

Conflict resolution is an important Git skill.

---

## 25. .gitignore

`.gitignore` specifies files that Git should normally ignore.

Example:

```text
.env
*.log
node_modules/
__pycache__/
.terraform/
```

Never commit secrets such as:

```text
Passwords
API keys
Access tokens
Private keys
Cloud credentials
```

---

## 26. git clone

`git clone` creates a local copy of a remote repository.

Example:

```bash
git clone https://github.com/user/project.git
```

Model:

```text
GitHub Repository
       |
       | git clone
       v
Local Repository
```

---

## 27. git revert

`git revert` creates a new commit that reverses an earlier commit.

Example:

```text
A → B → C → D
        ^
     original

A → B → C → D → E
                ^
             revert
```

The original commit remains in history.

This is often safer for shared branches.

---

## 28. git reset

`git reset` changes the current branch reference and can also affect the staging area and working tree depending on the mode.

Common modes:

```bash
git reset --soft
git reset --mixed
git reset --hard
```

Be especially careful with:

```bash
git reset --hard
```

because it can discard local changes.

---

## 29. git stash

`git stash` temporarily stores uncommitted changes.

Example:

```bash
git stash
```

Restore them:

```bash
git stash pop
```

Typical use:

```text
Working on Feature A
        |
        | urgent task
        v
    git stash
        |
        v
Handle urgent task
        |
        v
   git stash pop
        |
        v
Continue Feature A
```

---

## 30. Git Tag

A tag is a named reference to a specific commit.

Tags are commonly used for releases.

Example:

```bash
git tag v1.0.0
```

Model:

```text
A---B---C---D
        ^
      v1.0.0
```

---

## 31. Branch Cleanup

After a feature branch has been merged, it can normally be deleted.

Local:

```bash
git branch -d feature/my-feature
```

Remote:

```bash
git push origin --delete feature/my-feature
```

Only delete branches when you are sure they are no longer needed.

---

## 32. Good Commit Messages

Good commit messages describe the logical change.

Good:

```text
Fix README grammar
Add health check endpoint
Update Docker configuration
Add Jenkins pipeline
```

Poor:

```text
changes
update
test
stuff
final
```

Good commit messages make troubleshooting and auditing easier.

---

## 33. Professional Git Workflow

A common workflow is:

```text
Create branch
      |
      v
Make changes
      |
      v
Review changes
      |
      v
git add
      |
      v
git commit
      |
      v
git push
      |
      v
Pull Request
      |
      v
Code Review
      |
      v
CI/CD checks
      |
      v
Merge
      |
      v
main
```

---

## 34. Git in DevOps

Git is often the starting point of a DevOps delivery pipeline.

Example:

```text
Developer
    |
    v
Git Repository
    |
    v
Pull Request
    |
    v
CI Pipeline
    |
    +---- Tests
    |
    +---- Security Scan
    |
    +---- Build
    |
    v
Container Image
    |
    v
Container Registry
    |
    v
Kubernetes
    |
    v
Production
```

This is why Git is an essential DevOps skill.

---

## 35. Git and Infrastructure as Code

DevOps teams commonly store infrastructure and deployment configuration in Git.

Examples:

* Terraform
* Ansible
* Kubernetes YAML
* Helm charts
* Jenkins pipelines
* Dockerfiles
* Application source code

Benefits include:

* Versioning
* Code review
* Auditing
* Rollback
* Collaboration
* Automation

GitOps builds on this idea by using Git as a source of desired operational state.

---

## 36. Beginner Golden Rules

### Rule 1 — Know your branch

```bash
git branch
```

### Rule 2 — Check repository state

```bash
git status
```

### Rule 3 — Review changes

```bash
git diff
```

### Rule 4 — Stage intentionally

```bash
git add <file>
```

### Rule 5 — Review staged changes

```bash
git diff --staged
```

### Rule 6 — Commit logical changes

```bash
git commit -m "Meaningful message"
```

### Rule 7 — Push your branch

```bash
git push
```

### Rule 8 — Use Pull Requests

Keep `main` stable and reviewed.

### Rule 9 — Keep secrets out of Git

Never commit credentials or secrets.

### Rule 10 — Understand destructive commands

Be careful with:

```bash
rm -rf
git reset --hard
git push --force
```

Never run destructive commands blindly.

---

## 37. Most Important Mental Model

Remember:

```text
Working Directory
       |
       | git add
       v
Staging Area
       |
       | git commit
       v
Local Repository
       |
       | git push
       v
Remote Repository
       |
       | Pull Request
       v
Code Review
       |
       | merge
       v
main
```

If you understand this model, Git becomes much easier to learn.

---

## 38. Summary

The fundamental Git workflow is:

```text
Edit
  ↓
git diff
  ↓
git add
  ↓
git commit
  ↓
git push
  ↓
Pull Request
  ↓
Review
  ↓
Merge
```

The goal is not to memorize every Git command.

The goal is to understand:

**What Git is doing, why we are doing it, and what state the repository is currently in.**

