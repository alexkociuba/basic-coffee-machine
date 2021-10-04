from drink_menu import MENU, resources


machine_on = True
# drink_choice = True
total_money_taken = 0
transaction = 0



def report():
    water = resources['water']
    print(f"water remaining: {water}ml")
    milk = resources['milk']
    print(f"milk remaining: {milk}ml")
    coffee = resources['coffee']
    print(f"coffee remaining: {coffee}g")
    print(f"total money taken: £{format(total_money_taken, '.2f')}")
    print(f"___________________________")
    print(f'end of report')
    print(f"___________________________")
    make_selection()


def make_drink(drink_choice):
    enough_ingredients = True
    drink_paid_for = False
    coffee_stock = (resources['coffee'])
    milk_stock = (resources['milk'])
    water_stock = (resources['water'])
    coffee_required = (MENU[f"{drink_choice}"]['ingredients']['coffee'])
    milk_required = (MENU[f"{drink_choice}"]['ingredients']['milk'])
    water_required = (MENU[f"{drink_choice}"]['ingredients']['water'])
    cost_of_drink = (MENU[f"{drink_choice}"]['cost'])
    global total_money_taken


    while enough_ingredients:
        if coffee_stock >= coffee_required:
            print('coffee available')
        else:
            print('not enough coffee')
            make_selection()
        if milk_stock >= milk_required:
            print('milk available')
        else:
            print('not enough milk')
            make_selection()
        if water_stock >= water_required:
            print('water available')
        else:
            print('not enough water')
            make_selection()
        print(f'price is {format(cost_of_drink, ".2f")}')



        while not drink_paid_for:
            payment = round(0, 2)
            if payment < cost_of_drink:
                print('Insert coins')
                coin1 = int(input('£1: '))
                payment += 1.00 * coin1
                coin50 = int(input('50p: '))
                payment += 0.50 * coin50
                coin20 = int(input('20p: '))
                payment += 0.20 * coin20
                coin10 = int(input('10p: '))
                payment += 0.10 * coin10

                print(f'Total inserted: £{format(payment, ".2f")}')
            if payment == cost_of_drink:
                print('thank you for inserting the correct amount')
                drink_paid_for = True
                total_money_taken += cost_of_drink
            elif payment > cost_of_drink:
                change = (payment - cost_of_drink)
                print(f"Take your change: £{format(change, '.2f')}")
                drink_paid_for = True
                total_money_taken += cost_of_drink
            elif payment < cost_of_drink:
                print(f'you need to insert {float(round(cost_of_drink - payment, 2))} more')
                print("** eject coins **")

        print('please wait for your drink')
        print('_______________________________')
        print('PLEASE TAKE YOUR DRINK, GOODBYE')
        print('_______________________________')

        # reflect new stock levels
        (resources['coffee']) = (coffee_stock - coffee_required)
        (resources['milk']) = milk_stock - coffee_required
        (resources['water']) = water_stock - water_required

        return



def make_selection():
    print(f'Welcome, choose a drink:')
    for drink in MENU.keys():
        print(drink.title())

    choice = input('which drink would you like?: ')
    if choice == 'off':
        global machine_on
        machine_on = False
        print("machine turning off")
        quit()
    elif choice == 'report':
        report()
        quit()
    make_drink(choice)


# START OF PROCESS HERE:
while machine_on:
    make_selection()


