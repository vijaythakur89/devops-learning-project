# Git Practice Lab for Beginners

This lab is designed for someone learning Git from zero.

The exercises are intentionally practical.

Follow them in order and do not skip the verification steps.

---

# Lab 1 — Check Git Installation

Check whether Git is installed:

git --version

## Lab 2 — Configure Git Identity

Check your configured username:

git config --global user.name

Check your configured email:

git config --global user.email

These values are used to identify the author of your commits.

## Lab 3 — Create a Project Directory

Create a practice directory:

mkdir git-practice

Enter it:

cd git-practice

Check your current directory:

pwd

## Lab 4 — Initialize a Git Repository

Initialize Git:

git init

Expected message will indicate that an empty Git repository was initialized.

Check the directory:

ls -la

You should see:

.git

## Lab 5 — Check Repository Status

Run:

git status

At this point there should be no commits.

Git should report that there is nothing committed yet.

## Lab 6 — Create a File

Create a README:

touch README.md

Check the file:

ls

Then check Git:

git status

Git should show README.md as an untracked file.

## Lab 7 — Add Content

Add some content:

echo "# Git Practice Project" > README.md

View the file:

cat README.md

## Lab 8 — Understand Untracked Files

Run:

git status

You should see:

README.md

under untracked files.

This means Git sees the file but it has not been added to the staging area.

## Lab 9 — Stage a File

Stage the README:

git add README.md

Check the status:

git status

The file should now appear under:

Changes to be committed

## Lab 10 — Review Staged Changes

Run:

git diff --staged

Review what will be included in the commit.

## Lab 11 — Create Your First Commit

Create a commit:

git commit -m "Add README"

Then check:

git status

The working tree should be clean.

## Lab 12 — View Commit History

Run:

git log

Then try the shorter version:

git log --oneline

## Lab 13 — Modify an Existing File

Add another line:

echo "Learning Git step by step" >> README.md

Check the file:

cat README.md

## Lab 14 — Review Unstaged Changes

Run:

git status

Then:

git diff

You should see the newly added line.

## Lab 15 — Stage and Commit the Change

Stage the file:

git add README.md

Review the staged change:

git diff --staged

Commit it:

git commit -m "Update README"

## Lab 16 — Create a Branch

Create a feature branch:

git switch -c feature/add-description

Check your branches:

git branch

The current branch should have * beside it.

## Lab 17 — Make a Change on the Feature Branch

Edit the README:

echo "This repository is used to practice Git." >> README.md

Review the change:

git diff

## Lab 18 — Commit the Feature

Stage:

git add README.md

Commit:

git commit -m "Add project description"

Check:

git status

## Lab 19 — Compare Branches

Compare the feature branch with main:

git diff main...feature/add-description

This shows the changes introduced by the feature branch relative to main.

## Lab 20 — Switch Between Branches

Switch to main:

git switch main

View the README:

cat README.md

Now switch back:

git switch feature/add-description

View the README again:

cat README.md

Observe the difference.

This demonstrates branch isolation.

## Lab 21 — Merge a Feature Branch

Switch to main:

git switch main

Merge the feature:

git merge feature/add-description

Check the history:

git log --oneline --decorate --graph --all

## Lab 22 — Create a Remote Repository

For this exercise, create an empty repository on GitHub.

Then connect the local repository to GitHub.

Example:

git remote add origin https://github.com/<username>/<repository>.git

Verify:

git remote -v

## Lab 23 — Push Main to GitHub

Push the main branch:

git push -u origin main

The -u option establishes upstream tracking.

After this, future pushes can normally use:

git push

## Lab 24 — Create a Remote Feature Branch

Create a new branch:

git switch -c feature/remote-test

Make a change:

echo "Testing remote branches" >> README.md

Stage and commit:

git add README.md
git commit -m "Test remote branch"

Push it:

git push -u origin feature/remote-test

## Lab 25 — Pull Request Workflow

After pushing a feature branch, create a Pull Request on GitHub.

The workflow is:

Feature Branch
      |
      | git push
      v
GitHub
      |
      | Pull Request
      v
Review
      |
      v
Merge
      |
      v
main

Using GitHub CLI:

gh pr create

View the Pull Request:

