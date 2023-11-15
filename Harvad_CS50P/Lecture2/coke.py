
amount = 50

while amount > 0:
    print(f'Amount Due: {amount}')
    money = int(input('Insert Coin: '))
    if money == 25 or money == 10 or money == 5 :
        amount -= money
    else:
        continue

change_owed = abs(amount)

print(f'Change Owed: {change_owed}')
# print(f'Change Owed: {amount * -1}')

