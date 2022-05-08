from classes import *

c = CoffeeMaker()
menu = Menu()

while True:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if choice == 'espresso':
        cup = menu.find_drink(choice)
        print(f'You ordered a {cup.name}')
    elif choice == 'cappuccino':
        cup = menu.find_drink(choice)
        print(f'You ordered a {cup.name}')
    elif choice == 'latte':
        cup = menu.find_drink(choice)
        print(f'You ordered a {cup.name}')
    elif choice == 'report':
        c.report()
    elif choice == 'off':
        break
