from openlase import Openlase_Driver
from driver_instance import driver_instance
import threading



def write():

    di_0 = driver_instance()
    di_0.write()

    
    #di_1 = driver_instance()
    #di_1.write()

    #while(True):
    #    di_0.write()
    #    #di_1.write()

if(__name__ == "__main__"):
    '''
    od_0 = Openlase_Driver.Openlase_Driver()#this is what you send the tweets to
    #od_1 = Openlase_Driver.Openlase_Driver()#this is what you send the tweets to
    while(True):
        #od_1.write_tweet("test_1", 1)
        od_0.write_tweet("test_o", 1)
    
    od_0 = Openlase_Driver.Openlase_Driver()#this is what you send the tweets to
    od_0.write_tweet("test_o", 1)
    od_1 = Openlase_Driver.Openlase_Driver()#this is what you send the tweets to
    od_1.write_tweet("test_1", 1)


    while(True):
        od_0.write_tweet("test_o", 1)
        od_1.write_tweet("test_1", 1)
    '''
    
    t = threading.Thread(target = write)
    #t.daemon=True
    t.start()
