from classes import *


c = CoffeeMaker()
menu = Menu()

choice = input(f"What would you like? ({menu.get_items()}): ")

if choice == 'espresso':
    cup = menu.find_drink(choice)
    print(f'You ordered a {cup.name}')
if choice == 'report':
    c.report()