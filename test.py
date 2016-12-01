from openlase import Openlase_Driver
import threading
#this has to be able to properly destroy the openlase driver once it has written the message.

def write(message,time_display):
    
    od_0 = Openlase_Driver.Openlase_Driver()
    od_0.write_tweet(message[0],time_display)
    od_1 = Openlase_Driver.Openlase_Driver()
    od_1.write_tweet(message[1],time_display)
    od_0.shutdown()
    od_1.shutdown()
