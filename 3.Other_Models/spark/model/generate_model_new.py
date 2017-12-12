import os
import sys
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
import findspark
import pyspark
from pyspark.sql import SQLContext
import configparser
import os
import logging
import shutil


logHangle = logging.getLogger(__name__)
config = configparser.ConfigParser()
config.read('config_uspto.ini')
#os.environ['JAVA_HOME'] = config['DEFAULT']['JAVA_HOME']
findspark.init()
sc = pyspark.SparkContext(appName="myAppName")
logHangle.info("Spark Session Generated")
sqlContext = SQLContext(sc)

#filepath =/home/ubuntu/project/uspto_datasets/smalldatafiles
#df = sqlContext.read.csv( path = config['DEFAULT']['input_data_path'],header = True,inferSchema = True)
#raw_df = df.select("appl_doc_number","claim_text")

#tokenizer = Tokenizer(inputCol="claim_text", outputCol="words")
#wordsData = tokenizer.transform(raw_df.dropna(how="any",subset="claim_text"))

#hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures")
#featurizedData = hashingTF.transform(wordsData)

#idf = IDF(inputCol="rawFeatures", outputCol="features")

#idfmodel = idf.fit(featurizedData)
#shutil.rmtree(config['DEFAULT']['tfidfmodelmain'])
#idfmodel.save(config['DEFAULT']['tfidfmodelmain'])
#logHangle.info("Master Model Saved.")
#Generate models for smaller files Now
for file in os.listdir(config['DEFAULT']['input_data_path']):
    extension = os.path.splitext(file)[1]
    if extension == ".csv":
        filename = config['DEFAULT']['input_data_path'] + file #os.path.splitext(file)[0]
        modeldata = sqlContext.read.csv( path = filename,header = True,inferSchema = True)
        raw_model = modeldata.select("appl_doc_number","claim_text")
        tokenizer = Tokenizer(inputCol="claim_text", outputCol="words")
        candidate = tokenizer.transform(raw_model.dropna(how="any",subset="claim_text"))
        hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures")
        featurizedData= hashingTF.transform(candidate)
        idf = IDF(inputCol="rawFeatures", outputCol="features")
        idfmodel = idf.fit(featurizedData)
        #candidateTfIdf = idfmodel.transform(candidateTf)
        #tfidf = idfmodel.select("appl_doc_number", "features").rdd
        modelsave = config['DEFAULT']['small_model_path'] + os.path.splitext(file)[0]
        #shutil.rmtree(modelsave)
        idfmodel.save(modelsave)
logHangle.info("Child Model saved")
