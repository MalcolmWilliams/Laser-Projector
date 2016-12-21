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
#
# This programs proides the interface between the openlase and the main function.

"""
OpenLase is an open source library and toolkit for controlling laser scanners. It has an emphasis on real-time operation and integration with audio, and it uses the JACK Audio Connection Kit as a backend.

Features include:

- Classic OpenGL-like API
- Support for ILDA format sprites
- SVG to ILDA converter
- Built-in vector font
- Realtime bitmap tracer (edge detection)
- Python bindings
- Video player (using the bitmap tracer)
- Output processor GUI with perspective correction (projecting from an angle) and level controls.

More information can be found at: https://marcan.st/projects/openlase/ or https://github.com/marcan/openlase
"""

__docformat__ = 'restructuredtext'



import sys
sys.path.append('./openlase/build/python')
sys.path.append('./openlase/build/libol')
import pylase as ol
from math import pi
import time as t
import logging

class Openlase_Driver:
    """
    This class is a driver to provide an easier way to access the openlase functions
    """
    
    def __init__(self):
        """
        Initializes an instance of the driver
        """
        ol.init()
        self.font = ol.getDefaultFont()
        open('performance.log', 'w').close()
        logging.basicConfig(filename='performance.log', level=logging.DEBUG)
        #filehandler = logging.FileHandler('performance.log', mode='w') 
        #logger.addHandler(filehandler)

    def test_params(self, tweet_segments, time_display, justification='c'):
        """
        Runs several tests with different parameters to determine how to get the highest fps. 

        **Args:**
            | *tweet_segments:* String that contains the message (tweet) This is a list that is already divided for each line.
            | *time_display:* How long the message will be displayed. The function will exit when the time runs out
            | *justification:* Whether to be left ('l'), right ('r') or center('c') justified. Useful when multiple lasers present.

        **Returns:**
            *None*

        **Note:**
            Calls the write function. All the input arguments are simply passed to the write function.
        """
        
        '''
        int rate;
        float on_speed;
        float off_speed;
        int start_wait;
        int start_dwell;
        int curve_dwell;
        int corner_dwell;
        int end_dwell;
        int end_wait;
        float curve_angle;
        float flatness;
        float snap;
        int render_flags;
        int min_length;
        int max_framelen;
        '''
 
        #self.update_params()
        
        #logging.info("\ton_speed\t" + str(params.on_speed))
        #logging.info("\toff_speed\t" + str(params.off_speed))
        #params = ol.RenderParams()
        self.write_tweet(tweet_segments, time_display, justification = justification)

    def get_deviation_arr(self, num,dev):        
        return [num-num*(dev/100.0), num, num+num*(dev/100.0)]
        #return [10,20,30]




    def update_params(self):
        #this is temporary so I can demo


        params = ol.RenderParams()
        
        #testing effects of different parameters:
        deviation = 70 #deviation for min/max in terms of percentage.
        on_speed_arr = self.get_deviation_arr(params.on_speed, 200)
        off_speed_arr = self.get_deviation_arr(params.off_speed, 200)
        start_wait_arr = self.get_deviation_arr(params.start_wait, 50)#50
        start_dwell_arr = self.get_deviation_arr(params.start_dwell, 50)#50
        curve_dwell_arr = self.get_deviation_arr(params.curve_dwell, deviation)
        corner_dwell_arr = self.get_deviation_arr(params.corner_dwell, deviation)
        end_dwell_arr = self.get_deviation_arr(params.end_dwell, 50)
        end_wait_arr = self.get_deviation_arr(params.end_wait, 50)#70
        #max_framelen_arr = self.get_deviation_arr(params.max_framelen,deviation)


        print on_speed_arr
        print off_speed_arr

        #for i in range(3):
        #for j in range(3):
        '''params.on_speed  = on_speed_arr[i]
        params.off_speed = off_speed_arr[i] 
        params.start_wait = start_wait_arr[i]
        params.start_dwell = start_dwell_arr[i]
        params.curve_dwell = curve_dwell_arr[i]
        params.corner_dwell = corner_dwell_arr[i]
        params.end_dwell = end_dwell_arr[i]
        params.end_wait = end_wait_arr[i]'''
        params.on_speed  = on_speed_arr[2]
        params.off_speed = off_speed_arr[2] 
        params.start_wait = start_wait_arr[0]
        params.start_dwell = start_dwell_arr[0]
        params.curve_dwell = curve_dwell_arr[0]
        params.corner_dwell = corner_dwell_arr[0]
        params.end_dwell = end_dwell_arr[0]
        params.end_wait = end_wait_arr[0]
        #params.max_framelen = max_framelen_arr[i]

        #params.render_flags=ol.RENDER_NOREVERSE default settingis the best
        ol.setRenderParams(params)


    def write_tweet(self, tweet_segments, time_display, justification='c'):
        """
        Displays a 140 character max message with lasers

        **Args:**
            | *tweet_segments:* String that contains the message (tweet) This is a list that is already divided for each line.
            | *time_display:* How long the message will be displayed. The function will exit when the time runs out
            | *justification:* Whether to be left ('l'), right ('r') or center('c') justified. Useful when multiple lasers present.

        **Returns:**
            *None*

        **Note:**
            Calls openlase functions that will send the data through JACK to the laser galvos and the simulator
        """
        
        '''
        params = ol.RenderParams()
        params.render_flags = ol.RENDER_NOREORDER | ol.RENDER_GRAYSCALE
        params.on_speed = 2/120.0
        params.off_speed = 2/30.0
        params.flatness = 0.1
        ol.setRenderParams(params)
        '''
        
        self.update_params()
        
        time = 0
        frames = 0
        print_output = True

        t_end = t.time() + time_display
        while(t.time() < t_end):

            if (justification == 't'):
                line_height = 0.9
                height_change = -0.2
            elif(justification == 'b'):
                line_height = -0.9+0.2*len(tweet_segments)
                height_change = -0.2


            #Maybe can be moved to init?
            ol.loadIdentity3()
            ol.loadIdentity()


            for line in tweet_segments:
                line = line.lstrip()
                w = ol.getStringWidth(self.font, 0.2, line)
                horiz_start = -w/2
                ol.drawString(self.font, (horiz_start, line_height), 0.2, ol.C_WHITE, line)
                line_height += height_change

            #not entirely sure what the perspective and translation does. 
            ol.perspective(60, 1, 1, 100)
            ol.translate3((0, 0, -3))

            ftime = ol.renderFrame(60)
            frames += 1
            time += ftime
            if (print_output):
                print "Frame time: %f, FPS:%f"%(ftime, frames/time)
                print_output = False
                logging.info( "\tFPS:\t\t" + str(frames/time) )

    def shutdown(self):
        ol.shutdown()

if(__name__ == "__main__"):
    od = Openlase_Driver()
    while(True):
        od.write_tweet(["this is a test tweet, I am checking"], 10)# how the segmentatation code will work. The character limit of 140 is kinda big.")
    #for line in lw.segment_message("this is a test tweet, I am checking how the segmentatation code will work. The character limit of 140 is kinda big."):
    #    print line.lstrip()
