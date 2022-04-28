# Tweet Search By Username
## Description
This is a very small program that allows you to make a bar graph of the most recent tweets, not including retweets or replies, made by a specific user. In order to use this you will need an authorization token to use the twitter api.

## Languages/Tools Used
- Python
- Tkinter
- Plotly
- Twitter's API

## Possible Improvements
- ~~Make an interface so it isn't all done on the command line.~~
- Allow the user to choose what types of tweets to pull (tweets, quote tweets, retweets, replies) and what metric to look at (likes or retweets).
- Improve readability of the graph (alter the colors, include a gradient).
- Allow users to see the tweets the graph is made up of.

## How to Use (No GUI)
1. Open the command line.
2. Start up the virtual environment and set your authentication/bearer token.
3. Start the program which will then prompt you for the twitter handle and length of time for the search.
4. The graph may not open automatically in which it should be in the same directory as the program.

## How to Use (With GUI)
1. Run the program twitter_search_by_username_w_gui.py which should open the GUI for the program.
2. Fill out the text boxes with appropriate information.
3. Click the submit button.

## The Files
### twitter.py
This is what was already present from Twitter to handle token authorization and the get request. You can set your bearer/authorization token here if you would rather not set it every time you want to run the program.

### twitter_search_by_username.py
The code in here should be pretty straightforward. If other options are desired, the options variable can altered to fit what you are searching for. If you would like to see what can be used to modify the query, there is a table [here](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query) at the bottom. The furthest this search goes back is 7 days, so that is why the input is restricted from 1 to 7 days. You can open it to less than a day by modifying the if statement. The query wants the time in a specific way so datetime is used to change the users input into what the query needs. There is a print statement that is commented out in case you would like to see what else you can get from the search. There is also a print statement stating how many tweets were pulled to compare to how many bars there are on the graph(they should be the same). The very last part is setting up the bar graph. You can change the bar graph and if you are wondering how you can check Plotly's [Python API reference](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Bar.html) or use [Plotly Express](https://plotly.com/python/bar-charts/).

### twitter_search_by_username_w_gui.py
This has most of the same code as the non-gui version, everything is just rearranged to make use of tkinters tools. Most of the code pertaining to the look of the GUI is near the bottom.

### twitter_for_gui.py
Because the non-gui version made use of the command line to set the authorization token, I had to make a couple of tweaks to account for the change. The main change was creating a class to hold the token value so that I can use it in both files. 
