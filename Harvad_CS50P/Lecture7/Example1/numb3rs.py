import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    regex_pattern = r'^' + regex() + r'\.' + regex() + r'\.' + regex() + r'\.' + regex() + r'$'
    if match := re.search(regex_pattern, ip):
        return True
    else:
        return False


def regex():
    return r'\b([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])'


if __name__ == "__main__":
    main()