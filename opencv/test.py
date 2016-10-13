import numpy as np
import cv2


def get_contours(im):
    #contours finds white object from black background. 
    #invert the image. 
    im = (255-im)

    #convert to greyscale
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #delete the image outline   #this is obselete now. 
    #contours = np.delete(contours, (0), axis=0)
    
    return contours

#def make_output(contours, shape):
    #convert the contours array to a style that is appropriate for laser display. 


if(__name__ == "__main__"):
    #im = cv2.imread('square.png')
    im = cv2.imread('hello.jpeg')
    #im = cv2.imread('circles.jpeg')
    #im = cv2.imread('circles2.png')
    #im = cv2.imread('test.jpg')

    contours = get_contours(im)

    img = np.ones(im.shape)#how to get size of original image.
    cv2.drawContours(img, contours, -1, (0, 0, 255), 1)

    for c in contours:
        print c
        print "\n"


    cv2.imshow("img", img)
    cv2.imshow ("im", im)
    #cv2.imshow("im2", im2)
    cv2.waitKey(0)



'''
lasershark display format.

r=1000 # THIS MUST BE THE FIRST LINE IN THE FILE! 
# The "r=number" command sets the speed in points per second (pps) at which samples are displayed by the Lasershark. 
# The pps speed can be set to any integer between 1 and the maximum value as reported by the Lasershark (64000)
# You should not set this value to be greater than what your galvos are capable of operating at.
#       Failure to adhere to this guidance can result in galvo damage or decreased lifespan.
#
# !!!!!!!!!!!!!!!!!!!!!!!!!DO NOT ATTEMPT TO RUN THIS FILE!!!!!!!!!!!!!!!!!!!!!!!!!
# THIS FILE IS INTENDED DEMONSTRATE THE lasershark_stdin COMMAND FORMAT ONLY!
# !!!!!!!!!!!!!!!!!!!!!!!!!DO NOT ATTEMPT TO RUN THIS FILE!!!!!!!!!!!!!!!!!!!!!!!!!
#
# Comment lines start with a "#". These are ignored.
# Command lines may also have comments appended to their ends using the "#" symbol.
#
e=1
# The "e=" command sets the output enable state of the Lasershark. The output enable status must be set for any
# laser or galvo control to occur.
#       "e=1" == enable
#       "e=0" == disable
#
p=Prints a text string to the console
#
s=1,1,1,1,1,1
# The "s=" command adds a sample to the sample buffer to be written out to the Lasershark.
# A sample defines galvo positioning and laser intensity for a particular point to be displayed.
# The format is "s=X,Y,A,B,C,INTL_A"
# The ranges for these fields are X=[0-4095],Y=[0-4095],A=[0-4095],B=[0-4095],C=[0,1],INTL_A=[0,1]
# For A and B (analog laser control outputs), 0 means the output is off and 4096 means the output is at full power
#       1024 would indicate 25% output power, 2048 would indicate 50% output power, etc.
# For C (TTL laser control output) 0 means the output is off and 1 means the output is on
# For INTL_A (Interlock A) 0 means the output is off and 1 means the output is on (for ttl)
# Samples are queued until they fill a full lasershark packet and are then written out to the lasershark.
# This means that to ensure ALL samples are written out, a flush should be performed once all desired samples are
# written out.
#
f=1 # Flushes all samples. It is reccomended to stick this at the end of your output file to ensure all samples are displayed.
'''
