
## Saving/Adding changes to a repository

Once we have initiated the project in a repository, we can start composing the changes and add it to the project. This section will explain the commands needed to add and commit changes to your project. 

Detailed tutorial found at https://www.atlassian.com/git/tutorials/saving-changes/git-add

**1] Adding changes to a project**

git add command adds the changes done in the working directory to staging area. It tells git that you want to include updates to a particular file in the project.

=====================

Checklist of git add

=====================

git add

git add <*file*>

git add <*directory*>

git add -p

What's the purpose of the -p flag?


**2] Commit changes to a repository**

git commit takes the staged changes and commits it to the project history. 

=========================

Checklist of git commit

=========================

git commit

git commit -a

git commit -a -m <*commit_message_in_double_quotes*>

===========================

Exercises

===========================

EXERCISE 2.1 Add new empty file named "my_new_file.txt" and a folder "my_new_folder" to the local git repository named my_local_repo. You should create this local repo if it is absent.

EXERCISE 2.2 Commit the addition of new file to the git repo with brief message.

