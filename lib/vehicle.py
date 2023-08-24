class Vehicle:
    
    def __init__(self,wheel_size,wheel_number):
        self.wheel_size=wheel_size
        self.wheel_number=wheel_number

    def go(self):
        print("vrrrrrrrooom!")
        return "vrrrrrrrooom!" 

    def fill_up_tank(self):
        print ("filling up!")
        return "filling up!"

bmw=Vehicle(5,12)
bmw.go()
bmw.fill_up_tank()
toyota=Vehicle(7,14)
toyota.go()
toyota.fill_up_tank()     
