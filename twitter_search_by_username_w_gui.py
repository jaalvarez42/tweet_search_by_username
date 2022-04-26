import json
import twitter_for_gui as twt
from tkinter import *
from datetime import datetime, timedelta
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Base url for searching
url = "https://api.twitter.com/2/tweets/search/recent"

# Extra specificities for query
options = " -is:retweet -is:reply"

days = 0

query = {
	'query': "",
	'start_time': "",
	'max_results': 100,
	'tweet.fields': 'public_metrics'
	}

token = twt.Token()

#Click function; assigns all text boxes to appropriate variables and submits
def click():
	token.token = tokenEntry.get()
	tweeter =  "from:" + tweeterEntry.get()
	days = int(daysEntry.get())
	hours = days*24

	# Making the timeframe for the query
	date_time = str((datetime.now() + timedelta(hours=5) - timedelta(hours=hours))).split()
	date = date_time[0]
	time = date_time[1][0:8]
	search_date = date + "T" + time + "Z"

	query['query'] = tweeter + options
	query['start_time'] = search_date

	output.delete(0.0, END)

	message = ("Success! If the graph does not appear, check your files. "
		"If it is incorrect or not in your files, make sure "
		"the data you entered is correct.")

	if (days < 1 or days > 7):
		message = "Please use a number from 1 to 7 for days."
		output.insert(END, message)
	if (days >= 1 and days <= 7):
		json_response = twt.connect_to_endpoint(url, query, token.token)

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

		print(f"Tweets made in the last {days} day(s): {json_response['meta']['result_count']}")

		output.insert(END, message)

#Function to close the window
def close_window():
	window.destroy()
	exit()

window = Tk()
window.title("Tweet Search By Username")
window.configure(background="lightblue")

Label(window, text="Authorization key:", bg="lightblue", fg="white",
	font="none 15 bold") .grid(row=1, column=0, sticky=W)

tokenEntry = Entry(window, width=20, bg="white")
tokenEntry.grid(row=2, column=0, sticky=W)

# Getting the username from the user
Label (window, text="Whose tweets would you like to search for?(@)", bg="lightblue",
	fg="white", font="none 15 bold") .grid(row=3, column=0, sticky=W)

tweeterEntry = Entry(window, width=20, bg="white")
tweeterEntry.grid(row=4, column=0, sticky=W)

# Getting the timeframe for the search
Label (window, text="How many days back would you like to begin the search? 1-7",
	bg="lightblue", fg="white", font="none 15 bold") .grid(row=5, column=0, sticky=W)

daysEntry = Entry(window, width=5, bg="white")
daysEntry.grid(row=6, column=0, sticky=W)

Button (window, text="SUBMIT", width=0, command=click) .grid(row=7, column=0,
	sticky=W)

output = Text(window, width=75, height=6, wrap=WORD, bg="white")
output.grid(row=8, column=0, columnspan=2, sticky=W)

window.mainloop()