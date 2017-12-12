# same cleaning and stemming function used while creating the csv files from xml to be used for query
import nltk
import re
sb_stemmer = nltk.stem.SnowballStemmer('english')

def tokenize_and_stem(text):
    text_stem = ''
    for word in text.lower().split():
        if text_stem:
            text_stem =  text_stem + ' ' + sb_stemmer.stem(word)
        else:
            text_stem = sb_stemmer.stem(word)
    return text_stem


def clean_stem(string):
    stopwords = {'back', 'thru', 'eg', 'hereafter', 'too', 'part', 'which', 'will', 'be', 'thereupon', 'about', 'nevertheless', 'therein', 'through', 'we', 'among', 'in', 'then', 'former', 'via', 'below', 'whereafter', 'due', 'you', 'bill', 'forty', 'few', 'not', 'with', 'rather', 'next', 'nine', 'me', 'its', 'sometime', 'yours', 'who', 'whoever', 'down', 'some', 'such', 'thereafter', 'hasnt', 'fifteen', 'both', 'as', 'ever', 'could', 'find', 'hence', 'something', 'a', 'there', 'mostly', 'whereas', 'many', 'serious', 'can', 'indeed', 'afterwards', 'whenever', 'by', 'becomes', 'may', 'after', 'couldnt', 'seemed', 'anyhow', 'etc', 'might', 'already', 'no', 'please', 'them', 'myself', 'therefore', 'from', 'along', 'ltd', 'against', 'everywhere', 'amoungst', 'because', 'where', 'sixty', 'ie', 'although', 'sincere', 'move', 'seeming', 'or', 'wherever', 'inc', 'whatever', 'into', 'anywhere', 'around', 'nor', 'see', 'several', 'sometimes', 'for', 'interest', 'beyond', 'whether', 'detail', 'describe', 'moreover', 'nobody', 'whereupon', 're', 'without', 'an', 'ours', 'perhaps', 'only', 'five', 'towards', 'keep', 'eleven', 'one', 'other', 'any', 'otherwise', 'except', 'that', 'cannot', 'behind', 'ourselves', 'under', 'within', 'fifty', 'across', 'if', 'thus', 'per', 'wherein', 'here', 'empty', 'co', 'still', 'whole', 'how', 'off', 'to', 'yourself', 'call', 'cry', 'four', 'so', 'she', 'take', 'their', 'been', 'now', 'even', 'mill', 'what', 'another', 'namely', 'always', 'themselves', 'almost', 'six', 'formerly', 'ten', 'found', 'onto', 'yet', 'between', 'give', 'hers', 'herein', 'eight', 'above', 'anyway', 'third', 'himself', 'front', 'over', 'two', 'much', 'latter', 'itself', 'besides', 'those', 'on', 'twenty', 'up', 'us', 'amongst', 'beforehand', 'but', 'most', 'same', 'mine', 'should', 'this', 'full', 'herself', 'her', 'thick', 'con', 'everything', 'is', 'am', 'three', 'throughout', 'again', 'enough', 'your', 'once', 'hereupon', 'become', 'yourselves', 'everyone', 'before', 'i', 'whereby', 'others', 'must', 'seems', 'elsewhere', 'were', 'either', 'would', 'became', 'hundred', 'toward', 'very', 'latterly', 'top', 'often', 'beside', 'cant', 'else', 'the', 'however', 'and', 'somehow', 'him', 'noone', 'somewhere', 'our', 'nothing', 'de', 'fill', 'well', 'it', 'all', 'last', 'do', 'these', 'has', 'upon', 'every', 'side', 'system', 'put', 'thence', 'twelve', 'becoming', 'show', 'un', 'least', 'of', 'have', 'own', 'since', 'though', 'whither', 'out', 'hereby', 'meanwhile', 'none', 'while', 'whom', 'further', 'why', 'made', 'whose', 'my', 'someone', 'they', 'during', 'anyone', 'first', 'go', 'less', 'his', 'anything', 'thereby', 'amount', 'together', 'never', 'was', 'thin', 'also', 'each', 'fire', 'are', 'when', 'alone', 'had', 'until', 'done', 'more', 'at', 'than', 'nowhere', 'seem', 'whence', 'name', 'neither', 'he', 'get', 'being', 'bottom'}
    #strip and change to lower case and replace commas and semi colons with spaces
    stem = string.strip().lower().replace(';', ' ').replace(',', ' ').replace(':', ' ').replace('(',' ').replace(')',' ').replace('#', ' ').replace('.', ' ').strip()
         
    # remove words that only have numbers( second one removes special characters also)
    stem = re.sub(r'\b\d+\b', ' ',stem).strip()
    
    #remove special characters at the end of words
    stem = re.sub(r'([^\w\s]|_)+(?=\s|$)', ' ',stem).strip()
    
    #remove any words that have a number in it ( even if in the middle )
    stem = re.sub(r'\w*\d\w*', ' ',stem).strip()
    
    # remove any words with only one alphabet
    stem = re.sub(r'\b[a-zA-Z]\b', ' ',stem).strip()
    
    # remove stop words and change to lower case
    stem = ' '.join([item for item in (stem.strip().split()) if item not in stopwords])
    
    # get words greater than length 4 and less than 25
    stem = ' '.join([item for item in (re.findall('\w{4,25}', stem))])
    #re.findall('\w{4,25}', stem).join(' ').strip() 
    
     #apply stemming for all words
    stem = tokenize_and_stem(stem)
    return stem

