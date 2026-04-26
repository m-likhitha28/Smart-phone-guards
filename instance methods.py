class car:
    def __init__(self,brand,speed):
       self.brand=brand
       self.speed=speed
    def start(self):
        print(self.brand," has been started")
    def accelerate(self):
        self.speed+=10
        print(self.speed, "is the maximum speed of the car")
    def dispaly(self):
        print("Brand",self.brand)
        print("Speed",self.speed)
c1=car("Toyota",180)
c1.start()
c1.accelerate()
c1.display()