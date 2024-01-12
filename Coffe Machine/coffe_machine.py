from recipes import MENU
from recipes import RESOURCES


def machine_hello():
    print("Welcome to the Coffe Machine!\n")
    print("1 - Menu: \n2 - Insert Coins \n3 - Operator")
    option = int(input("Select an option: "))
    return option


def order_management(coffe, machine_balance):
    resource = check_resources(coffe)
    coffe_name = list(MENU.keys())[coffe-1]
    if resource:
        print(f"\nYou chose {coffe_name}. Let's proceed with your order.")
        print("Insert your coins: ")
        machine_balance = money_management(MENU[coffe_name]['cost'], machine_balance)
        resource_management(coffe_name)
    else:
        print("Sorry, machine have not enough resources!")
    return machine_balance

def money_management(cost, machine_balance):
    coin_quarters = int(input("How many QUARTERS coins: "))*0.25
    print(f'Actual credit: ${coin_quarters}, you need ${cost}.')
    coin_dimes = int(input("How many DIMES coins: "))*0.10
    print(f'Actual credit: ${coin_quarters+coin_dimes}, you need ${cost}.')
    coin_nickles = int(input("How many NICKLES coins: "))*0.05
    print(f'Actual credit: ${coin_quarters+coin_dimes+coin_nickles}, you need ${cost}.')
    coin_pennies = int(input("How many PENNIES coins: "))*0.01
    
    user_money = coin_quarters+coin_dimes+coin_nickles+coin_pennies
    print(f'Actual credit: ${user_money}, you need {cost}.')
    print(f'MACHINE BALANCE {machine_balance}')
    if user_money >= cost:
        machine_balance+=cost
        print("Preparing the coffe...")
        print("Ready to take!")
        print(f'Your change is: ${user_money - cost}')
        print(f'BALANCE {machine_balance}')
    return machine_balance

def resource_management(coffe_name):
    RESOURCES["water"] -= MENU[coffe_name]["ingredients"]["water"]
    RESOURCES["milk"] -= MENU[coffe_name]["ingredients"]["milk"]
    RESOURCES["coffee"] -= MENU[coffe_name]["ingredients"]["coffee"]


def check_resources(coffe):
    coffe_name = list(MENU.keys())[coffe-1]
    for keys in RESOURCES:
        try:
            print(f'Machine resource: {RESOURCES[keys]}')
            print(f'Needed resource: {MENU[coffe_name]['ingredients'][keys]}')            
            if RESOURCES[keys] >= MENU[coffe_name]['ingredients'][keys]:
                print("Enough")
                return True
        except ValueError: 
            print("Sorry")           
            return False
        

def op_management(op_option, machine_balance):
    if op_option == 1:
        print("option not implemented yet")
    elif op_option == 2:
        print("option not implemented yet")
    elif op_option == 3:
        for keys in RESOURCES:
            RESOURCES[keys] = int(input(f'{keys} quantity: '))
    else:
        print("\nReporto of the machine:")
        print(f'Water: {RESOURCES["water"]}ml ')
        print(f'Milk: {RESOURCES["milk"]}ml ')
        print(f'Coffe: {RESOURCES["coffee"]}g ')
        print(f'Money: ${machine_balance} ')

def machine(machine_balance):
    option = machine_hello()
    if option == 1:
        print("\nYou Coffe options are: ")

        index = 1
        for keys in MENU.keys(): 
            paddind_size = max(0, 15 - len(keys))
            print(f"{index} - {keys} {' ' * paddind_size} ${MENU[keys]["cost"]}")
            index+=1

        coffe = int(input("Chose your coffe: "))
        machine_balance = order_management(coffe, machine_balance)

    elif option == 3:
        print("You are in OPERATION mode!\n")
        print("1 - Insert coins: \n2 - Rescue Coins \n3 - Add Resources \n4 - Report")
        op_option = int(input("Select an option: "))
        op_management(op_option, machine_balance)
    return machine_balance

machine_balance = 0
while True:   
    machine_balance = machine(machine_balance)
