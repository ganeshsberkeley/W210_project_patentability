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

Process to check in files
-------------------------

Do the following

git status

to see what are the files that need to be pushed
git add

for all the files that needs to be checked in
git commit -m "Message"

git push -u origin master


EC2 Steps
-----------

The data used for the project is quite large.  So create a volume of atleast 10224 GB in EBS and attach to the instance.

Python Installation
--------------------
python --version

sudo yum install python27-devel -y

python --version

mv /usr/bin/python /usr/bin/python266

ln -s /usr/bin/python2.7 /usr/bin/python

/usr/bin/python --version

python --version

