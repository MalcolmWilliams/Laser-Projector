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
        mention_account = '@malcolm_test'#'@BarackObama'
        retrieval_count = 20
        black_list = "" #tweets containing these words will be filtered out, add them in this format "-shit -piss -fuck -cunt -cocksucker -motherfucker"
        filter_ = "filter:safe"
        lang_= 'en'
        tweets_filename='twitter_functions/output.txt'

       
        self.num_lasers = 2
        self.laser_speeds = [20000, 40000]      #note these also need to be properly configured in jack!

        self.lf = Laser_Format.Laser_Format(self.laser_speeds)

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
        
        print "Output: " + tweet
        tweet = self.lf.format(tweet)
        #only uncomment next line if you are testing the performance.
        tweet = [ ["1234567890 1234567890","1234567890 1234567890",], [] ]
    
        
        #This is a reaaaallllly shitty work-around. You cannot simply run two instances of the openlase driver class, it needs to be two seperate files. 
        #Every time you write to the driver, open a new instance, write to first, small delay, write to second, etc. Once the drivers are done running they will destroy themselves.
        #hide the output
        cmd_start = "nohup python driver_instance.py --message "
        cmd_end = " > /dev/null 2>&1 &"
        #display output
        cmd_start = "python driver_instance.py --message "
        cmd_end = " &"
        
        #for i in range(len(tweet)):     #one per laser.
        for i in range(1):     #for testing speed on a single laser.

            if(i == 0): justification = 'r'
            elif(i == len(tweet)-1): justification = 'l'
            else: justification = 'c' #this should be changed to full justification and not centered. will never be used. 
            
            cmd = cmd_start + str(tweet[i]) + " --time_display  " + str(time_display) + " --justification " + justification + cmd_end
            #print cmd
            os.system(cmd)
            time.sleep(0.05)#if they are run to close to each other they sometimes mess up
            
        time.sleep(time_display + 0.5)



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
                self.write_tweet(message, 5)
        except KeyboardInterrupt:
            pass 
        '''
        
        #This is a quick testing function that will print up to 140 characters (max length of a tweet)
        #can be used to evaluate performance of the lasers

        test_string = "1234567890 "
        for i in range(13,14):
            temp = test_string*(i+1)
            self.write_tweet(temp, 3)
        

if(__name__ == "__main__"):
    lw = Laser_Writer()
    lw.start_tweet_retrieval()

    #sleep the program for 1 second so the tweets can be retrieved.
    time.sleep(1)

    lw.demo()

    #raw_input()
