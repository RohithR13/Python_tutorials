class computer:
    def __init__(self,cpu,ram):
        self.cpu =cpu
        self.ram = ram

        
    def config(self):
        print("config is  "+str(self.cpu)+ "  and "+str(self.ram))



com1 = computer('i5',16)  
com1.config()  