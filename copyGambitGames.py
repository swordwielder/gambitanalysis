import requests
import json
import datetime
from datetime import timedelta
import dateutil.parser
import pytz

resp = requests.get('https://api.gambitprofit.com/gambit-plays/tokens/xxxx?_sort=createdAt:DESC&_limit=500')
json_resp = json.loads(resp.content)
multipliers = []

for play in json_resp:
    d = dateutil.parser.parse(play['PlayDate'])
    
    print(play['Team1']['Name'], play['Team1']['Reward'],      play['Team2']['Name'], play['Team2']['Reward'])
    multipliers.append({
        play['Team1']['Name']: play['Team1']['Reward'],
        play['Team2']['Name']: play['Team2']['Reward']
        })
json_object = json.loads(resp.content)

json_formatted_str = json.dumps(json_object, indent=2)