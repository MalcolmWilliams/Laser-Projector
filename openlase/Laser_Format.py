"""
Contains all the functions to format a raw text string into something that can be output by the laser writer. 

**Input:** String
**Output:** Double nested list of strings (one for each laser, one for each line). 

Formatting that will be done:
-----------------------------
1. convert to 128bit ascii.
2. remove hyperlinks, metions
3. wordwrapping (split words if needed)
4. split into one section per laser
"""

__docformat__ = 'restructuredtext'
import sys
sys.path.append('./openlase/build/python')
import pylase as ol
from itertools import cycle

class Laser_Format:
    """
    Handles the formatting and segmentation
    """



    def __init__(self, laser_speeds):
        """
        Initializes a Laser_Format object
        
        **Args:**
            | *laser_speeds:* List contating the speeds of each laser galvo pair (in pps). The number of characters that can be displayed is derived from this.

        **Return:**
            | *None*
        """
        
        self.num_lasers = len(laser_speeds)
        char_to_pps = 666 # you need 666 pps to make 1 character. 
        self.laser_chars = [pps / char_to_pps for pps in laser_speeds] # convert the laser speeds into number of characters they are capable of.

 
    def format(self, message):
        """
        This is the public funciton that exterior functions will call. 

        **Args:**
            | *message:* The unformatted string
        
        **Return:**
            | *formatted_message:* The formatted and segmented string, stored in a double nested list. 
        """
        #message = "List contating the speeds of each laser galvo pair (in pps). The number of characters that can be displayed is derived from this."  #test string
        message = message.encode('ascii', 'ignore') #openlase library can only take ascii data
        message = self.segment_message(message)      #this divides the tweet into lines that are the right lenght for the laser. 

        #now the message needs to be divided even further so it is ready for each laser.

        #if the lasers are arranged horizontally, alternate. 
        #i = cycle(range(self.num_lasers))
        #if they are vertical, half go to first laser, half to second.
        count = 0
        i = 0

        formatted_message = [[],[]]
        for line in message:
            #formatted_message[i.next()].append(line)
            formatted_message[i].append(line)
            count += 1
            if ( (count + 1) > len(message)/2):
                i = 1            


        #print formatted_message
        return formatted_message
    
    def segment_message(self, tweet_string):
        """
        Format the tweet so it will be properly output by the laser writer

        **Args:** 
            *tweet_string:* string containing the message with no formatting

        **Returns:** 
            list of strings that are cut to appropriate lengths
        """
        
        self.font = ol.getDefaultFont()#this shouldnt be here!

        tweet_segments = []
        tweet_words = tweet_string.split()      #break the message up into words. 
        #delete any entry that is a hyperling (contains https://)
        tweet_words = [word for word in tweet_words if "https://" not in word]
    

        #print tweet_words
        #not sure what the actual screen width is, use this as a placeholder.
        screen_width = 1.9
        count = 0        

        while( ol.getStringWidth(self.font, 0.2, self.get_tweet_string(tweet_words)) > screen_width):
            count = 0
            w = 0
            while(w < screen_width):
                count += 1
                w = ol.getStringWidth(self.font, 0.2, self.get_tweet_string(tweet_words, count))
            count -= 1
            tweet_segments.append(self.get_tweet_string(tweet_words, count))
            del tweet_words[:count]
            #tweet_words = tweet_words[count:]     #this will likely need to be fixed. 
        tweet_segments.append(self.get_tweet_string(tweet_words))
        
        return tweet_segments           
        
    def get_tweet_string(self, tweet_words, count = -1):
        """
        Reformats a list of words into a string
        
        **Args:**
            | *tweet_words:* A list of strings that make up the full tweet
            | *count:* How many of the words are to be used for the string

        **Returns:**
            String reformatted like the original tweet
        """
        tweet_string = ''
        if count == -1:
            #print "count is -1"
            for word in tweet_words:
                tweet_string = tweet_string + ' ' + word
        else:
            for i in range(count):
                tweet_string = tweet_string + " " + tweet_words[i]
        #print tweet_string
        return tweet_string


if __name__ == "__main__":
    lf=Laser_Format([20000,40000])
    lf.format("test")
