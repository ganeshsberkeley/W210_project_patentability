#!/bin/bash

sudo yum update
cd ~
wget https://d3kbcqa49mib13.cloudfront.net/spark-2.2.0-bin-hadoop2.7.tgz

# Unpack Spark in the /opt directory
sudo tar zxvf spark-2.2.0-bin-hadoop2.7.tgz -C /opt

# Create a symbolic link to make it easier to access
sudo ln -fs spark-2.2.0-bin-hadoop2.7 /opt/spark

#write spark_home
echo "export SPARK_HOME=/opt/spark" >> ~/.bash_profile
echo "PATH=$PATH:$SPARK_HOME/bin" >> ~/.bash_profile
echo "export PATH" >> ~/.bash_profile

source ~/.bash_profile

spark-submit --version

echo "********Now install JAVA and JAVA_HOME**************"
sudo apt-get update
sudo apt-get install default-jre
sudo apt-get install default-jdk
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
sudo update-alternatives --config java
sudo update-alternatives --config command
sudo update-alternatives --config java

echo 'JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java"' >> /etc/environment
source /etc/environment
