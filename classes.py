# Classes

class Vehicle :
    def __init__(self, make , model):
        self.make = make
        self.model = model
        self
        
    def moves(self) :
        print("Move along..")

    def get_make_model(self) :
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle("Tesla", "Model Y")

my_car.moves()
print(my_car.make)
print(my_car.model)
my_car.get_make_model()

your_car = Vehicle("Tata" , "Punch")
your_car.get_make_model()
your_car.moves()

print("\n\n")

# Inheritance

class Airplane(Vehicle) :
    def __init__(self, make , model , faa_id):
        super().__init__(make,model)
        self.faa_id = faa_id

    def moves(self) :
        print("Files along..")
    
class Truck(Vehicle) :
    def moves(self):
        print("Rumbles along..")

class GolfCart(Vehicle) :
    pass


karthik = Airplane("Karthik" , "XY", "hg-123")
kumar = Truck("Kumar" , "XY")
golf_play = GolfCart("Golf" , "TT")

karthik.get_make_model()
karthik.moves()
kumar.get_make_model()
kumar.moves()
golf_play.get_make_model()
golf_play.moves()

print(" ")


for v in (my_car,your_car,karthik,kumar,golf_play) :
    v.get_make_model()
    v.moves()