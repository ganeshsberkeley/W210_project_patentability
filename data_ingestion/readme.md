## Prerequisites
### Step 1
Create EC2 instance based on AMI "UCB MIDS W205 EX2-FULL".
### Step 2
Copy setup_ec2.sh file to EC2 .

### Step 3
Mount volume (at least size 200GB) on /data folder using below command
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
