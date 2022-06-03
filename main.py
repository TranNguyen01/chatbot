# from tokenize import String
# from warnings import catch_warnings
# from flask import Flask, render_template, request
# from flask_cors import CORS, cross_origin
# import nltk
# nltk.download('punkt')
# from nltk.stem.lancaster import LancasterStemmer
# stemmer = LancasterStemmer()

# from tensorflow.keras.models import load_model
# import random
# import json
# import requests
# import re
# import numpy
# import pickle

# # feature module
# from chatbot_engine.model.drug_search.searcher import get_drug_search_result
# from chatbot_engine.model.symptom_checker.checker import get_check_result
# from chatbot_engine.model.utils.string_util import bag_of_words

# app = Flask(__name__)
# CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

# # load data and resource
# with open("./chatbot_engine/intents/intents.json",  encoding="utf8") as file:
#   data = json.load(file)
# with open("./chatbot_engine/model/data.pickle", "rb") as f:
#   words, labels = pickle.load(f)

# # model
# model = load_model('./chatbot_engine/model/chatbot_model.h5')


# @app.route('/', methods=['POST', "GET"])
# def chatbot(): 
#     if request.method =="POST":  
#       sentence = request.form["sentence"]
#       result = get_result(sentence)
#       print(result)
#       return json.dumps(result, ensure_ascii=False).encode("utf8")
#     else:
#         return render_template('chatbot.html')
       

# if __name__ == '__main__':
#     app.run()

from flask import Flask,render_template, request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from chatbot_engine.model.utils.bot import get_result
# api
@app.get('/')
def index():
  return render_template('chatbot.html')


# @app.post('/')
# def chatbot(): 
#     if request.method =="POST":  
#       sentence = request.form["sentence"]
#       result = get_result(sentence)
#       print(result)
#       return json.dumps(result, ensure_ascii=False).encode("utf8")


@app.post('/')
def chatbot(): 
  sentence = request.form["sentence"]
  result = get_result(sentence)
  print(result)
  return json.dumps(result, ensure_ascii=False).encode("utf8")
   
if __name__ == '__main__':
  app.run(debug=True)