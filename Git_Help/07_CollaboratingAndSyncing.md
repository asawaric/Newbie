
## Syncing

In Git's collaboration model, every developer is given their own copy of the repository complete with its own local history and branch structure. Users can share series of commits and even entire branches between repositories to manage connections with other repositories.

For more details read https://www.atlassian.com/git/tutorials/syncing

**1] Manage remote connections**

The git remote command is a convenient tool for administering remote connections. Instead of passing the full URL to the fetch, pull, and push commands, it lets you use a more meaningful shortcut to create, view, and delete connections to other repo.

===========================

Checklist for git remote

===========================

git remote

git remote -v 

git remote add <*remote_repo_name*> <*path_to_remote_repo*> 

git remote show <*name_of_remote_repo*>

git remote rename <*old_remote_repo_name*> <*new_remote_repo_name*>

git remote rm <*remote_repo_name*>


**2] Importing commits from remote repo**

git fetch imports commits from a remote repo into your local repo. The resulting commits are stored as remote branches and have no effect on your local developement work. This makes fetching a safe way to review commits before integrating them with your local repo.

===========================

Checklist for git fetch

===========================

git fetch

git fetch <*remote_repo_name*>

git fetch <*remote_repo_name*> <*branch_name*>

git branch -r


**3] Fetch + Merge**

git pull downloads a branch from a remote repo and immediately merges it into the current branch. It is an automated version of git fetch. 

===========================

Checklist for git pull

===========================

git pull

git pull --rebase <*remote*>

**4] Publish your contribution**

git push exports commits to remote branches. It's a convenient way to publish your contributions. However, git push can also overwrite changes, thus you must be careful with its use! 

============================

Checklist for git push

============================

git push

git push <*remote*>

git push <*remote*> <*branch*>


============================

Exercises

============================

EXERCISE 7.1 Create a remote branch named remote_branch_01 and check the updates from remote git repo.

EXERCISE 7.2 Check all remote branches of your remote git repo.

EXERCISE 7.3 Fetch a remote branch named remote_branch_01 from remote repo to my_local_repo.

EXERCISE 7.4 Create a branch named local_branch_02 in local git repo. Edit a file named new_local_file.txt and commit the changes on this new branch.
 
EXERCISE 7.5 Integrate the branch named local_branch_02 with local branch master using rebase.

EXERCISE 7.6 Create a tag in my_local_repo labeled v1.0 and push this local tag v1.0 to the remote git repo.


