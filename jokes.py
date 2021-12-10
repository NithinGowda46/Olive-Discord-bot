import requests
import json

def get_jokes():
  jokes = requests.get('https://geek-jokes.sameerkumar.website/api?format=json')
  json_data = json.loads(jokes.text)
  joke = json_data['joke']
  return joke