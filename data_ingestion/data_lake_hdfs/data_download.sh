#! /bin/bash


if [ ! -d "data_sets" ] 
then
	mkdir data_sets
else
	rm -rf data_sets
	mkdir data_sets
fi

echo "Downloading file from the USPTO Website :::"

cd data_sets
echo $pwd
wget https://bulkdata.uspto.gov/data/patent/pair/economics/2014/csv.zip
wget https://bulkdata.uspto.gov/data/patent/claims/economics/2014/patent_claims_fulltext.csv.zip
unzip csv.zip
unzip patent_claims_fulltext.csv.zip
mkdir 2014
mv *csv 2014/
rm *csv
wget https://bulkdata.uspto.gov/data/patent/pair/economics/2015/csv.zip
unzip csv.zip
mkdir 2015
mv *csv 2015/
rm *csv

cd ../
echo $pwd


echo "# getting rid of header ..."
tail -n +2 data_sets/2014/foreign_priority.csv > data_sets/2014/foreign_priority.csv
tail -n +2 data_sets/2015/foreign_priority.csv > data_sets/2015/foreign_priority.csv
tail -n +2 data_sets/2015/application_data.csv > data_sets/2015/application_data.csv
tail -n +2 data_sets/2015/application_data.csv > data_sets/2015/application_data.csv
tail -n +2 data_sets/2015/application_data.csv > data_sets/2015/application_data.csv
tail -n +2 data_sets/2015/application_data.csv > data_sets/2015/application_data.csv
tail -n +2 data_sets/2014/transactions.csv > data_sets/2014/transactions.csv
tail -n +2 data_sets/2015/transactions.csv > data_sets/2015/transactions.csv
tail -n +2 data_sets/2014/event_codes.csv > data_sets/2014/event_codes.csv
tail -n +2 data_sets/2015/event_codes.csv > data_sets/2015/event_codes.csv
tail -n +2 data_sets/2014/status_codes.csv > data_sets/2014/status_codes.csv
tail -n +2 data_sets/2015/status_codes.csv > data_sets/2015/status_codes.csv
tail -n +2 data_sets/2014/patent_claims_fulltext.csv > data_sets/2014/patent_claims_fulltext.csv


echo "# creating /user/root/w210/ folder in HDFS ..."
hdfs dfs -rm -r -f /user/root/w210

hdfs dfs -mkdir /user/root/w210
hdfs dfs -mkdir /user/root/w210/foreign_priority
hdfs dfs -mkdir /user/root/w210/application_data
hdfs dfs -mkdir /user/root/w210/transactions
hdfs dfs -mkdir /user/root/w210/event_codes
hdfs dfs -mkdir /user/root/w210/status_codes
hdfs dfs -mkdir /user/root/w210/full_text

hdfs dfs -mkdir /user/root/w210/foreign_priority/2014
hdfs dfs -mkdir /user/root/w210/application_data/2014
hdfs dfs -mkdir /user/root/w210/transactions/2014
hdfs dfs -mkdir /user/root/w210/event_codes/2014
hdfs dfs -mkdir /user/root/w210/status_codes/2014
hdfs dfs -mkdir /user/root/w210/full_text/2014


hdfs dfs -mkdir /user/root/w210/foreign_priority/2015
hdfs dfs -mkdir /user/root/w210/application_data/2015
hdfs dfs -mkdir /user/root/w210/transactions/2015
hdfs dfs -mkdir /user/root/w210/event_codes/2015
hdfs dfs -mkdir /user/root/w210/status_codes/2015
hdfs dfs -mkdir /user/root/w210/full_text/2015

echo "#Putting Files in Data Lake"
hdfs dfs -put data_sets/2015/foreign_priority.csv /user/root/w210/foreign_priority/2015/foreign_priority.csv
hdfs dfs -put data_sets/2015/application_data.csv /user/root/w210/application_data/2015/application_data.csv
hdfs dfs -put data_sets/2015/transactions.csv /user/root/w210/transactions/2015/transactions.csv
hdfs dfs -put data_sets/2015/event_codes.csv /user/root/w210/event_codes/2015/event_codes.csv
hdfs dfs -put data_sets/2015/status_codes.csv /user/root/w210/status_codes/2015/status_codes.csv

hdfs dfs -put data_sets/2014/foreign_priority.csv /user/root/w210/foreign_priority/2014/foreign_priority.csv
hdfs dfs -put data_sets/2014/application_data.csv /user/root/w210/application_data/2014/application_data.csv
hdfs dfs -put data_sets/2014/transactions.csv /user/root/w210/transactions/2014/transactions.csv
hdfs dfs -put data_sets/2014/event_codes.csv /user/root/w210/event_codes/2014/event_codes.csv
hdfs dfs -put data_sets/2014/status_codes.csv /user/root/w210/status_codes/2014/status_codes.csv

hdfs dfs -put data_sets/2014/patent_claims_fulltext.csv /user/root/w210/full_text/2014/patent_claims_fulltext.csv
