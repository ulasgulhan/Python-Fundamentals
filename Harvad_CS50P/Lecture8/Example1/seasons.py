from datetime import date
import inflect
import sys

p = inflect.engine()


def check_date(year, mounth, day):
    today = date.today()
    b_day = date(int(year), int(mounth), int(day))
    diffrance = today - b_day
    total_minutes = diffrance.days * 24 * 60
    output = p.number_to_words(total_minutes)
    return output

    

def main():
    try:
        year, mounth, day = input('Birth Date: ').split('-')
    except ValueError:
        sys.exit('Invalid Date')

    print(check_date(year, mounth, day))
    


if __name__ == "__main__":
    main()