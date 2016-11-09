#This is the main funciton that starts all the other processes.

from twitter_functions import Select_Tweet
from twitter_functions import Retrieve_Tweets
import threading        #threadign for the tweet retrieval to run concurrently.

class Laser_Writer:

    def __init__(self):
        #init the needed functions. 
        
        #Properties of the search
        mention_account = '@malcolm_test'
        retrieval_count = 20
        black_list = "" #tweets containing these words will be filtered out, add them in this format "-shit -piss -fuck -cunt -cocksucker -motherfucker"
        filter_ = "filter:safe"
        lang_= 'en'
        tweets_filename='twitter_functions/output.txt'

        self.rt = Retrieve_Tweets.Retrieve_Tweets(black_list, tweets_filename=tweets_filename)
        
        #select tweet should be called after, in case the output.txt file does not exist. 
        self.st = Select_Tweet.Select_Tweet(tweets_filename=tweets_filename)
        #st.self_test()

    def start_tweet_retrieval(self):
        t = threading.Thread(target = self.rt.get_tweets)    #start the tweet retrieval process as a thread.
        t.daemon = True         #make the thread a daemon so it is properly killed on Keyboard Interrupt
        t.start()


if(__name__ == "__main__"):
    lw = Laser_Writer()
    lw.start_tweet_retrieval()

    raw_input()
