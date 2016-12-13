#Don't judge me based on this code. 

import argparse
from openlase import Openlase_Driver

#it pains me to make this funciton. 
#This function takes in the argparse argument and converts it to a list,
#this sucks so much
def format_list(message):
    message[0] = message[0].replace('[', '', 1)
    idx = len(message)-1
    message[idx] = message[idx][:len(message[idx])-1]
    for i in range(0,idx+1):
        message[i] = message[i].lstrip()
    #edge case for when commas get left behind
    if(len(message)>1):
        for i in range(len(message)-1): #happens of first until second last lines
            message[i] = rreplace(message[i])
    
    return message

def rreplace(s, old=',', new='', occurrence=1):
    li = s.rsplit(old, occurrence)
    return new.join(li)

parser = argparse.ArgumentParser(description='This is a shitty work-around')
parser.add_argument('--message', nargs='+')
parser.add_argument('--time_display', action="store", type=float)
parser.add_argument('--justification', action="store", type=str)

results = parser.parse_args()

#print results.message


message = format_list(results.message)
time_display = results.time_display
justification = results.justification

od = Openlase_Driver.Openlase_Driver()
#use the test_params when tuning the parameters to find the fastest acceptable setting
od.test_params(results.message, results.time_display, justification=justification)
#od.write_tweet(results.message, results.time_display, justification=justification)

print message
print time_display
print justification
