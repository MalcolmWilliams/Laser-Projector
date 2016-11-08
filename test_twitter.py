# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '795764215411838977-ykebbXz7Hp0Uoe2LdkAirMg9a3gNUik'
ACCESS_SECRET = 'FSPQaCJwrRQ5Syhqbrh1CHgzQhA61bMyUuG04nVdEJJ1o'
CONSUMER_KEY = 'OIMH5a8Ode8Ys8jKhkcAoNBXz'
CONSUMER_SECRET = 'Y3fO2qI8OlONsknlrbkdbMZQKDxDvlb77jJjmOJwS5IW4kkzHR'

#name of the account to gather mentions from
mention_account = '@malcolm_test'


oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter = Twitter(auth=oauth)

tweets = twitter.search.tweets(q=mention_account)
#tweets = json.dumps(tweets)
#print tweets

#strip out the metadata
tweets = tweets['statuses']

for tweet in tweets:
    print json.dumps(tweet)
    #print tweet
    #print '\n\n\n'
    #print len(tweet)
    #for t in tweet:
    #    print t
    continue

