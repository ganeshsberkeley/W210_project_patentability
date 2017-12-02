import pickle
from jsonschema import validate
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import stop_words
import nltk
import logging

import configparser

config = configparser.ConfigParser()
config.read('config_uspto.ini')

sb_stemmer = nltk.stem.SnowballStemmer('english')
def tokenize(doc):
    return doc.lower().split(" ")


def query_first_level_cluster(query_string):
    # find first level cluster
    nmf_filename = config['DEFAULT']['nmfmodelx']
    tfidf_filename = config['DEFAULT']['tfidfmodelx']
    # load the model from disk
    loaded_nmf_model = pickle.load(open(nmf_filename, 'rb'))
    loaded_tfidf_model = pickle.load(open(tfidf_filename, 'rb'))
    query_string = query_string.lower().strip()
    query_string_pr_stem = ''
    for word in query_string.split():
        if query_string_pr_stem:
            query_string_pr_stem = query_string_pr_stem + ' ' + sb_stemmer.stem(word)
        else:
            query_string_pr_stem = sb_stemmer.stem(word)
    query_tfidf = loaded_tfidf_model.transform([query_string_pr_stem])
    nmf_query = loaded_nmf_model.transform(query_tfidf)
    # print(nmf_query)
    # nmf_query.argmax(axis=1)
    return (nmf_query.argmax(axis=1)[0])


def query_second_level_cluster(query_string, first_level_cluster):
    # find second level cluster
    nmf_filename = config['DEFAULT']['nmfmodellower'] + str(first_level_cluster) + '.sav'
    tfidf_filename = config['DEFAULT']['tfidfmodellower'] + str(first_level_cluster) + '.sav'
    # load the model from disk
    loaded_nmf_model = pickle.load(open(nmf_filename, 'rb'))
    loaded_tfidf_model = pickle.load(open(tfidf_filename, 'rb'))
    query_string = query_string.lower().strip()
    query_string_pr_stem = ''
    for word in query_string.split():
        if query_string_pr_stem:
            query_string_pr_stem = query_string_pr_stem + ' ' + sb_stemmer.stem(word)
        else:
            query_string_pr_stem = sb_stemmer.stem(word)
    query_tfidf = loaded_tfidf_model.transform([query_string_pr_stem])
    nmf_query = loaded_nmf_model.transform(query_tfidf)
    # print(nmf_query)
    # nmf_query.argmax(axis=1)
    return (nmf_query.argmax(axis=1)[0])

if __name__ == "__main__":
    # execute only if run as a script
    print("main module")