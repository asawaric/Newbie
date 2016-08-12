
## Answers to Exercises 1 to 8

**Important: The exercises given are to be done using terminal commands and not using Git GUI.**

=======================================

**Exercises 1: Setting up a repository**

=======================================

EXERCISE 1.1 Create and initialize a local git repository named my_local_repo in your home directory, and list the contents of this repository.

SOLUTION : 

         cd ~

         mkdir my_local_rep
         
         cd my_local_repo
        
         git init
         
         ls -al

EXERCISE 1.2 Clone an existing remote git repository to home directory on your local machine using SSH key.

SOLUTION : 

         First, identify the remote git repository from which you'll like to clone. 

         To have your git repo ssh-only access, you must have a SSH key set for your Git repo. 
         See https://help.github.com/articles/generating-an-ssh-key/ to set up SSH key for your Git repo. Then,
         
         cd ~	
         
         git clone git@github.com:USERNAME/YOURREPOSITORY.git 

EXERCISE 1.3 Configure your user info (name, email, etc) and the text editor in your local git installation.

SOLUTION :   

         cd ~/my_local_repo

	     git config user.name <name> 
             
         git config user.email <email>  
             
         git config --system core.editor <editor>  

==============================

**Exercises 2: Saving changes**

==============================

EXERCISE 2.1 Add new empty file named "my_new_file.txt" and a folder "my_new_folder" to the local git repository named my_local_repo. You should create this local repo if its absent.

SOLUTION :

         cd ~/my_local_repo

	     touch my_new_file.txt
         
	     mkdir my_new_folder
         
	     git add my_new_file.txt
         
         git add my_new_folder

EXERCISE 2.2 Commit the addition of new file to the git repo with brief message.

SOLUTION :   

         git commit -m "Added new file" 

======================================

**Exercises 3: Inspecting a repository**

======================================

EXERCISE 3.1 Check the status of the working directory in your local git repo named my_local_repo.

SOLUTION :   

         cd ~/my_local_repo

         git status

EXERCISE 3.2 Create a ".gitignore" file in your project directory which lists the files to be ignored.

SOLUTION :   
 
         cd ~/my_local_repo 

	     touch .gitignore

EXERCISE 3.3 Check the history of commits made to the git repo as graph-summary.

SOLUTION :   
         
         cd ~/my_local_repo

         git log --graph --decorate --oneline

==================================

**Exercises 4: Viewing old commits**

==================================

EXERCISE 4.1 Checkout a previous version of any file in your local git repo. 

SOLUTION :   

          cd ~/my_local_repo

          git checkout <commit_id> <file_name>
             
          # If you have added my_new_file.txt to your repo from EXERCISE 2.1,
             
          git checkout my_new_file.txt 

EXERCISE 4.2 Compare two different versions of a file in your local git repo.

SOLUTION :   

          git diff HEAD 

          # If you have added my_new_file.txt to your repo from EXERCISE 2.1,
             
	      git diff HEAD my_new_file.txt
	     
==================================

**Exercises 5: Undoing changes**

==================================

EXERCISE 5.1 Checkout the most recent version of a file named my_new_file in your local git repo.

SOLUTION :   

         cd ~/my_local_repo

	     git checkout HEAD my_new_file

EXERCISE 5.2 Revert to the newly created commit in your local git repo.

SOLUTION :   

         cd ~/my_local_repo

	     git revert HEAD

EXERCISE 5.3 Unstage a tracked file named my_new_file.txt in your local git repo.

SOLUTION :   

         cd ~/my_local_repo

         git reset my_new_file.txt

EXERCISE 5.4 Remove untracked files from the current directory in your local git repo.

SOLUTION :  

         cd ~/my_local_repo/<*current_directory_name*>

         git clean -f

==================================

**Exercises 6: Rewriting history**

==================================

EXERCISE 6.1 Create a new branch named local_branch_01

SOLUTION :   

         git branch local_branch_01

EXERCISE 6.2 Edit my_new_file and commit these changes to my_new_branch.

SOLUTION :   

         git checkout local_branch_01

         gedit my_new_file  # edit and save the changes to the file
             
         git add my_new_file.txt
             
         git commit -m "Added a file to local_branch_01"

EXERCISE 6.3 Edit another file named my_second_file.txt in the master branch and commit the changes to the master branch

SOLUTION : 

         git checkout master

         gedit my_second_file  # edit and save the changes to the file
             
         git add my_second_file.txt
             
         git commit -m "Added second file"
             

EXERCISE 6.4 Update most recent commit message for the most recent commit made to the git repo.

SOLUTION :   

         git commit --amend -m "Added second file to master"

EXERCISE 6.5 Rebase local_branch_01 onto the changes made to the master branch and then merge these into the master branch.

SOLUTION :   

         git checkout local_branch_01

         git rebase master
             
         git checkout master
             
         git merge master

EXERCISE 6.6 Change the order of the commits made to the my_local_repo and transfer to the master.

SOLUTION :   

         git checkout local_branch_01

	     git rebase -i master

EXERCISE 6.7 Check the reflog for my_local_repo.

SOLUTION :   

         cd ~/my_local_repo

         git reflog

====================================

**Exercises 7: Collaborating: Syncing**

====================================

EXERCISE 7.1 Create a remote branch named remote_branch_01 and check the updates from remote git repo.

SOLUTION :   

         git push origin origin:refs/heads/remote_branch_01

         git fetch origin

EXERCISE 7.2 Check all remote branches of your remote git repo.

SOLUTION :   

         git branch -r

EXERCISE 7.3 Fetch a remote branch named remote_branch_01 from remote repo to my_local_repo.

SOLUTION :   

         cd ~/my_local_repo

         git fetch origin remote_branch_01

EXERCISE 7.4 Create a branch named local_branch_02 in local git repo. Edit a file named new_local_file.txt and commit the changes on this new branch.

SOLUTION :   

         cd ~/my_local_repo

         git branch local_branch_02
             
         gedit new_local_file.txt  # Edit and save changes to the file.
             
         git add new_local_file.txt
             
         git commit -m "added new_local_file" 

EXERCISE 7.5 Integrate the branch named local_branch_02 with local branch master using rebase.

SOLUTION :  

         git checkout local_branch_02

         git rebase master
             
         git checkout master
             
         git merge local_branch_02
             

EXERCISE 7.6 Create a tag in my_local_repo labeled v1.0 and push this local tag v1.0 to the remote git repo.

SOLUTION :  

         cd~/my_local_repo

         git tag v1.0       
             
         git push origin --tags

===========================================

**Exercises 8: Collaborating: Using branches**

===========================================

EXERCISE 8.1 Checkout the current branch named master. Check all completely merged branches with the master branch of your local git repo.

SOLUTION :  

         cd ~/my_local_repo

         git checkout master
             
         git branch --merged

EXERCISE 8.2 Create and checkout new branch named local_branch_03 in your local git repo.

SOLUTION :   

         cd ~/my_local_repo

         git checkout -b local_branch_03

EXERCISE 8.3 Merge local_branch_03 into the current branch master of your local git repo and generate a merge commit. 

SOLUTION :  

         cd ~/my_local_repo

         git checkout master
             
         git merge --no-ff local_branch_03

