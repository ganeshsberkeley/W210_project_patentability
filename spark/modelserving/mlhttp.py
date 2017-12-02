import pickle
from jsonschema import validate
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import stop_words
import nltk
import logging
import sparkrun
from base import query_first_level_cluster,query_second_level_cluster
sb_stemmer = nltk.stem.SnowballStemmer('english')
my_words = ['', '()', '(),']
my_stop_words = text.ENGLISH_STOP_WORDS.union(my_words)

logHangle = logging.getLogger(__name__)
import json
from nameko.web.handlers import http
from jsonschema import validate
schema = {"claim_text" : {

    "claim" : {"type" : "string"},
    "topN" :{"type":"number"}
}}

#config = configparser.ConfigParser()
#config.read('config_uspto.ini')

import os
import sys

#os.environ['JAVA_HOME'] = '/Library/Java/JavaVirtualMachines/jdk-9.0.1.jdk/Contents/Home'
import findspark
import pyspark
from pyspark.sql import SQLContext

if 'sc' not in globals():  # not globals().has_key('sc'):
    findspark.init()
    sc = pyspark.SparkContext(appName="myAppName")

def give_word_cloud(path,major,minor):
    filename = path+"_"+str(major)+".csv"
    df =pd.read_csv(filename,header=None ,names=["index","words"])
    return df["words"][minor]

class HttpService:
    name = "http_service"
    def __init__(self):
        self.sqlContext = SQLContext.getOrCreate(sc)

    @http('POST', '/find_top_5')
    def do_post(self, request):
        respo = {}
        try:
            validate(request, schema)

        except:
            return_msg =" Invalid JSON format"
            return json.dumps("Invalid JSON Format")

        msg = json.loads(request.get_data(as_text=True))

        query_string = str(msg['claim_text']['claim'])
        logHangle.info(query_string)
        first_cluster = query_first_level_cluster(query_string)
        second_cluster = query_second_level_cluster(query_string, first_cluster)
        respo['first_cluster'] = first_cluster
        respo['second_cluster'] = second_cluster

        #Now words cloude
        respo["word_cloud"]= give_word_cloud("/home/ubuntu/project/uspto_datasets/topics/topics",first_cluster,second_cluster)
        ##find top 5 similar claims from spark cluter calculations.
        respo['similar_claims'] = sparkrun.get_top_N(sc, first_cluster, second_cluster, query_string, N=5)
        logHangle.info(json.dumps(str(respo)))
        return json.dumps(str(respo))

    @http('GET', '/healthcheck')
    def do_check(self, request):
        return json.dumps("health is OK here")
if __name__ == "__main__":
    # execute only if run as a script


    if 'sc' not in globals():  # not globals().has_key('sc'):
        findspark.init()
        sc = pyspark.SparkContext(appName="myAppName")

    logHangle.info("main module")
