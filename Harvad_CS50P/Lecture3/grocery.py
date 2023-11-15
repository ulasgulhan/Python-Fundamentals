
list = {}


while True:
    try:
        item = input().upper()
        if item in list:
            list[item] += 1
        else:
            list[item] = 1
    except EOFError:
        for item in sorted(list.keys()):
            print(list)
            print(list[item], item)
        break