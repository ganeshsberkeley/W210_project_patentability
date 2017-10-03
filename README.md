# W210_project_patentability

The project folder for capstone

### Google doc 
https://docs.google.com/presentation/d/1tVJt7rY5WC3kwxC0yHxXtODOS29Wa9rqwgr2L-T8J6k/edit#slide=id.g254836169a_0_0

### Presentation 
https://docs.google.com/presentation/d/1pDtlcFDyNQNFO7TWPlKi3L3Zot2Pmj1OsFoe_aVRNro/edit?ts=59d27c4d#slide=id.p

### Slack 
https://ucbischool.slack.com

### Next checkpoint 
10/3      w5       workshop 1: teams and project management - patent


Steps to push and pull from GITHUB for EC2
-------------------------------------------
In order to clone the repo do the following In the user account (or create a directory which you created for the project), type the command

git clone https://github.com/ganeshsberkeley/W210_project_patentability

git pull

Also edit the .git/config to change the following line to

url = ssh://git@github.com/ganeshsberkeley/W210_project_patentability

Generate ssh keys
------------------

ssh-keygen -t rsa -C ganeshsberkeley@github.com

ssh-copy-id ganeshsberkeley@github.com

Copy the keys to the github (logon on to git hub, select the repo, click on settings, click on deploy keys, and add the keys there)

cat ~/.ssh/id_rsa.pub
