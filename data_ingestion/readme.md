## Prerequisites
### Step 1
Create EC2 instance based on AMI "UCB MIDS W205 EX2-FULL".
1. Log into https://console.aws.amazon.com/ec2/v2/home?region=us-east-1 
2. Selection region N. Virginia
3. Go to launch instance, and search for above name in Community AMIs, select m3.2xlarge for size 
4. Launch that instance using default settings, but modify for the storage part. Add volumn with size 1024G. Take a note of the device name, for example /dev/sdc
5. Be sure to save the key, for example W210.pem 
6. Update permission for the key, for example: ```sudo chmod 600 W210.pem```
7. Add the key using ssh: ```ssh-add -K W210.pem```
8. Go to instance, click connect, and copy the connect command and run it.
9. You should be logged into the EC2 instance now. 

### Step 2
Copy setup_ec2.sh file to EC2 instance. Don't run it yet. 
1. Update git on your local, and copy file to EC2 instance using: ```scp -i W210.pem -r {directory to your setup file}/setup_ec2.sh root@{your instance name}compute-1.amazonaws.com:.``` 
2. Log into EC2 instance, make sure you can find the file under root directory. 

### Step 3
Mount volume (at least size 200GB) on /data folder
Following instructions here https://devopscube.com/mount-ebs-volume-ec2-instance/ 
1. Log onto your instance, check disk: ```lsblk```
2. Find your volumn name, for example if it is xvdc, then do ```sudo file -s /dev/xvdc``` 
3. Then run: ```sudo mkfs -t ext4 /dev/xvdc```
4. Then make the data directory: ```sudo mkdir /data```
5. Mount the volumn: ```sudo mount /dev/xvdc /data/```
6. Go the mounted directory, make sure you can see it: ```cd /data``` 


### Step 4
Run setup_ec2.sh as below
1. Either pull the whole git repo on your EC2 instance, or copy the setup file using scp as mentioned in step2. 
2. Make sure you are at root directory 
3. Modify file permission for execution: ```chmod 777 setup_ec2.sh```
4. Then execute the command using this command, make sure you use the drive name on your instance: ```./setup_ec2.sh /dev/xvdc```

### Step 5
Go to /root folder and run below command to start hadoop.
1. At root directory, run: ```./start-hadoop.sh```


### Step 6 
Setup github access, since the github repo we are using is private, you need to setup SSH access

Follow instructions here to seup github so that you can access github using ssh 
https://help.github.com/articles/connecting-to-github-with-ssh/
You can use this link to add a new ssh key
https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/ 

Then follow this to setup access on EC2
http://www.fullstackjs.com/book/16/private-repo-ec2.html

At the end you should be able clone repo on your EC2 instance using 
'''git clone git@github.com:ganeshsberkeley/W210_project_patentability.git'''

