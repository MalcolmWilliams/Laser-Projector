"""
Twitter offers a comprehensive set of REST APIs to provide programmatic access to read and write Twitter data. More information is avaiable at the following `link <https://dev.twitter.com/rest/public>`_

| Several other sources were used to write the Retrive_Tweet module:
| - Tutorial: http://socialmedia-class.org/twittertutorial.html
| - Python Library: https://pypi.python.org/pypi/twitter
| - Search API query docs: https://dev.twitter.com/rest/public/search
"""

__docformat__='restructuredtext'

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import time


class Retrieve_Tweets:
    """
    https://dev.twitter.com/rest/public
    """


    def __init__(self, black_list, mention_account='@malcolm_test', retrieval_count='20', filter_='filter:safe', lang='en', tweets_filename='output.txt'):
        """
        Initializes an instance of the retrieve tweets module

        **Args:**
            | *black_list:* string containg inappropriate words that should be filtered out, add them in this format ```-shit -piss -fuck -cunt -cocksucker -motherfucker```
            | *mention_account:* The account that the tweets are directed to
            | *retrieval_count:* Maximum number of tweets that will be retrieved in a single refresh
            | *filter_:* Twitters own filtering intelligence to make sure tweets are safe
            | *lang:* Language of the tweet
            | *tweets_filename:* Storage location for retrieved tweets
        
        **Returns:**
            | *None*

        **Note:**
            | Also takes care of the authorization
        """
        # Variables that contains the user credentials to access Twitter API 
        ACCESS_TOKEN = '795764215411838977-ykebbXz7Hp0Uoe2LdkAirMg9a3gNUik'
        ACCESS_SECRET = 'FSPQaCJwrRQ5Syhqbrh1CHgzQhA61bMyUuG04nVdEJJ1o'
        CONSUMER_KEY = 'OIMH5a8Ode8Ys8jKhkcAoNBXz'
        CONSUMER_SECRET = 'Y3fO2qI8OlONsknlrbkdbMZQKDxDvlb77jJjmOJwS5IW4kkzHR'

        self.mention_account = mention_account
        self.retrieval_count = retrieval_count
        self.black_list = black_list
        self.filter_ = filter_
        self.lang = lang

        self.tweets_filename = tweets_filename
        f = open(self.tweets_filename, 'w')     #create the file in case is does not exist. this is to be a little more robust with select_tweet.py
        f.close()
    
        #query = mention_account + ' ' + black_list
        self.query = mention_account + ' ' + black_list + ' ' + filter_

        oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

        self.twitter = Twitter(auth=oauth)

    def get_tweets(self):
        """
        Store any tweets that match the search parameters

        **Args:**
            | *None*
        
        **Returns:**
            | *None*

        **Note:**
            | - Stores discovered tweets in file determined by ``tweets_filename``
            | - Prints out tweet id whenever a new tweet is found
            | - Successive searches will only look for tweets that have come in since the last search
        """
        tweets = self.twitter.search.tweets(q=self.query, count=self.retrieval_count)
        #tweets = json.dumps(tweets)
        #print tweets

        #strip out the metadata
        tweets = tweets['statuses']
        #print len(tweets)
        #to make sure the file is properly closed, even if an exception is raised
        with open(self.tweets_filename, 'w') as output_file:
            latest_id = 0
            for tweet in tweets:
                output_file.write( json.dumps(tweet) )
                output_file.write('\n')
                output_file.flush()     #make sure the buffer is clear
                id_ = tweet['id']
                if(id_ > latest_id): latest_id = id_
                #print "Added tweet: " + str(id_)

            #keep refreshing and looking for new tweets to add to file. 
            while(True):
                time.sleep(10)  #sleeps for 10 seconds
                tweets = self.twitter.search.tweets(q=self.query,since_id=latest_id, count=self.retrieval_count)
                tweets = tweets['statuses']
                if len(tweets) != 0:    #if there were any new tweets retrieved
                    #print tweets
                    for tweet in tweets:
                        output_file.write(json.dumps(tweet))
                        output_file.write('\n')
                        output_file.flush()     #make sure the buffer is clear. 
                        id_ = tweet['id']
                        if(id_ > latest_id): latest_id = id_
                        #print "Added tweet: " + str(id_)


if(__name__ == "__main__"):

    #Properties of the search
    mention_account = '@BarackObama'
    retrieval_count = 20
    black_list = "" #tweets containing these words will be filtered out, add them in this format "-shit -piss -fuck -cunt -cocksucker -motherfucker"
    filter_ = "filter:safe"
    lang_= 'en'

    rt = Retrieve_Tweets(mention_account=mention_account, black_list='')
    rt.get_tweets()
