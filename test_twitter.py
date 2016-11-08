# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import time

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '795764215411838977-ykebbXz7Hp0Uoe2LdkAirMg9a3gNUik'
ACCESS_SECRET = 'FSPQaCJwrRQ5Syhqbrh1CHgzQhA61bMyUuG04nVdEJJ1o'
CONSUMER_KEY = 'OIMH5a8Ode8Ys8jKhkcAoNBXz'
CONSUMER_SECRET = 'Y3fO2qI8OlONsknlrbkdbMZQKDxDvlb77jJjmOJwS5IW4kkzHR'

#Properties of the initial search
mention_account = '@malcolm_test'
retrieval_count = 20
black_list = "" #tweets containing these words will be filtered out, add them in this format "-shit -piss -fuck -cunt -cocksucker -motherfucker"
filter_ = "filter:safe"
lang_= 'en'



#query = mention_account + ' ' + black_list
query = mention_account + ' ' + black_list + ' ' + filter_

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter = Twitter(auth=oauth)

tweets = twitter.search.tweets(q=query, count=retrieval_count)
#tweets = json.dumps(tweets)
#print tweets

#strip out the metadata
tweets = tweets['statuses']
#print len(tweets)
#to make sure the file is properly closed, even if an exception is raised
with open('output.txt', 'w') as output_file:
    latest_id = 0
    for tweet in tweets:
        output_file.write( json.dumps(tweet) )
        output_file.write('\n')
        output_file.flush()     #make sure the buffer is clear
        id_ = tweet['id']
        if(id_ > latest_id): latest_id = id_
        print latest_id

    #keep refreshing and looking for new tweets to add to file. 
    while(True):
        time.sleep(10)  #sleeps for 10 seconds
        tweets = twitter.search.tweets(q=query,since_id=latest_id, count=retrieval_count)
        tweets = tweets['statuses']
        if len(tweets) != 0:    #if there were any new tweets retrieved
            #print tweets
            for tweet in tweets:
                output_file.write(json.dumps(tweet))
                output_file.write('\n')
                output_file.flush()     #make sure the buffer is clear. 
                id_ = tweet['id']
                if(id_ > latest_id): latest_id = id_
                print latest_id

