from flask import Flask,render_template, request
from flask_cors import CORS, cross_origin
import json
import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from chatbot_engine.model.utils.bot import get_result
# api
@app.get('/')
def index():
  return render_template('chatbot.html')

@app.post('/')
def chatbot(): 
  sentence = request.form["sentence"]
  result = get_result(sentence)
  return json.dumps(result, ensure_ascii=False).encode("utf8")
   
if __name__ == '__main__':
  app.run(debug=True)