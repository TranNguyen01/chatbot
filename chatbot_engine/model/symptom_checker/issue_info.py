
import json
import requests
import sys
import os

from pathlib import Path
from googletrans import Translator

dirname = os.path.dirname(__file__)
utils_path = str(Path(__file__).parent.parent.absolute().joinpath('utils'))
sys.path.append(utils_path)

from string_util import get_quote_content, get_best_match_item_ID
from io_util import get_response_with_exception, get_success_response, get_fail_response

with open(os.path.join(dirname, 'issues.json'), encoding='utf8') as file:
  data = json.load(file)

def get_issue_info_result(sentence, intent):
  try:
    issue_info = get_issue_info(sentence, intent)
    return get_success_response(tag= intent["tag"], data= issue_info)
  except Exception as e:
    return get_fail_response(str(e))

def get_issue_info(sentence, intent):
  query_string = {"language":"en-gb"}
  headers = intent["api"]["headers"]
  url = intent["api"]["url"]
  issue_ID = get_issue_ID(sentence, data["Issues"])
  url = url.replace("ISSUE_ID", str(issue_ID))

  response = get_response_with_exception(url, headers=headers, params=query_string)
  result = response.json()
  return get_translation_result(result)

def get_issue_ID(sentence, issues):
  issue_name = get_quote_content(sentence)
  issue_ID = get_best_match_item_ID(issue_name, issues)
  if(issue_ID == None):
    raise Exception("Không xác định được vấn đề sức khỏe của bạn")
  else:
    return issue_ID

def get_translation_result(issue):
  issue_data = [issue["Name"], issue["DescriptionShort"], issue["MedicalCondition"], issue["PossibleSymptoms"], issue["TreatmentDescription"]]
  print(issue_data)
  translator = Translator()
  translations2 = translator.translate(issue["Name"], src="en", dest="vi")
  translations3 = translator.translate(issue["DescriptionShort"], src="en", dest="vi")
  translations4 = translator.translate(issue["MedicalCondition"], src="en", dest="vi")
  translations5 = translator.translate(issue["PossibleSymptoms"], src="en", dest="vi")
  translations6 = translator.translate(issue["TreatmentDescription"], src="en", dest="vi")
  

  result = {
    "name": translations2.text,
    "descriptionShort": translations3.text,
    "medicalCondition": translations4.text,
    "possibleSymptoms": translations5.text,
    "treatmentDescription": translations6.text,
  }
  return result


