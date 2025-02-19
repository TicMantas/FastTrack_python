income = 0
spending = 0
spending_dict = {}
running = True

def place_income():
    amount = float(input(f'{" "*100}Enter Your Income: '))
    if amount < 0:
        print(f'{" "*100}That is not valid')
        return 0
    print(f'{" "*100}Amount been added to your balance: ${amount:.2f}')
    return amount


def place_spendings():
    reason = input(f"{" "*100}Enter the reason for spending: ")
    spend = float(input(f'{" "*100}Enter Your Spendings: '))

    if spend < 0:
        print(f'{" "*100}That is not valid')
        return 0
    else:
        print(f'{" "*100}Amount been added to your spending balance: ${spend:.2f}')

        spending_dict[reason] = spending_dict.get(reason, 0) + spend

        return spend


def show_balance():
    deducted_amount = income - spending
    print(f'{" "*100}Your balance is ${deducted_amount:.2f}')


def show_spending_total():
    print(f'{" "*100}Your total spending is ${spending:.2f}')
    print(f"{" "*100}Here is a breakdown of your spendings:")

    if spending_dict:
        for reason, amount in spending_dict.items():
            print(f'{" "*100}- {reason}: ${amount:.2f}')
    else:
        print(f"{" "*100}No spendings recorded yet.")


def show_statement():
    print(f"{" "*100}Transaction Statement:")
    print(f'{" "*100}Total Income: ${income:.2f}')
    show_spending_total()
    print(f'{" "*100}Final Balance: ${income - spending:.2f}')

while running:
    print(' **********************')
    print(' Budget Program')
    print(' **********************')
    print(f'{" "*30}1. Place Income ')
    print(f'{" "*30}2. Place Spendings ')
    print(f'{" "*30}3. Show Balance')
    print(f'{" "*30}4. Show Spending Total ')
    print(f'{" "*30}5. Show Statement')
    print(f'{" "*30}6. Exit')

    choice = input("Choose a program: ")

    if choice == '1':
        income += place_income()
    elif choice == '2':
        spending += place_spendings()
    elif choice == '3':
        show_balance()
    elif choice == '4':
        show_spending_total()
    elif choice == '5':
        show_statement()
    elif choice == '6':
        running = False
        print('^^^^^^^^^ See you soon ^^^^^^^^^^')
    else:
        print('^^^^^^^ That is not a valid program ^^^^^^^')

