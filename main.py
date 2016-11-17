"""
This is the main function that controls the flow of all the other processes. 

This module defines the following class:
- `Laser_Writer` contains the functions to control writing flow

How To Use This Module
======================

1. Activate venv: ``source venv/bin/activate``
2. Start support services: ``./start_ol_services.hs``
3. Run it: ``python main.py``
"""

__docformat__ = 'restructuredtext'

from twitter_functions import Select_Tweet
from twitter_functions import Retrieve_Tweets
from openlase import Openlase_Driver
import threading        #threadign for the tweet retrieval to run concurrently.
import time

class Laser_Writer:
    
    """
    A laser writer that uses laser galvonometers (TODO: link to wikipedia) to write tweets on distant objects

    Several modules aid the functionality:
    - `Select_Tweet` (TODO: link to Select_Tweet) Selects a tweet from a pool of available tweets based on certain characteristics
    - `Retrieve_Tweets` (TODO: link to Retrieve_Tweets) using twitter's API retrieve tweets aimed at the desired source, perform black listing and store the tweet data in a text file
    - `Openlase_Driver` (TODO: link to Openlase_Driver) provide an abstraction layer on the openlase library. The tweet text is sent here and is then formatted and sent to the laser
    """

    def __init__(self):
        """
        Initilise a Laser_Writer object
        """


        #init the needed functions. 
        
        #Properties of the search
        mention_account = '@BarackObama'
        retrieval_count = 20
        black_list = "" #tweets containing these words will be filtered out, add them in this format "-shit -piss -fuck -cunt -cocksucker -motherfucker"
        filter_ = "filter:safe"
        lang_= 'en'
        tweets_filename='twitter_functions/output.txt'

       
        self.od = Openlase_Driver.Openlase_Driver()#this is what you send the tweets to

        self.rt = Retrieve_Tweets.Retrieve_Tweets(black_list, tweets_filename=tweets_filename, mention_account=mention_account)
        
        #select tweet should be called after, in case the output.txt file does not exist. 
        self.st = Select_Tweet.Select_Tweet(tweets_filename=tweets_filename)
        #st.self_test()

    def write_tweet(self, time_display=10):
        tweet = self.st.get_random_tweet_text()
        tweet = tweet.encode('ascii', 'ignore') #openlase library can only take ascii data
        print "Output: " + str(tweet)
        #tweet = self.st.get_tweet_text(self.st.get_tweet_by_id(796082699215613952)) 
        #tweet = self.st.self_test()
        #write a tweet using the lasers!!!. this takes in a string of text.
        t = threading.Thread(target = self.od.write_tweet(tweet, time_display))
        #t = daemon = True
        t.start()
        #note: there needs to be a way to kill this and start it again nicely. 

    def write_message(self, message="this is the default message", time_display=10):
        message = message.encode('ascii', 'ignore') #openlase library can only take ascii data
        print "Output: " + str(message)
        t = threading.Thread(target=self.od.write_tweet(message, time_display))
        t.start()

    def start_tweet_retrieval(self):
        t = threading.Thread(target = self.rt.get_tweets)    #start the tweet retrieval process as a thread.
        t.daemon = True         #make the thread a daemon so it is properly killed on Keyboard Interrupt
        t.start()
        

    def demo(self):
        #this function demos the functionality of the program. 
        #there are 2 parts
        #1. it selects and displays a random tweet
        #2. user can enter their own messages and have them displayed.
        #
        # use: run the program and it will start displaying random tweets. hit ctrl-c and it will give keyboard prompts
        try:
            while(True):
                print("====================================================")
                print "Selecting a new random tweet"
                self.write_tweet(5)
        
        except KeyboardInterrupt:
            pass
        try:
            while(True):
                #get the users message:
                print("====================================================")
                message = raw_input("Enter the desired message: ") 
                self.write_message(message, 5)
        except KeyboardInterrupt:
            pass        


if(__name__ == "__main__"):
    lw = Laser_Writer()
    lw.start_tweet_retrieval()

    #sleep the program for 1 second so the tweets can be retrieved.
    time.sleep(1)

    lw.demo()

    #raw_input()
