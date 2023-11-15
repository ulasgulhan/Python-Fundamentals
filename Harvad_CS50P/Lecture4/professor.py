
import random


def main():
    generate_integer(get_level())
        



def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if 4 > level > 0:
                return level
        except ValueError:
            pass

def generate_integer(level):
    point = 0
    for i in range (10):
        if level == 1:      
            a = random.randint(0, 9)
            b = random.randint(0, 9)
        elif level == 2:
            a = random.randint(10, 99)
            b = random.randint(10, 99)
        elif level == 3:
            a = random.randint(100, 999)
            b = random.randint(100, 999)
        
        while True:
            for j in range(4):
                print(f'{a} + {b} = ', end='')
                try:
                    z = int(input())
                    if z == a + b:
                        point += 1
                        break
                    elif z != a + b:
                        if j < 2:
                            print('EEE')
                        else:
                            print('EEE')
                            print(f'{a} + {b} = {a + b}')
                            break
                except ValueError:
                    pass
            break
    print(point)

                        
            




if __name__ == "__main__":
    main()