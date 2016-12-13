
"""
| Select a tweet from the pool of potential tweets based on a predetermined algorithm.
| The pool of tweets are stored in ``output.txt`` in JSON format

| Currently the most advanced selection method is ``select_random_tweet_id()``
| Future implementations will include more intelligent tweet selections based on a number of factors, such as:
| - Location
| - Time
| - Subjet Matter
| - Number of favorites/retweets
| - Hashtags
"""

__docformat__='restructuredtext'


# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json
import types
import random
import logging

class Select_Tweet:
    """
    Select a tweet from the pool of potential candidates
    """


    def __init__(self, mention_account='@malcolm_test', tweets_filename='./output.txt'):
        """
        Initialize an instance of the tweet selection module

        **Args:**
            | *mention_account:* The account that the tweets are directed to
            | *tweets_filename:* Where to find the pool of potential tweets

        **Return:**
            | *None*
        """
        self.mention_account = mention_account
        self.tweets_filename = tweets_filename
        self.tweets_file = open(tweets_filename, "r")

            
        self.tweets = []
        self.refresh_tweets()

        logging.basicConfig(filename="temp.log", level=logging.DEBUG)


    def print_file(self):
        """
        Prints the entire pool of tweets in human readable format

        **Args:**
            | *None*
        **Returns:**
            | *None*
        **Note:**
            | Will print out to terminal
        """
        for line in self.tweets_file:
            try:
                #print line
                # Read in one line of the file, convert it into a json object 
                tweet = json.loads(line.strip())
                if 'text' in tweet: # only messages contains 'text' field is a tweet
                    print tweet['id'] # This is the tweet's id
                    print tweet['created_at'] # when the tweet posted
                    print tweet['text'] # content of the tweet

                    print tweet['user']['id'] # id of the user who posted the tweet
                    print tweet['user']['name'] # name of the user, e.g. "Wei Xu"
                    print tweet['user']['screen_name'] # name of the user account, e.g. "cocoweixu"

                    hashtags = []
                    for hashtag in tweet['entities']['hashtags']:
                        hashtags.append(hashtag['text'])
                    print hashtags

            except:
                # read in a line is not in JSON format (sometimes error occured)
                continue

    def get_tweet_by_id(self, target_id):
        """
        Select a tweet given a specific ID
        
        **Args:**
            | *target_id:* ID of the target tweet

        **Returns:**
            | JSON tweet object, or None
        """
        for tweet in self.tweets:
            if 'text' in tweet:
                if tweet['id'] == target_id:
                    return tweet        #return a copy of the tweet when we find it. 
        return None #something went wrong (corrupt file, couldnt find id etc)

    def select_random_tweet(self):
        """
        Select a tweet random tweet from the pool
        
        **Args:**
            | *None*

        **Returns:**
            | JSON tweet object
        """
        try:
            while(True):
                rand_int = random.randint(0, len(self.tweets)-1)
                tweet = self.tweets[rand_int]
                logging.info(str(tweet['text']))
                logging.info(len(str(tweet['text'])))
                if(len(str(tweet['text'])) < 80):       #reject tweets if there are toomany charaacters.
                    print "Random tweet selected: " + str(tweet['id'])
                    break
        except (ValueError):
            tweet = "No tweets in pool"
            print tweet
        return tweet

    def get_tweet_text(self, tweet):   
        """
        retrieve text from JSON tweet object
        
        **Args:**
            | *tweet:* JSON tweet object

        **Returns:**
            | tweet string or error message
        
        **Note:**
            | Also does some formatting
        """
        try:
            return tweet['text'].replace(self.mention_account,"",1).lstrip()    #strip out the first occurence of the mention, and any leading whitespace. 
        except:
            return "could not find tweet"
        
    def get_random_tweet_text(self):
        """
        Simplifies process of getting random tweet text
        
        **Args:**
            | *None*

        **Returns:**
            | tweet string or error message

        **Note:**
            | Also refreshes pool
        """
        self.refresh_tweets()
        return self.get_tweet_text(self.select_random_tweet())  
    
    def refresh_tweets(self):
        """
        Parses the output.txt file and builds an internal pool of tweet data
        
        **Args:**
            | *None*

        **Returns:**
            | None

        **Note:**
            | Used for initial pool building and refreshing
        """
        tweets = []
        self.tweets_file.seek(0)    #refresh all the tweets in the pool. in the future if there are too many tweets, only refresh the new ones.
        for line in self.tweets_file:
            try:
                tweets.append(json.loads(line.strip()))
                #print "tweet appended successfully"
            except:
                #print "could not append"
                continue
        self.tweets = tweets
        print "There are " + str(len(self.tweets)) + " tweets in the pool"

    def self_test(self):
        """
        Easily test functionality. Grabs 1 specific tweet.
        
        **Args:**
            | *None*

        **Returns:**
            | Tweet string or error message

        **Note:**
            | Also refreshes pool
        """
        self.refresh_tweets()
        return self.get_tweet_text(self.get_tweet_by_id(795766807424626693))#   795795239092908032))#796082699215613952))

if(__name__ == "__main__"):
    mention_account = '@malcolm_test'
    tweets_filename = './output.txt'

    st = Select_Tweet()
    #print st.self_test()
    print st.get_random_tweet_text()
