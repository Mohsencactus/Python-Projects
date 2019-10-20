import os

class ESPM:
    def __init__(self,IP):
        self.root_url = "http://" + str(IP) 

    def Open(self):
    	os.system('wget -t 1 '+ str(self.root_url)+"/OPEN")

    def Close(self):
        os.system('wget -t 1 '+ str(self.root_url)+"/CLOSE")
