import random

class Product():

    def __init__(self,name,price = 10,weight = 20, flammability = .5, ID = random.randint(1000000,10000000)):
        self.name = name
        self.price = price
        self.flammability = flammability
        self.weight = weight
        self.ID = ID

    def stealability(self):
        ratio = self.price / self.weight

        if ratio < .5:
            return "Not so stealable."

        elif ratio >= .5 and ratio < 1.0:
            return "kinda stealable."

        else:
            return "Very stealable."

    def explode(self):
        combust = self.flammability / self.weight

        if combust < 10:
            print("...fizzle")
        
        elif combust > 10 and combust < 50:
            print("...boom")
        
        else:
            print("...BABOOM!!")
        

class BoxingGlove(Product):

    def __init__(self,name,price = 10,weight = 20, flammability = .5, ID = random.randint(1000000,10000000)):
         super().__init__(name,price = 10,weight = 10, flammability = .5, ID = random.randint(1000000,10000000))

    def explode(self):
        print("...it's a glove")
    
    def punch(self):

        if self.weight < 5:
            print("That tickles")
        
        elif self.weight > 5 and self.weight < 15:
            print("Hey that hurt!")

        else:
            print("OUCH")

