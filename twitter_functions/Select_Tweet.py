
"""
This program selects a tweet from the list that retrieve_tweet constantly updates. 
in the future there can be some type of algorithm to select the "hottest" one to display (reddit style)
for now it is placeholder and chooses the latest tweet
"""

__docformat__='restructuredtext'





# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json
import types
import random

class Select_Tweet:

    def __init__(self, mention_account='@malcolm_test', tweets_filename='./output.txt'):
        self.mention_account = mention_account
        self.tweets_filename = tweets_filename
        self.tweets_file = open(tweets_filename, "r")

            
        self.tweets = []
        self.refresh_tweets()

    def print_file(self):
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
        for tweet in self.tweets:
            if 'text' in tweet:
                #print type(tweet['id'])
                #print type(target_id)
                if tweet['id'] == target_id:
                    return tweet        #return a copy of the tweet when we find it. 
        return None #something went wrong (corrupt file, couldnt find id etc)

    def get_tweet_text(self, tweet):   
        try:
            return tweet['text'].replace(self.mention_account,"",1).lstrip()    #strip out the first occurence of the mention, and any leading whitespace. 
        except:
            return "could not find tweet"

    def self_test(self):
        self.refresh_tweets()
        return self.get_tweet_text(self.get_tweet_by_id(795766807424626693))#   795795239092908032))#796082699215613952))

    def refresh_tweets(self):
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
        #print "tweets"
        #print tweets
        #self.tweets = tweets

    def select_random_id(self):
        id_list = []
        for tweet in self.tweets:
            id_list.append(tweet['id'])
        rand_int = random.randint(0, len(id_list)-1)
        print "Random tweet selected: " + str(id_list[rand_int])
        return id_list[rand_int]
        
    def get_random_tweet_text(self):
        self.refresh_tweets()
        return self.get_tweet_text(self.get_tweet_by_id(self.select_random_id()))  

if(__name__ == "__main__"):
    mention_account = '@malcolm_test'
    tweets_filename = './output.txt'

    st = Select_Tweet()
    #print st.self_test()
    print st.get_random_tweet_text()
