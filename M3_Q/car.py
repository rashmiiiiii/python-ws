#object oriented concepts
#in pytho every superclass is object class
#self -keyword indicating the current object
class Car:
    def __init__(self,regno,no_gears):   #def __init__() constructor 
        self.regno = regno               #instance variables
        self.no_gears = no_gears
        self.is_started = False
        self.c_gear = 0
    def start(self):
        if self.is_started:
            print(f"car with {self.regno} already started")
        else:
            print(f"car with {self.regno} started")
            self.is_started = True
    def stop(self):
        if self.is_started:
            print(f"car with regno:{self.regno} stopped")
            self.is_started = False
        else:
            print(f"car with regno:{self.regno} stopped already")
            
    def change_gear(self):
        if self.is_started:
            if self.c_gear < self.no_gears:
                self.c_gear += 1
                print(f"car with reg no:{self.regno} changed gear {self.c_gear} ")
            else:
                print(f"car with regno:{self.regno} already in top gear {self.c_gear} you can't change ")
        else:
            print(f"car with regno:{self.regno} already change the gear")
    def showInfo(self):
        print(f"the car {self.regno} is started:{self.is_started} no of gears:{self.no_gears} gear status:{self.c_gear}")

'''bmw = Car("KA013060",5)
bmw.start()
bmw.change_gear()'''
