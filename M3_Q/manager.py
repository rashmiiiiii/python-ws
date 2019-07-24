from car import Car
car_1 = Car("KA1085",5)
car_2 = Car("KA1075",6)
car_3 = Car("KA1065",4)
car_4 = Car("KA1075",3)
car_5 = Car("KA1065",5)

car_1.start()
car_2.start()
car_3.start()

car_1.change_gear()
car_2.change_gear()
car_1.change_gear()

lst = [car_1,car_2,car_3,car_4,car_5]
for Car in lst:
    Car.showInfo()
c=len(list(filter(lambda x:x.is_started and x.c_gear == 0,lst)))
print(c)
'''bmw = Car("KA013060",5)
bmw.start()
bmw.change_gear()
bmw.change_gear()
bmw.change_gear()
bmw.change_gear()
bmw.change_gear()
bmw.change_gear()
bmw.stop()'''
