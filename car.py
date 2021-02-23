class Car(object):
    def __init__(self,size,color,company,model,speed_limit,fuel,safety=None):
        self.size = size
        self.color = color
        self.company = company
        self.model = model
        self.speed_limit = speed_limit
        self.fuel = fuel
        self.safety = safety or {}

    def start(self):
        print("Your card is perfect.", self.model)

    def speed(self):
        print("Your car runs very fast.", self.speed_limit)

    def carLook(self):
        print("Your car looks awesome.", self.color)

    def quality(self):
        print("Your car quality is good.", self.model)

    def stop(self):
        print("Your car is safe.", self.safety)

tesla = Car(4,"red","Tesla","ModelS",30,"electricity",{"airbags: ": 5,"self-stop": True})
duster = Car(4,"grey","Renault","ModelY3",20,"petrol",{"airbags: ": 2,"self-stop": False})

print(tesla.stop())