#query for first level cluster and then second level cluster
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import stop_words
from sklearn.feature_extraction import text
import pandas as pd
from scipy import spatial
import nltk
from string import printable
sb_stemmer = nltk.stem.SnowballStemmer('english')

my_words = ['','()','(),']
my_stop_words = text.ENGLISH_STOP_WORDS.union(my_words)

def tokenize(doc):
    return doc.lower().split(" ")

def query_first_level_cluster(query_string):
    #find first level cluster
    nmf_filename = '/home/ubuntu/data/models_data/nmfmodels/nmf_model_X.sav'
    tfidf_filename = '/home/ubuntu/data/models_data/tfidfmodels/tfidf_model_X.sav'
    # load the model from disk
    loaded_nmf_model = pickle.load(open(nmf_filename, 'rb'))
    loaded_tfidf_model = pickle.load(open(tfidf_filename, 'rb'))

    query_string_pr_stem = clean_stem(query_string)

    query_tfidf = loaded_tfidf_model.transform([query_string_pr_stem])
    nmf_query = loaded_nmf_model.transform(query_tfidf)
    # print(nmf_query)
    # nmf_query.argmax(axis=1)
    return(nmf_query.argmax(axis=1)[0])

def query_second_level_cluster(query_string, first_level_cluster):
    #find second level cluster
    nmf_filename = '/home/ubuntu/data/models_data/nmfmodels/nmf_model_' + str(first_level_cluster) + '.sav'
    tfidf_filename = '/home/ubuntu/data/models_data/tfidfmodels/tfidf_model_' + str(first_level_cluster) + '.sav' 
    # load the model from disk
    loaded_nmf_model = pickle.load(open(nmf_filename, 'rb'))
    loaded_tfidf_model = pickle.load(open(tfidf_filename, 'rb'))
    
    query_string_pr_stem = clean_stem(query_string)
    
    query_tfidf = loaded_tfidf_model.transform([query_string_pr_stem])
    nmf_query = loaded_nmf_model.transform(query_tfidf)
    # print(nmf_query)
    # nmf_query.argmax(axis=1)
    return(nmf_query.argmax(axis=1)[0])

def query_similarities(query_string, first_level_cluster,second_level_cluster,cosine_sim_threshold,top):
    #find top similarities for a given cluster combo
    
    filename = '/home/ubuntu/data/models_data/smalldatafiles/small_cluster_data_' + str(first_level_cluster) + '_' + str(second_level_cluster) + '.csv'
    tfidf_model_filename = '/home/ubuntu/data/models_data/tfidfmodels/tfidf_model_' + str(first_level_cluster) + '_' + str(second_level_cluster) + '.sav'
    tfidf_filename = '/home/ubuntu/data/models_data/tfidfmodels/tfidf_' + str(first_level_cluster) + '_' + str(second_level_cluster) + '.sav'

    df_data = pd.read_csv(filename,usecols = ['appl_doc_number', 'appl_doc_number', 'invention_title','abstract','claim_text','patent_number'])
    loaded_tfidf_vectorizer = pickle.load(open(tfidf_model_filename, 'rb'))
    loaded_tfidf = pickle.load(open(tfidf_filename, 'rb'))
    
    
    query_tfidf = loaded_tfidf_vectorizer.transform([query_string])

    df_result = pd.DataFrame(columns=['cosine_similarity', 'appl_doc_number','invention_title','abstract','claim_text','patent_number'])

    # get the result and add to a new dataframe
    loc_index = 0
    patent_query = query_tfidf.toarray()[0]
    for index_corpus, patent_corpus in enumerate(loaded_tfidf.toarray()):
        #cosine_sim = cosine_similarity(patent_query, patent_corpus)
        cosine_sim = 1 - spatial.distance.cosine(patent_query, patent_corpus)
        if cosine_sim > cosine_sim_threshold:
            #res_row = df_data.iloc[index_corpus]
            df_result.loc[loc_index] = [cosine_sim,df_data.iloc[index_corpus]['appl_doc_number'],df_data.iloc[index_corpus]['invention_title'],df_data.iloc[index_corpus]['abstract'],df_data.iloc[index_corpus]['claim_text'],df_data.iloc[index_corpus]['patent_number']]
            #df_result.loc[loc_index] = [cosine_sim,res_row['appl_doc_number'],res_row['invention_title'],res_row['abstract'],res_row['claim_text'],res_row['patent_number']]
            
            loc_index += 1

    # sort the results and pick top results        
    df_result = df_result.sort_values('cosine_similarity',ascending=[False])
       
    df_result = df_result[:top]
    
    #remove any non-printable characters
    df_result['abstract'] = df_result['abstract'].apply(lambda x: re.sub(r'[^\x00-\x7f]',r'', x))
    df_result['abstract'] = df_result['abstract'].apply(lambda x: x.replace(" &#8216", '').replace(" &#8217", ''))
    df_result['claim_text'] = df_result['claim_text'].apply(lambda x: re.sub(r'[^\x00-\x7f]',r'', x))
    df_result['claim_text'] = df_result['claim_text'].apply(lambda x: x.replace("&#8216;", ' ').replace("&#8217;", ' '))
 
    return(df_result)

def query_wrapper(query_string,cosine_sim_threshold,top):
    first_cluster = query_first_level_cluster(query_string)
    second_cluster = query_second_level_cluster(query_string,first_cluster)
    df_result = query_similarities(query_string,first_cluster,second_cluster,cosine_sim_threshold,top)
    return df_result,first_cluster,second_cluster
    #return(first_cluster,second_cluster)