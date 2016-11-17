"""
This is the main function that controls the flow of all the other processes. 

This module defines the following class:
- `Laser_Writer` contains the functions to control data flow

How To Use This Module
----------------------

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
    This class calls all the necessary helper modules.
    Concurrently running modules are handled with pythons threading library
    """

    def __init__(self):
        """
        Initilise a Laser_Writer object
        """
        
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

    def write_tweet(self, tweet="This is the default tweet", time_display=10):
        """
        Will send a tweet to the laser to be written

        **Args:**
            *tweet:* A 140 character max string to be sent to the laser
            *time_display:* How long the tweet will be displayed. When the time runs out the thread will terminate and the function will exit.

        **Returns:**
            None
        
        **Note:**
            Will print out the message to be displayed.
        """
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

    def start_tweet_retrieval(self):
        """
        Continuously check for new tweets with the matching criteria
        
        **Args:**
            *None*
        **Returns:**
            *None*  

        """
        t = threading.Thread(target = self.rt.get_tweets)    #start the tweet retrieval process as a thread.
        t.daemon = True         #make the thread a daemon so it is properly killed on Keyboard Interrupt
        t.start()
        

    def demo(self):
        """
        | Demos two ways the program can be used. 
        | 1. Select and display a random tweet
        | 2. Directly enter a message into the command prompt

        The function will start by randomly showing tweets. Hit ```ctrl-c``` to switch to keyboard promt. Hit ```crtl-c``` again to exit
        """
        try:
            while(True):
                print("====================================================")
                print "Selecting a new random tweet"
                self.write_tweet(self.st.get_random_tweet_text(), 5)
        
        except KeyboardInterrupt:
            pass
        try:
            while(True):
                #get the users message:
                print("====================================================")
                message = raw_input("Enter the desired message: ") 
                self.write_tweet(message, 5)
        except KeyboardInterrupt:
            pass        


if(__name__ == "__main__"):
    lw = Laser_Writer()
    lw.start_tweet_retrieval()

    #sleep the program for 1 second so the tweets can be retrieved.
    time.sleep(1)

    lw.demo()

    #raw_input()
