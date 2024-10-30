import time

print("---------- Welcome to WitziWings --------------")

food = {
    "popcorn" : 50,
    "eggpuff" : 30,
    "sweetcorn" : 40,
    "icecream" : 30,
    "pepsi" : 40.5,
    "samosa" : 20.8,
    "chickenpuff" : 40,
    "thumbsup" : 40.7,
    "waffles" : 30,
    "potatochips" : 20,
    "fries" : 60,
    "donut" : 40,
    "pizza" : 150,
    "burger" : 70
}

cart = []
total = 0

time.sleep(2)

print("------------------ Menu -----------------------")
for keys, values in food.items():
    print(f'{keys:15} : {values:.2f} rs')
print("-----------------------------------------------")

while True:
    select = input("Select Your food / q to Quit: ").lower()
    if select == "q":
        break
    elif food.get(select) is not None:
        cart += [select]

print("---------------- Your Order ------------------")

for item in cart:
    total += food.get(item)
    print(item, end=' ')

print()
print(f"Total is : {total:.2f} rs")

