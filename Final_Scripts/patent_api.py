from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_jsonpify import jsonpify
from patent_search_script import *
from flask import json
from flask_cors import CORS, cross_origin

app = FlaskAPI(__name__)
CORS(app)

@app.route('/patentsearch',methods=['GET'])
def patentsearch():
    if request.method == 'GET':
        query_string = str(request.args.get('query_string'))
        cosine_sim_threshold = float(request.args.get('cosine_sim_threshold'))
        top = int(request.args.get('top'))
        
        results, first_cluster, second_cluster = query_wrapper(query_string,cosine_sim_threshold,top)
    
        f_topics_filename = '/home/ubuntu/data/models_data/topics/topics_X.csv'
        s_topics_filename = '/home/ubuntu/data/models_data/topics/topics_' + str(second_cluster) + '.csv'
        df_f_topics = pd.read_csv(f_topics_filename,header=None,names = ['i','topics'])
        df_s_topics = pd.read_csv(s_topics_filename,header=None,names = ['i','topics'])
        
        charts_filename = '/home/ubuntu/data/models_data/chartdatafiles/chart_cluster_data_' + str(first_cluster) + '_' + str(second_cluster) + '.csv'
        chartfile = open(charts_filename, 'r') 
        i = 1
        chart_text = ''
        for line in chartfile:
            if i == 1:
                chart_text = "\"charts_data" + str(i) + "\":" + line 
            else:
                chart_text += ", " + "\"charts_data" + str(i) + "\":" + line 
            i += 1    
        
        json_str = '{'
        json_str += '\"searchresult\":'
        json_str += results.to_json(orient='records')
        json_str +=  ',' + "\"firstcluster\":" + "\"" + str(first_cluster) + "\""
        json_str +=  ',' + "\"secondcluster\":" + "\"" + str(second_cluster) + "\""
        json_str +=  ',' + "\"firstcluster_topics\":" + "\"" + str(df_f_topics.iloc[first_cluster]['topics']).rsplit(' ', 1900)[0] + "\""
        json_str +=  ',' + "\"secondcluster_topics\":" + "\"" + str(df_s_topics.iloc[second_cluster]['topics']).rsplit(' ', 1900)[0] + "\""
        json_str +=  ',' + "\"charts_data\": {" + str(chart_text) + "}"
        json_str += '}'
        return json_str
        
if __name__ == "__main__":
    app.run(host= '0.0.0.0',port=8080,debug=False) 
    #app.run(debug=True) 