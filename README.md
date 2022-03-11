# tweet_search_by_username
This allows you to make a bar graph of the most recent tweets, not including retweets or replies, made by a specific user.

# Table of Contents
I made this project to get some introductory practice on using APIs and Plotly.

This is my first time making something like this so there is a lot of room for improvements with the program. For example, the bar graph can be made more readable. The color of the bars and the background can be changed, and a gradient could even be implemented to try to quickly show the general difference in amount of likes each tweet got. The text contained in the tweet can even be made to appear when hovering over the bar. A step beyond that could be having the entire tweet appear, but since this is a program that just generates a bar graph, I am not sure how the tweets would be embedded. Also, if the tweets were embedded, the next step would be allowing users to interact with those tweets, such as replying, liking, or retweeting. A minor thing to note is also that this program assumes the user is in EST, so a change could be made to adjust for other time zones.

Starting with twitter.py, this is what was already present from Twitter to handle authorization and the get request. To make sure this works I have to set a variable named BEARER_TOKEN with my authorization token before starting the program.

In the other file, I made sure to import what I would need to create the graph and the code that twitter supplied. I also import datetime and timedelta in order to allow the user to add time restrictions for the tweets.

I start by setting the url the request will use, and then building the query that will be used by asking for the parameters from the user. I set each part of the parameter to a variable as I go to make it easier for me to build the query dictionary and to remember where each variable will go in the query. The program will not work if the search range is past 7 days and I just picked 1 day as the minimum time length for the search so I make sure to have the user pick a number in that range. With how the request wanted the timeframe for the search set up, I decided to use datetime, split it up, and then put it back together how Twitter wanted it. The reason I add 5 hours is because the request works in UTC. This program assumes the user is in EST so it changes the time from EST to UTC.

Once I have the info I need, I put it all together in the query dictionary and make the request. From there it prints the number of tweets made and then begins storing the info needed for the bar graph. I then make the configurations for the axes and title, and then generate the bar graph.
