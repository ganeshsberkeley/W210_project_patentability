from pyspark.ml.feature import  IDFModel,IDF,HashingTF, Tokenizer
import numpy as np
from numpy import linalg as LA
from pyspark.sql import SQLContext
import configparser
from pyspark.sql.functions import udf, desc
from pyspark.sql.types import StringType, ArrayType, FloatType
#load model
config = configparser.ConfigParser()
config.read('config_uspto.ini')

def load_model(sc,major,minor,model_path =config['DEFAULT']['small_model_path']  ):
    modelload = model_path + "small_cluster_data_" +str(major)+"_"+str(minor)
    model = IDFModel.load(modelload)
    return model

def load_data(sc,major,minor,data_path=config['DEFAULT']['input_data_path']):
    sqlContext = SQLContext(sc)
    filename = data_path + "small_cluster_data_" +str(major)+"_"+str(minor) +".csv"
    modeldata = sqlContext.read.csv( path = filename,header = True,inferSchema = True)
    return modeldata

def find_similar(model, candidateTfIdf, N):
    nfps = np.array(candidateTfIdf.select("features").collect()).reshape(-1)
    lanfps = LA.norm(nfps)
    udf_cosineSimilarity = udf(lambda x_vector: cosineSimilarity(x_vector, nfps), FloatType())
    #similarities = model.map(lambda v: (v.appl_doc_number, v.features.dot(nfps) / (LA.norm(v.features) * lanfps)))
    # topFive = sorted(enumerate(similarities.collect()), key=lambda (k, v): -v)[0:5]
    df_Similarity = model.withColumn("similarity", udf_cosineSimilarity("features"))
    df_Similarity_Sorted = df_Similarity.sort(desc("similarity"))
    return df_Similarity_Sorted.limit(N).select("appl_doc_number", "similarity").collect()
    #return similarities.collect()


def get_claim_text(sc,application_ids, major, minor, model_data):
    claim_text = []
    claim = {}
    #model_data = load_data(sc,major, minor, data_path)

    for ids in application_ids:
        claim[ids] = model_data.select("claim_text").filter(model_data["appl_doc_number"] == ids).collect()[
            0]
        claim_text.append(claim)
    return claim_text

def cosineSimilarity(x, y):
    xy = sum([i*j for (i,j) in zip(x,y)])
    x2 = math.sqrt(sum([i*i for i in x]))
    y2 = math.sqrt(sum([j*j for j in y]))
    if (x2*y2 == 0):
      return float(0.0)
    else:
      return float(1.0*xy/(x2*y2))
      
def get_top_N(sc,major, minor, inputtext, N=5):
    # load TF-IDF feature
    #idfmodel = IDFModel.load("file:///Users/nileshbhoyar/Documents/Docker/idfmodel")
    idfmodel = load_model(sc,major, minor)
    df = load_data(sc,major, minor)
    raw_df = df.select("appl_doc_number","claim_text")

    tokenizer = Tokenizer(inputCol="claim_text", outputCol="words")
    wordsData = tokenizer.transform(raw_df.dropna(how="any",subset="claim_text"))

    hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures")
    featurizedData = hashingTF.transform(wordsData)
    rescaledData = idfmodel.transform(featurizedData)
    model = rescaledData.select("appl_doc_number", "features")
    # prepare candidate input text
    sqlContext = SQLContext(sc)
    candidate_raw = sqlContext.createDataFrame([
        (9999999, inputtext)
    ], ["appl_doc_number", "claim_text"])
    tokenizer = Tokenizer(inputCol="claim_text", outputCol="words")
    candidate = tokenizer.transform(candidate_raw)
    hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures")
    candidateTf = hashingTF.transform(candidate)
    candidateTfIdf = idfmodel.transform(candidateTf)
    # load child models for similarity calculations.
    #model = load_model(sc,major, minor)
    # find similarities
    result = find_similar(model, candidateTfIdf, N)
    top = sorted(result, key=lambda x: -x[1])[0:N]

    return get_claim_text(sc,[int(i[0]) for i in top], major, minor,  df )

if __name__ == "__main__":
    # execute only if run as a script
    print("main module")
