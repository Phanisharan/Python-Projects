import time
import random

def spin_row():
    symbols = ["🍒", "🍋", "🍉", "🔔", "⭐"]

    return [random.choice(symbols) for _ in range(3)]
    
def print_row(row):
    print("****************")
    print(" | ".join(row))
    print("****************")

def pay_out(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 2
        elif row[0] == "🍉":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 2
        elif row[0] == "⭐":
            return bet * 2
    return 0

def main():
    
    balance = 100

    print("*********************************************")
    print("       Welcome to the Spinroll Madrip        ")
    print("*********************************************")
    time.sleep(1)
    print(f"Congrats! You got a Joining bonus : {balance}")
    time.sleep(1)
    print("Lets play a Game!!!")
    time.sleep(1)
    print("Here is your symbols 🍒 🍋 🍉 🔔 ⭐")
    time.sleep(1)
    
    while balance > 0:
        print(f"Current balance : {balance}")

        bet = input("Let's bet your amount : ")
        if not bet.isdigit():
            print("Please enter a valid amount")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        elif bet < 0:
            print("The value should be greater than 0")
            continue
       
        balance -= bet

        row = spin_row()
        print("Spinning..../n")
        time.sleep(3)
        print("Spinning....n-")
        time.sleep(3)
        print("Spinning....-n")
        time.sleep(3)

        print_row(row)

        get_pay = pay_out(row, bet) 

        if get_pay > 0:
            print(f"you won {get_pay}")
        else:
            print("Sorry you lost this round")

        balance += get_pay

        user = input("Do You want to play again (Y/N) : ").lower()

        if user == 'y':
            continue
        elif user == 'n':
            break

    print("*********************************************")
    print(f"     Game over! Your current balance {balance}  ")
    print("*********************************************")

if __name__ == "__main__":
    main()