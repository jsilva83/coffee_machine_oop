from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def run_coffee_machine():
    # Create my coffee machine
    my_coffee_machine = CoffeeMaker()
    my_money_machine = MoneyMachine()
    my_coffee_menu = Menu()
    while True:
        my_money_machine.report()
        my_coffee_machine.report()
        str_user_choice: str = input(f'Chose your drink: {my_coffee_menu.get_items()}:\n').lower()
        if str_user_choice == 'off':
            break
        obj_user_choice = my_coffee_menu.find_drink(str_user_choice)
        if obj_user_choice is None:
            continue
        if my_coffee_machine.is_resource_sufficient(obj_user_choice):
            if not my_money_machine.make_payment(obj_user_choice.cost):
                continue
            my_coffee_machine.make_coffee(obj_user_choice)
        else:
            print(f'Not enough ingredients to make a {str_user_choice}.')
    return


if __name__ == '__main__':
    run_coffee_machine()
