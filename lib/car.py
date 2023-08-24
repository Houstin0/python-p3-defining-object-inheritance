from vehicle import Vehicle

class Car(Vehicle):
    
    def go(self):
        print("VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!")
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

mazda=Car(12,34)
mazda.go()    