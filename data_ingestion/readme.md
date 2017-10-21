## Prerequisites
### Step 1
Create EC2 instance based on AMI "UCB MIDS W205 EX2-FULL".
1. Log into https://console.aws.amazon.com/ec2/v2/home?region=us-east-1 
2. Selection region N. Virginia 
3. Go to launch instance, and search for above name in Community AMIs. 
4. Launch that instance using default settings. Be sure to save the key, for example W210.pem 
5. Update permission for example: sudo chmod 600 W210.pem 
6. Add key for example: ssh-add -K W210.pem
7. Go to instance, click connect, and copy the connect command and run it. 

### Step 2
Copy setup_ec2.sh file to EC2 instance. Don't run it yet. 
1. Update git on your local, and copy file to EC2 instance using: scp -i W210.pem -r ../Documents/GitHub/W210_project_patentability/data_ingestion/setup_ec2.sh root@ec2-54-174-208-210.compute-1.amazonaws.com:/ 
2. Log into EC2 instance, make sure you can find the file. 

### Step 3
Mount volume (at least size 200GB) on /data folder
1. Create volumn, size is at least 200G. 
2. Region has to be in the same region where you created your EC2 instance, in this case us-east-1d. You can find this by looking at your existing volumn.  
3. Attach volumn to instance by click on the volumn, then right click and attach after selecting the volumn. 
4. Select the instance you just created, attach to /dev/xvdb 
5. Reboot your EC2 instance 


```
 mkfs.ext4 /data
 mount -t ext4 /dev/xvdb /data
 ```
### Step 4
Run setup_ec2.sh as below
```
./setup_ec.sh /dev/xvdb
```
### Step 5
Go to /root folder and run below command to start hadoop.
```
./start-hadoop.sh
```
