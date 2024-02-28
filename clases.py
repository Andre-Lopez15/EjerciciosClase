class car:
    Type = "Automovil"
    doors = 4
    
    def start(self):
        print("Car started")
        
    def quantitydors(self):
        return self.doors
newCar=car()
newCar.start()

newCar.dors = 3
newCar.start()