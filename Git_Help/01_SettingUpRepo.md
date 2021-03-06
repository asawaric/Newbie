
## Setting up a Repository

To store all kinds of your projects in a trackable way one can use the effective way of having one's own repository!

This page gives the list of most important git commands for setting up your own repository. 
For detail information please read
https://www.atlassian.com/git/tutorials/setting-up-a-repository and 
https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

The checklists of git commands helps reinforce your understanding and long-term memory of how to set up a repository.
You should be able to perform the exercises at the end of this document.


**1] Initialize a new repository** 

git init command creates a new repository. It creates a .git subdirectory in the project root, which contains all of the necessary metadata for the repo. You can also convert an existing directory to a git repository. (If you want to work in your local directory skip step 2)

========================

Checklist for git init

========================

git init

git init <*directory*>

git init --bare <*directory*>

what does --bare do in git init --bare?


**2] Clone a remote git repo** 

(start with step 2 when you want to work on a copy of remote directory)
git clone creates a local copy/copies of your project on a local machine so you can add your changes to it. One typically clones via HTTPS or SSH protocols in a one time operation. To set up passwordless ssh-login to your github repo, please follow steps mentioned here https://help.github.com/articles/generating-an-ssh-key/

========================

Checklist for git clone

========================

git clone  <*repo_name*>

git clone  <*repo_name*>  <*desk_directory*>


**3] Configure your repository** 

git config configures your git installation. It can define user info to prepferences to the behavior of a
repository.

=========================

Checklist for git config

=========================

git config

git config --global --edit

git config --global user.name  <*name*>

git config --global user.email  <*email*>

git config --global alias. <*alias-name*>  <*git-command*>

git config --system core.editor  <*editor*>

What is --global here?

and

What is --system?


===========================================

Exercises

===========================================

EXERCISE 1.1 Create and initialize a local git repository named my_local_repo in your home directory, and list the contents of this repository.

EXERCISE 1.2 Clone an existing remote git repository to home directory on your local machine using SSH key.

EXERCISE 1.3 Configure your user info (name, email, etc) and the text editor in your local git installation.

