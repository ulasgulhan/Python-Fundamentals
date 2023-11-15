
while True:
    try:
        fuel = input('Fraction: ')
        x, y = fuel.split('/')
        try:
            s = (int(x)/int(y)) * 100
            if 0 <= s <= 100:
                if s >= 99:
                    print('F')
                elif s <= 1 or s == 0:
                    print('E')
                else:
                    print(f'{s}%')
                break
        except ZeroDivisionError:
            pass
    except ValueError:
        pass


