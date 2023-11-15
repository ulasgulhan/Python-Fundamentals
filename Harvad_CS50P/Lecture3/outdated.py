
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input('Date: ')
        if '/' in date:
            month, day, year = date.split('/')
        elif ',' in date:
            date = date.replace(',', '')
            month, day, year = date.split(' ')
            if month in months:
                month = months.index(month) + 1
        try:
            if 12 < int(month) or 31 < int(day):
                continue
            else:
                break
        except ValueError:
            continue
    except EOFError:
        print()
        break

print(f'{year}-{int(month):02}-{int(day):02}')


