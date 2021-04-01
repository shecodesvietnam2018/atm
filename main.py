balance = 10000
limit = 100000000
history = []


def deposit(amount):
    global balance
    global limit
    global history
    if balance + amount > limit:
        raise Exception("Limit exceeded")
    balance = balance + amount
    history.append(f"Deposit {amount} to account")


def withdraw(amount):
    global balance
    global history
    if amount > balance:
        raise Exception("Balance cannot be negative")
    balance = balance - amount
    history.append(f"Withdraw {amount} from account")


def display_history():
    global history
    print("History:")
    for content in history:
        print(content)


while True:
    print(f"Current balance: {balance}")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display history")
    print("4. Exit")
    selection = int(input("Your selection: "))
    while selection != 1 and selection != 2 and selection != 3 and selection != 4:
        selection = int(input("Your selection: "))
    try:
        if selection == 1:
            amount = int(input("How much money do you want to deposit? "))
            deposit(amount)
        elif selection == 2:
            amount == int(input("How much money do you want to withdraw? "))
            withdraw(amount)
        elif selection == 3:
            display_history()
        else:
            break
    except Exception as e:
        print(e)
    finally:
        print()  # New line on the screen
