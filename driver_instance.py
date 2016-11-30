from openlase import Openlase_Driver

class driver_instance(object):

    def __init__(self):
        self.od = Openlase_Driver.Openlase_Driver()#this is what you send the tweets to
        while(True)     #hold the thread open

    def write(self, message, time_display):
        self.od.write_tweet(message, time_display)


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
    di_0 = driver_instance()
    di_0.write()

    
    di_1 = driver_instance()
    di_1.write()

    
    di_0.write()
