
expression = input('Expression: ')

x, y, z = expression.split(' ')

if y == '+':
    print(int(x) + int(z))
elif y == '-':
    print(int(x) - int(z))
elif y == '/' and z != 0:
    print(int(x) / int(z))
elif y == '*':
    print(int(x) * int(z))
else:
    print('nanik')


