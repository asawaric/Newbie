
## Using branches

A branch represents an independent line of development. Branches serve as an abstraction for the edit/stage/commit process.

For more details read https://www.atlassian.com/git/tutorials/using-branches

**1] Create isolated development environments within a single repository**

git branch command lets you create, list, rename, and delete branches. It's a general purpose branch administration tool; a way to request a brand new working directory, staging are,and project hisotry. 

==================================

Checklist for git branch

==================================

git branch

git branch -r

git branch <*branch*>

git branch -d <*branch_to_be_deleted*>

git branch -m <*new_name_for_current_branch*>


**2] Naviagte between the branches**

git checkout lets you navigate between the branches created by git branch. "Checking" out branch updates the files in the working history to match the selected branch and it tells Git to record all the new commits on that branch. 

==================================

Checklist for git checkout

==================================

git checkout

git checkout <*branch_name*>

git checkout -b <*new_branch*>


**3] Integrating different branches into a single branch**

git merge is a powerful way to integrate changes from divergent branches. Merging is Git's way of putting a forked history back together again. 

==================================

Checklist for git merge

==================================

git merge

git merge <*branch*>

git merge --no-ff <*branch*>

git branch --merged

==================================

Exercises

==================================

EXERCISE 8.1 Checkout the current branch named master. Check all completely merged branches with the master branch of your local git repo.

EXERCISE 8.2 Create and checkout the new branch named local_branch_03 in your local git repo.

EXERCISE 8.3 Merge local_branch_03 into the current branch master of your local git repo and generate a merge commit. 


