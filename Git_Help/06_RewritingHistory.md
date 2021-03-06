
## Rewriting history

To retain total control over your development workflow and never lose a committed change, Git provides its history-rewriting commands.

**Caution! : Using some of these commands for commits in public repositories may result in data loss!**

For more details see https://www.atlassian.com/git/tutorials/rewriting-history/git-commit--amend

**1] Amending staged changes**

git commit --amend lets you combine newly staged changes with previous commit. But not only does it alter the most recent commit, it replaces it entirely. Hence, do not ammend to public history!  

=================================

Checklist for git commit --amend

=================================

git commit --amend

git commit --amend --no-edit


**2] Rebasing a branch**

git rebase moves a branch from one commit to another. Git accomplishes this by creating new commits and applying them to the specified base. This process rewrites a project history, so do not rebase in public hisotry!

Interactive rebasing allows you to clean up hisotry by removing, splitting, and altering an existing series of commits. 

==================================

Checklist for git rebase

==================================

git rebase

git rebase <*base*>

git rebase -i


**3] Keep track of the updates**

After rewriting history, the reflog contains information about the old state of the branches and allows you to go back to that state if necessary. Every time the current HEAD gets updated a new entry will be added to the reflog.

==================================

Checklist for git reflog

==================================

git reflog

git reflog --relative-date


===================================

Exercises

===================================

EXERCISE 6.1 Create a new branch named local_branch_01.

EXERCISE 6.2 Edit my_new_file and commit these changes to my_new_branch.

EXERCISE 6.3 Edit another file named my_second_file.txt in the master branch and commit the changes to the master branch.

EXERCISE 6.4 Update most recent commit message for the most recent commit made to the git repo .

EXERCISE 6.5 Rebase local_branch_01 onto the changes made to the master branch and then merge these into the master branch.

EXERCISE 6.6 Change the order of the commits made to the my_local_repo and transfer to the master.

EXERCISE 6.7 Check the reflog for my_local_repo.


























