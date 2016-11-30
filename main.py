"""
This is the main function that controls the flow of all the other processes. 

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
from openlase import Laser_Format
import threading        #threadign for the tweet retrieval to run concurrently.
import time
from subprocess import call
import os

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
        mention_account = '@malcolm_test'
        retrieval_count = 20
        black_list = "" #tweets containing these words will be filtered out, add them in this format "-shit -piss -fuck -cunt -cocksucker -motherfucker"
        filter_ = "filter:safe"
        lang_= 'en'
        tweets_filename='twitter_functions/output.txt'

       
        self.num_lasers = 2
        self.laser_speeds = [20000, 40000]      #note these also need to be properly configured in jack!

        self.lf = Laser_Format.Laser_Format(self.laser_speeds)

        '''
        self.od = []
        for i in range(self.num_lasers):
            self.od.append(Openlase_Driver.Openlase_Driver())
            self.od[i].write_tweet("Initializing",1)  #seems to be necessary to write to the driver before creating a new one.

        #self.od_0 = Openlase_Driver.Openlase_Driver() 
        #self.od_1 = Openlase_Driver.Openlase_Driver()
        #self.od = [Openlase_Driver.Openlase_Driver() for i in range(self.num_lasers)] #this is what you send the tweets to. one driver per laser.
        #print self.od
        '''

        self.rt = Retrieve_Tweets.Retrieve_Tweets(black_list, tweets_filename=tweets_filename, mention_account=mention_account)
        
        #select tweet should be called after, in case the output.txt file does not exist. 
        self.st = Select_Tweet.Select_Tweet(tweets_filename=tweets_filename)
        #st.self_test()



    def write_tweet(self, tweet="This is the default tweet", time_display=10):
        """
        Will send a tweet to the laser to be written

        **Args:**
            | *tweet:* A 140 character max string to be sent to the laser
            | *time_display:* How long the tweet will be displayed. When the time runs out the thread will terminate and the function will exit.

        **Returns:**
            None
        
        **Note:**
            Will print out the message to be displayed.
        """
        
        tweet = self.lf.format(tweet)

        print "Output: " + str(tweet)
    
        #tweet = self.st.get_tweet_text(self.st.get_tweet_by_id(796082699215613952)) 
        #tweet = self.st.self_test()
        #write a tweet using the lasers!!!. this takes in a string of text.
        
        #t = threading.Thread(target = self.od[0].write_tweet(tweet[0][0], time_display))
        #t.start()
        
        
        #This is a reaaaallllly shitty work-around. You cannot simply run two instances of the openlase driver class, it needs to be two seperate files. 
        #Every time you write to the driver, open a new instance, write to first, small delay, write to second, etc. Once the drivers are done running they will destroy themselves.
        cmd_start = "nohup python ol_driver_instance.py "
        cmd_end = " > /dev/null 2>&1 &"

        

        for i in range(len(tweet)):     #one per laser.
            #t[i] = threading.Thread(target = self.od[i].write_tweet(tweet[i][0] time_display))
            #t.daemon = True
            #t[i].start()
            
            #call([cmd_start, str(tweet[i][0]), str(time_display), cmd_end])
            cmd = cmd_start + str(tweet[i][0]) + " " + str(time_display) + cmd_end
            print cmd
            os.system(cmd)
            time.sleep(0.01)
        time.sleep(time_display + 0.5)        
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
        There are two sections to the demo: 
        
        1. Select and display a random tweet
        2. Directly enter a message into the command prompt

        The function will start by randomly showing tweets. Hit ``ctrl-c`` to switch to keyboard promt. Hit ``crtl-c`` again to exit
        """
        '''
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
                self.write_tweet(message, 0.1)
        except KeyboardInterrupt:
            pass 
        '''
        test_string = "1234567890 "
        for i in range(14):
            temp = test_string*(i+1)
            self.write_tweet(temp, 1)

if(__name__ == "__main__"):
    lw = Laser_Writer()
    lw.start_tweet_retrieval()

    #sleep the program for 1 second so the tweets can be retrieved.
    time.sleep(1)

    lw.demo()

    #raw_input()
