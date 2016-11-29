from openlase import Openlase_Driver


if(__name__ == "__main__"):
    od = Openlase_Driver.Openlase_Driver()#this is what you send the tweets to
    while(True):
        od.write_tweet("test_2", 100)
