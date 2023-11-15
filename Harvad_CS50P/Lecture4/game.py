import random

while True:
    try:
        level = int(input('Level: '))
        if level > 0 and level.is_integer:
            break
    except:
         pass

integer = random.randint(1, level)

while True:
        try:
            guess = int(input('Guess: '))
            if guess > 0:
                if guess == integer:
                    print('Just right!')
                    break
                elif guess < integer:
                    print('Too small!')
                else:
                    print('Too large!')
        except:
             pass


