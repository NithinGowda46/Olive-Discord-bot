import json
import requests
def dict_api(word):
  word_id = word 
  url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'+ word_id
  r = requests.get(url)
  data = r.json()
  k = data[0]['meanings']
  k = k[0]['definitions']
  k = k[0]['definition']
  return k
  
  