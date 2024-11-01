def show_balance(balance):
    print(f"Your current balance is : {balance:.2f} rs ")

def deposit():
    amount = float(input("Enter an amount to deposit : "))
    if amount < 0:
        print("Invalid amount")
    if amount > 0:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to withdraw : "))

    if amount > balance:
        print("Insufficient amount")
        return 0
    elif balance < 0:
        print("Insufficient amount")
        return 0
    elif balance > 0:
        return amount

def main():
    balance = 0
    is_running = True

    print("*****************************************")
    print("         Welcome to Paris banking        ")
    print("*****************************************")

    while is_running:

        print("*****************************************")
        print("1. Show balance\n2. Deposit\n3. Withdraw\n4. Exit")
        print("*****************************************")

        user = input("Enter Your Choice (1-4) : ")

        if user == "1":
            show_balance(balance)
        elif user == "2":
            balance += deposit()
        elif user == "3":
            balance -= withdraw(balance)
        elif user == "4":
            is_running = False
        else:
            print("Invalid Choice")

    print("*****************************************")
    print(" Thank you for visiting Have a nice day! ")
    print("*****************************************")

if __name__ == "__main__":
    main()