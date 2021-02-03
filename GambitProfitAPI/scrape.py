
import requests
import json
import datetime
from datetime import timedelta
import dateutil.parser
import pytz

# utc=pytz.UTC
# past = datetime.datetime.today() - timedelta(days=1)


# now = datetime.datetime.now()
# # here, now.tzinfo is None, it's a naive datetime
# now = pytz.utc.localize(now)

# # the wrong way
# now = now.replace(tzinfo=pytz.utc)

# x_dt.replace(tzinfo=Eastern)
resp = requests.get('https://api.gambitprofit.com/gambit-plays?_sort=PlayDate:DESC')
gambitGames = json.loads(resp.content)
multipliers = []


for game in gambitGames:
    print(game)


