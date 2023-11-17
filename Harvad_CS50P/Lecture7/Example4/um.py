import re


def main():
    print(count(input("Text: ")))


def count(s):
    if ums := len(re.findall(r'\b\W*um\W*', s, flags=re.IGNORECASE)):
        return ums



if __name__ == "__main__":
    main()