# W210_project_patentability

The project folder for capstone

### Presentation 1 Google Doc
https://docs.google.com/presentation/d/1pDtlcFDyNQNFO7TWPlKi3L3Zot2Pmj1OsFoe_aVRNro/edit?ts=59d27c4d#slide=id.p

### Presentation 2 Google Doc
https://docs.google.com/presentation/d/1tVJt7rY5WC3kwxC0yHxXtODOS29Wa9rqwgr2L-T8J6k/edit#slide=id.g254836169a_0_0

### Slack 
https://ucbischool.slack.com

### Heroku app  
https://patentfinder.herokuapp.com/

### UI balsamiq  
https://balsamiq.cloud/s1gny/ps8p2/r2278

### Scripts
1_W210_Load_XML_Data_To_S3.ipynb
This notebook has all the code for parsing patent application bulk files every week and to generate csv files for each year

The csv file structure is 
appl_doc_number,appl_country,appl_date,pub_doc_number,pub_date,number_of_days,invention_title,abstract,claim_text,claim_text_stemmed

2_W210_Create_Clusters_For_Data.ipynb
This notebook has all the code to create first level and second level clusters using NMF topic modeling

3_W210_Get_Clusters_For_A_Query.ipynb
This notebook has the code to return first and second level clusters for a query coming in from the application

4_w210_Get_Somilarities_For_A_Query
In progress by Nilesh and Ganesh

### Previous prject 
http://patentrecommender.s3-website-us-west-2.amazonaws.com/
https://www.ischool.berkeley.edu/projects/2016/patent-recommender 

### Next checkpoint 
12/12     4-8pm       Final presentation  


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

The data used for the project is quite large.  So create a volume of atleast 1024 GB in EBS and attach to the instance.
Once the EC2 volume is attached, please the following 
1.  Mount the volume when you login to EC2 
2.  Populate the data from git hub to the volume

In order to connect Jupyter to EC2 do the following
1.  Modify first line of /usr/bin/yum to be #!/usr/bin/python2.6 instead of #!/usr/bin/python
2.  wget https://bootstrap.pypa.io/ez_setup.py -O - | python
3.  easy_install pip
4.  sudo pip install keras --upgrade
5.  pip install jupyter
6.  Follow the steps documented in https://blog.keras.io/running-jupyter-notebooks-on-gpu-on-aws-a-starter-guide.html the ssl certificates and configuration of jupyter
7.  Install git bash on your computer
8.  From the directory where you have stored the EC2 keys files, start git bash 
9.  Once git bash is started a window will pop up.
10.  In the git bash window execute the command sudo ssh -i Capstone.pem -L 443:127.0.0.1:8888 root@ec2-54-147-126-214.compute-1.amazonaws.com
     where 
	Capstone.pem is the EC2 key
11.  run "jupyter notebook --allow-root"
12.  YOUR browser on your laptop (not aws), go to https://127.0.0.1
13.  Click on advanced and proceed to navigate.
14.  Enter the password

	


Python Installation
--------------------
python --version

sudo yum install python27-devel -y

python --version

mv /usr/bin/python /usr/bin/python266

ln -s /usr/bin/python2.7 /usr/bin/python

/usr/bin/python --version

python --version






