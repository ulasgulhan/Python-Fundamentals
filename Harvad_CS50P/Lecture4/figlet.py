from pyfiglet import Figlet
import sys
import random


figlet = Figlet()

if len(sys.argv) == 1:
    is_random_font = True
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    is_random_font = False
else:
    sys.exit()

figlet.getFonts()

if is_random_font == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print('Invalid usage')
        sys.exit()
else:
    font = random.choice(figlet.getFonts())

msg = input('Input: ')

print('Output:')
print(figlet.renderText(msg))