gh pr view <number>

Merge it:

gh pr merge <number>

## Lab 26 — Fetch Remote Changes

Download information from GitHub:

git fetch origin

View all branches:

git branch -a

View the history:

git log --oneline --decorate --graph --all

Remember:

git fetch downloads remote information but does not normally update your current branch.

## Lab 27 — Pull Remote Changes

Switch to main:

git switch main

Pull the latest changes:

git pull

Verify:

git status

## Lab 28 — Create a Merge Conflict

This exercise intentionally creates a conflict.

Start from main:

git switch main

Create a branch:

git switch -c feature/conflict-a

Edit the same line in a file.

Commit the change:

git add README.md
git commit -m "Change README from branch A"

Return to main:

git switch main

Create another branch:

git switch -c feature/conflict-b

Modify the same line differently.

Commit:

git add README.md
git commit -m "Change README from branch B"

Now merge the first branch into the second branch.

Git may report a conflict.

## Lab 29 — Resolve a Merge Conflict

When Git reports a conflict:

git status

Open the conflicted file.

Look for:

<<<<<<< HEAD
your version
=======
other version
>>>>>>> branch-name

Decide what the final content should be.

Remove the conflict markers.

Then stage the resolved file:

git add <file>

Complete the merge:

git commit

Verify:

git status

## Lab 30 — Create a .gitignore

Create the file:

touch .gitignore

Add examples:

echo ".env" >> .gitignore
echo "*.log" >> .gitignore

View it:

cat .gitignore

## Lab 31 — Test .gitignore

Create a file that should be ignored:

touch application.log

Run:

git status

The ignored file should not normally appear as an untracked file.

## Lab 32 — Practice git stash

Modify a tracked file:

echo "Temporary work" >> README.md

Check:

git status

Store the change temporarily:

git stash

Check:

git status

Restore the change:

git stash pop

Check:

git status

## Lab 33 — Practice git revert

First identify a commit:

git log --oneline

Select a commit that is safe to reverse.

Then:

git revert <commit>

Check the history:

git log --oneline

Notice that Git creates a new commit rather than deleting the original commit.

## Lab 34 — Practice Git Tags

Create a tag:

git tag v1.0.0

List tags:

git tag

Push the tag:

git push origin v1.0.0

Tags are commonly used to identify releases.

## Lab 35 — Inspect a Commit

Find a commit:

git log --oneline

Then inspect it:

git show <commit>

This helps understand exactly what changed in a commit.

## Lab 36 — Branch Cleanup

List branches:

git branch

After a feature branch has been merged, delete it locally:

git branch -d feature/add-description

Delete a remote branch when appropriate:

git push origin --delete feature/add-description

## Lab 37 — Git Troubleshooting Checklist

When something goes wrong, do not immediately start running random commands.

Start with:

git status

Then inspect:

git branch
git log --oneline --decorate --graph --all
git remote -v

If changes are unexpected:

git diff
git diff --staged

If remote state seems different:

git fetch origin

Then inspect:

git log --oneline --decorate --graph --all

## Lab 38 — Professional Mini Project

Practice the complete workflow:

1. Start from main
2. Create a feature branch
3. Make a change
4. Review with git diff
5. Stage the change
6. Review staged changes
7. Commit
8. Push the feature branch
9. Create a Pull Request
10. Review the Pull Request
11. Merge the Pull Request
12. Switch to main
13. Fetch remote changes
14. Pull the latest main
15. Verify git status
16. Review the final history

Useful commands:

git status
git branch
git diff
git diff --staged
git add
git commit
git push
git fetch
git pull
git log --oneline --decorate --graph --all
Git Practice Philosophy

Do not try to memorize every Git command.

Instead, ask yourself three questions:

Where am I?
git branch
What has changed?
git status
git diff
What is the history?
git log --oneline --decorate --graph --all

These three questions solve a surprising number of beginner Git problems.

Final Goal

By completing this lab, a beginner should be comfortable with:

Git repositories
Working directories
Staging
Commits
Branches
Remotes
Push
Fetch
Pull
Merge
Pull Requests
Merge conflicts
.gitignore
Stash
Revert
Tags
Branch cleanup
Basic Git troubleshooting
