class car:
    wheels = 4 #class variable

    def __init__(self):
        self.mil =10  #instance variable
        self.com ='bmw'# instance variable
    
c1 = car()
c2 = car()
c2.mil = 8
print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)

car.wheels =6
print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)
