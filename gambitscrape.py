
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
resp = requests.get('https://api.gambitprofit.com/gambit-plays/tokens/xxxx?_sort=createdAt:DESC&_limit=50')
json_resp = json.loads(resp.content)
multipliers = []

for play in json_resp:
    #output_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    #print(output_date)
    d = dateutil.parser.parse(play['PlayDate'])
    # print(d)
    # print(type(d))
    #print(datetime.datetime.today() - timedelta(days=1))
    #print(())
    # print(''.join(play['PlayDate']).split('T'))
    # today = utc.localize(d)
    # oneDay = utc.localize(past)
    # print(today)
    # print(oneDay)      ida-332_-____
    # print('d is ', type(d))  
    # print('date time is ' , type(past) )
    # if (today < oneDay ) :
    print(play['Team1']['Name'], play['Team1']['Reward'],      play['Team2']['Name'], play['Team2']['Reward'])
    multipliers.append({
        play['Team1']['Name']: play['Team1']['Reward'],
        play['Team2']['Name']: play['Team2']['Reward']
        })
# print(multipliers)
json_object = json.loads(resp.content)

json_formatted_str = json.dumps(json_object, indent=2)

# print(json_formatted_str)
# for i in multipliers:
#     print(i)


# import requests
# import json



# r = requests.get('https://api.gambitprofit.com/gambit-plays/tokens/xxxx?_sort=createdAt:DESC&_limit=100')


# print(r.url)
# print(json.dumps(r))





# res = jsonify(resp)
# print(resp)
# json_resp = json.dumps(res)
# print(json_resp)
# multipliers = []
# data = json.dumps(json_resp) 
# print(data)
# print(data)
# for play in data:
#     print(play)







