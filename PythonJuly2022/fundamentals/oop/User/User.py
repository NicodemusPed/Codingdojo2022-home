class User:
    def __init__(self):
        self.first_name = "nico"
        self.last_name="Ped"
        self.age="50"

user_nico=User()
user_Ped=User()
print(user_nico.first_name)
print(user_nico.last_name)
print('===========================')

class Shoe:
    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True

def on_sale_by_percent(self, percent_off):
    self.price = self.price * (1-percent_off)

skater_shoe=Shoe("Brooks", "Walkers", 149.99)
dress_shoe=Shoe("St. Jphns Bay", "Dress SlLip On", 89.99 )
print(skater_shoe.type)
print(dress_shoe.type)
skater_shoe.type = "Low-top Trainers"
print(skater_shoe.type)
dress_shoe.type = "Ballet Flats"
print(dress_shoe.type)

skater_shoe=skater_shoe.price *(1-0.5)
dress_shoe=dress_shoe.price*(1-0.1)
skater_shoe=skater_shoe.price*(1-0.1)
print(skater_shoe.price)




