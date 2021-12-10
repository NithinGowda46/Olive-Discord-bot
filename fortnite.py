import webbrowser
import json
import requests

def fn():
  r = requests.get('https://www.freetogame.com/api/games')
  data = r.json()
  k = data[47]['game_url']
  return k