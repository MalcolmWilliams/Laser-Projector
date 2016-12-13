#         OpenLase - a realtime laser graphics toolkit
#
# Copyright (C) 2009-2011 Hector Martin "marcan" <hector@marcansoft.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 or version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

import pylase as ol
from math import pi


class Laser_Writer:

    def __init__(self):
        ol.init()
        self.font = ol.getDefaultFont()

    def write_tweet(self, tweet_string):
        time = 0
        frames = 0

        while(True):
            tweet_segments = self.segment_message(tweet_string)
            line_height = 0.5

            #Maybe can be moved to init?
            ol.loadIdentity3()
            ol.loadIdentity()


            for line in tweet_segments:
                line = line.lstrip()
                w = ol.getStringWidth(self.font, 0.2, line)
                ol.drawString(self.font, (-w/2, line_height), 0.2, ol.C_WHITE, line)
                line_height -= 0.2
            line_height = 0.5

            #not entirely sure what the perspective and translation does. 
            ol.perspective(60, 1, 1, 100)
            ol.translate3((0, 0, -3))

            ftime = ol.renderFrame(60)
            frames += 1
            time += ftime
            print "Frame time: %f, FPS:%f"%(ftime, frames/time)

    def segment_message(self, tweet_string):
        #returns the tweet in chunks that will fit the screen
        tweet_segments = []
        tweet_words = tweet_string.split()      #break the message up into words. 
        #print tweet_words
        #not sure what the actual screen width is, use this as a placeholder.
        screen_width = 2
        w = 0
        count = 0        

        while( ol.getStringWidth(self.font, 0.2, self.get_tweet_string(tweet_words)) > screen_width):
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

    def shutdown(self):
        ol.shutdown()

if(__name__ == "__main__"):
    lw = Laser_Writer()
    lw.write_tweet("this is a test tweet, I am checking")# how the segmentatation code will work. The character limit of 140 is kinda big.")
    #for line in lw.segment_message("this is a test tweet, I am checking how the segmentatation code will work. The character limit of 140 is kinda big."):
    #    print line.lstrip()
