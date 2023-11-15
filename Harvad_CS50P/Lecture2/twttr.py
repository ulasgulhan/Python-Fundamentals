
# region Solution 1

""" s = input('Input: ')

print('Output: ', end='')

for i in s:
    match i:
        case 'a' | 'e' | 'ı' | 'i' | 'o' | 'ö' | 'u' | 'ü' | 'A' | 'E' | 'I' | 'İ' | 'O' | 'Ö' | 'U' | 'Ü':
            pass
        case _:
            print(i, end='')

print() """

# endregion

s = input('Input: ')

print('Output: ', end='')

for i in s:
    if not i.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(i, end='')

print()

