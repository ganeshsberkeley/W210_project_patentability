echo "Getting the Bulk Data"
wget -r -l1 -A.zip https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/2014/

echo "Moving the zip file"
mv  bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/2014/*.zip .
rm -rf bulkdata*

echo "Unzipping the files"
unzip '*.zip'
rm -rf *.zip

rm -rf scrape xml-split
mkdir scrape xml-split

echo "Running the splitter"
python split.py

echo "Extracting the Data"
python process_full.py

rm -rf *.xml

cd scrape
tail -n+2 ipg140617_xml.csv > 2014_full_txt.csv
hdfs dfs -put 2014_full_txt.csv /user/root/w210/full_text/2014/2014_full_txt.csv


