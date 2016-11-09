#This program selects a tweet from the list that retrieve_tweet constantly updates. 
#in the future there can be some type of algorithm to select the "hottest" one to display (reddit style)
#for now it is placeholder and chooses the latest tweet

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json
import types

class Select_Tweet:

    def __init__(self, mention_account='@malcolm_test', tweets_filename='./output.txt'):
        self.mention_account = mention_account
        self.tweets_filename = tweets_filename
        self.tweets_file = open(tweets_filename, "r")

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
        for line in self.tweets_file:
            tweet = json.loads(line.strip())
            if 'text' in tweet:
                #print type(tweet['id'])
                #print type(target_id)
                if tweet['id'] == target_id:
                    return tweet        #return a copy of the tweet when we find it. 
        return None #something went wrong (corrupt file, couldnt find id etc)

    def get_tweet_text(self, tweet):   
        try:
            return tweet['text'].replace(self.mention_account,"",1).lstrip()    #strip out the first occurence of the mention, and any lesding whitespace. TODO: dont hardcode the mention. 
        except:
            return "could not find tweet"

    def self_test(self):
        print self.get_tweet_text(self.get_tweet_by_id(796082699215613952))

if(__name__ == "__main__"):
    mention_account = '@malcolm_test'
    tweets_filename = './output.txt'

    st = Select_Tweet()

    print st.get_tweet_text(st.get_tweet_by_id(796082699215613952))
