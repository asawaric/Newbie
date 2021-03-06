
## Viewing old commits.

To see an old version of a file, old commits in the repository, git checkout loads any of these saved snapshots onto your local machine. Checking out old commits is a read-only operation.
Viewing old versions of your commit does not affect the current state of your project. 

Please see https://www.atlassian.com/git/tutorials/viewing-old-commits/ for more details.

**1] Checking out branches, old commits, files**

git checkout serves as a way to revert back to an old version of an individual file. You can re-commit the old version in a new snapshot as you would do any other file.
git checkout also lets you switch to a branch to work in it and then merge the work into a branch which contains stable work (such as 'master').

==========================

Checklist of git checkout

==========================

git checkout

git checkout -b <*branchname*>

git checkout <*commit_num*>

git checkout <*commit_num*> <*file*>

**2] Seeing differences between files, branches, etc.**

git diff shows all current local changes in working copy that are unstaged. You can also see changes that have already been added to the staging area.
git diff also gives details regarding how each branch is different from the other.

For more details, read:
https://www.git-tower.com/learn/git/ebook/en/command-line/advanced-topics/diffs and

https://git-scm.com/docs/git-diff 

=========================

checklist of git diff

=========================

git diff

git diff --staged

git diff <*branch1*> <*branch2*>

git difftool

==============================

Exercises

==============================

EXERCISE 4.1 Checkout a previous version of any file in your local git repo.

EXERCISE 4.2 Compare two different versions of a file in your local git repo.

