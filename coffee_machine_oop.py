from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine 


#instantiate classes and while loop counter as global variables
MENU = Menu()
COFFEE_MAKER = CoffeeMaker()
MONEY_MACHINE = MoneyMachine()
SHOW_ITEMS = MENU.get_items()
CONT = True


#initiate coffee machine loop
try:
    while CONT:
        choice  = input(f'What would you like? {SHOW_ITEMS[:-1]}:\n ~ ')
        MENU.find_drink(choice)
        # two machine maintainer options else normal user option
        if choice  == 'off':
            CONT = False
        elif choice == 'report':
            MONEY_MACHINE.report()
            COFFEE_MAKER.report()
        else:
            drink = MENU.find_drink(choice)
            if COFFEE_MAKER.is_resource_sufficient(drink) and MONEY_MACHINE.make_payment(drink.cost):
                COFFEE_MAKER.make_coffee(drink)

except KeyboardInterrupt:
    print('\nSee you later.')