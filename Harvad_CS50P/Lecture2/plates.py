def main ():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')


def is_valid(s):
    if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        for i in s:
            if i.isdigit():
                index = s.index(i)
                if s[index:].isdigit() and int(i) != 0:
                    return True
                else:
                    return False
        return True


main()