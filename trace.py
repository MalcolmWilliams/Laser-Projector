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
    
    approx = []
    
    for cnt in contours:
        #simplify the contours
        #epsilon = 0.005*cv2.arcLength(cnt,True)
        epsilon = 2
        approx.append(cv2.approxPolyDP(cnt,epsilon,True))
    
    #delete the image outline   #this is obselete now. 
    #contours = np.delete(contours, (0), axis=0)
    
    return approx 

def format_on(coord):
    return "s=" + str(coord[0])+ "," + str(coord[1]) + ",4095,0,0,0"

def format_off(coord):
    return "s=" + str(coord[0])+ "," + str(coord[1]) + ",0,0,0,0"

def make_output(contours, shape):
    #know the shape of the array so it can be scaled to the right output (0 to 4095)
    arr = np.array("s=0,0,0,0,0,0")

    scale = shape[0] if shape[0] > shape[1] else shape[1]
    
    scale = 2000/scale
    contours[:] = [c * scale + 1000 for c in contours]
    
    #perform appropriate size reduction
 
    #convert the contours array to a style that is appropriate for laser display. 
    for loop in contours: #this returns the individual shape. light must be on for the entire time, then off as it switches to the next shape. 
        #print loop
        #print loop[0]
        #print loop[0][0]
        arr = np.append(arr, format_off(loop[0][0]))
        for point in loop:
            arr = np.append(arr, format_on(point[0]))

    

    return arr

def init_laser():
    print "r=2000"
    print "e=1"

def draw_shape(arr):
    i=0

    for a in arr:
        '''
        i+=1
        if (i == 5):
            print a
            i = 0
        '''
        print a

def exit_laser():
    print "e=0"
    #print "f=1"

if(__name__ == "__main__"):
    #im = cv2.imread('square.png')
    im = cv2.imread('hello.jpeg')
    #im = cv2.imread('hello1.jpg')
    #im = cv2.imread('circles.jpeg')
    #im = cv2.imread('circles2.png')
    #im = cv2.imread('test.jpg')

    contours = get_contours(im)


    img = np.ones(im.shape)#how to get size of original image.
    cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
    cv2.imshow("img", img)
    #cv2.waitKey(0)

    arr = make_output(contours, im.shape)
    
    #print len(arr)
    
    
    init_laser()
    for i in range(100):
        draw_shape(arr)
    #draw_shape(arr) for i in range 100
    exit_laser()
    
    img = np.ones(im.shape)#how to get size of original image.
    cv2.drawContours(img, contours, -1, (0, 0, 255), 1)

    
    cv2.imshow ("im", im)
    #cv2.imshow("im2", im2)
    cv2.waitKey(0)
    ''''''


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

    print max_dim#       "e=0" == disable
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
