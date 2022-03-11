import json
import twitter as twt
from datetime import datetime, timedelta
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Base url for searching
url = "https://api.twitter.com/2/tweets/search/recent"

# Getting the username from the user
tweeter = "from:" + input("Whose tweets would you like to search for?\n@")

# Extra specificities for query
options = " -is:retweet -is:reply"

# Getting the timeframe for the search
days = int(input("How many days back would you like to begin the search? 1-7\n"))

# In case they try something outside of 1-7
if days > 7 or days < 1:
	while days > 7 or days < 1:
		days = int(input("Please pick a number from 1 to 7\n"))
hours = days*24

# Making the timeframe for the query
date_time = str((datetime.now() + timedelta(hours=5) - timedelta(hours=hours))).split()
date = date_time[0]
time = date_time[1][0:8]
search_date = date + "T" + time + "Z"

query = {
	'query': tweeter + options,
	'start_time': search_date,
	'max_results': 100,
	'tweet.fields': 'public_metrics'
}

json_response = twt.connect_to_endpoint(url, query)
#print(json.dumps(json_response, indent=4, sort_keys=True))
print(f"Tweets made in the last {days} day(s): {json_response['meta']['result_count']}")

ids = []
likes = []
tweet_text = []

for num in range(json_response['meta']['result_count']):
    ids.append(json_response['data'][num]['id'])
    likes.append(json_response['data'][num]['public_metrics']['like_count'])
    tweet_text.append(json_response['data'][num]['text'])

x_values = ids[:]
data = [Bar(x=x_values, y=likes)]

x_axis_config = {'title': 'Tweet IDs'}
y_axis_config = {'title': 'Total Likes'}
my_layout = Layout(title=f'Total Likes Per Tweets By @{tweeter[5:]}',
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='tweets.html')