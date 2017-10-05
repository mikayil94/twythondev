##from twython import Twython
##
APP_KEY='yPWZw2YvawVuL0KQXPxbliv1b'
APP_SECRET='gbQO12W2tg5wIKZP7hNhqEQaDCmhmbzrZ2MT12TPcy7uKGIilo'
OAUTH_TOKEN='557947438-vTev6xeaCcPZXOAXXEwWIJRqVkshab2DTLEQH1qz'
OAUTH_TOKEN_SECRET='aAUOING0pkL4Ew79fGArvimSfsYie0sf8KpczNxak22PO'
##twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
##
##for status in twitter.search(q='"Mikayil"')["statuses"]:
##    user = status["user"]["screen_name"].encode('utf-8')
##    text = status["text"].encode('utf-8')
##    print user, ":", text
##    print

##
##from twython import *
##twitter = Twython()
### First, let's grab a user's timeline. Use the
### 'screen_name' parameter with a Twitter user name.
##user_timeline = twitter.getUserTimeline(screen_name="pythoncentral")
##
### And print the tweets for that user.
##for tweet in user_timeline:
##    print(tweet['text'])

from twython import TwythonStreamer

# appending data to a global variable is pretty poor form
# but it makes the example much simpler
tweets = [] 

class MyStreamer(TwythonStreamer):
    """our own subclass of TwythonStreamer that specifies
    how to interact with the stream"""

    def on_success(self, data):
        """what do we do when twitter sends us data?
        here data will be a Python object representing a tweet"""

        # only want to collect English-language tweets
        if data['lang'] == 'en':
            tweets.append(data) 

        # stop when we've collected enough
        if len(tweets) >= 3:
            self.disconnect()  

        for text in tweets:
            for user in tweets:
                print user["user"]["screen_name"] , ":", text["text"]

    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()

def call_twitter_streaming_api():
    stream = MyStreamer(APP_KEY, APP_SECRET,
                        OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    # starts consuming public statuses that contain the keyword 'data'
    stream.statuses.filter(track='data science')

call_twitter_streaming_api()   
