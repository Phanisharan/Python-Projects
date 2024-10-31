credit_card  = input('Enter your credit card number : ')
credit_card_no = ""
for i in credit_card:
    if i == "-" or i == " ":
        credit_card_no += ""
    else:
        credit_card_no += i
# print(credit_card_no)

credit_card_no = credit_card_no[::-1]

sum_of_odd = 0
sum_of_even = 0

for i in credit_card_no[::2]:
    sum_of_odd += int(i)

for i in credit_card_no[1::2]:
    i = int(i) * 2
    if i >= 10:
        sum_of_even += (1 + (i % 10))
    elif i <= 10:
        sum_of_even += i

total = sum_of_even + sum_of_odd

if total % 10 == 0:
    print("Valid")

else:
    print("In-Valid")

