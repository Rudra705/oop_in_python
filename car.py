class Car(object):
    def __init__(self, model, color , company , speed_Limit):
        self.model = model
        self.color = color
        self.company = company
        self.speed_Limit = speed_Limit

    def start(self):
        print("Started ! ! !")
    
    def stop(self,speed):
        print("Stoped ! ! !")
        self.speed = speed
        print(speed)
    
    def accelerate(self):
        print("Done")

    def change_gear(self, gear_type):
        print("Gear Changed")

audi = Car("Top class", "silver" , "AUDI" , 80)
audi.stop(20)
