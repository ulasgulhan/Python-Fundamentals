burak_account = {
    'account_no': '12345',
    'full_name': 'Burak Yılmaz',
    'user_name': 'beast',
    'password': '123',
    'balance': 3000,
    'additional_balance': 1000
}

hakan_account = {
    'account_no': '98765',
    'full_name': 'Hakan Yılmaz',
    'user_name': 'bear',
    'password': '123',
    'balance': 5000,
    'additional_balance': 1000
}

ipek_account = {
    'account_no': '56789',
    'full_name': 'İpek Yılmaz',
    'user_name': 'keko',
    'password': '123',
    'balance': 8000,
    'additional_balance': 1000
}

users = [burak_account, hakan_account, ipek_account]

def send_money(auth: dict, acc_no: str, money) -> None:
    for no in users:
        if no['account_no'] == acc_no:
            withdraw_money(auth, money)
            add_money(no, money)
        else:
            print('No account found..!')


def add_money(auth: dict, money) -> None:
    if auth['additional_balance'] < 1000:
        auth.update({'additional_balance': auth['additional_balance'] + money})
        if auth['additional_balance'] > 1000:
            extra = auth['additional_balance'] - 1000
            auth.update({'balance': auth['balance'] + extra})
            auth.update({'additional_balance': auth['additional_balance'] - extra})
    else:
        auth.update({'balance': auth['balance'] + money})


def login(user_name: str, password: str) -> dict:
    test = False
    user_id = {}
    for id in users:
        if id['user_name'] == user_name and id['password'] == password:
            test = True
            user_id = id
            break

    if test:
        return user_id
    else:
        return {}


def withdraw_money(account: dict, money: int) -> None:
    if money <= account['balance']:
        account.update({'balance': account['balance'] - money})
    elif money <= account['balance'] + account['additional_balance']:
        question = input('Do you want to use additional balance?: ')
        if question == 'yes':
            account.update({'balance': account['balance'] - money})
            account.update({'additional_balance': account['balance'] + account['additional_balance']})
            account.update({'balance': account['balance'] * 0})
        elif question == 'no':
            print('Process closing')
        else:
            print('This is a yes or no question')
    else:
        print('Not enough money')


def show_account_information(account: dict) -> None:
    print(f"Account Infrmation\n"
          f"==================\n"
          f"Full Name: {account['full_name']}\n"
          f"Account No: {account['account_no']}\n"
          f"User Name: {account['user_name']}\n"
          f"Password: {account['password']}\n"
          f"Balance: {account['balance']}\n"
          f"Additional Balance: {account['additional_balance']}\n"
          f"==================\n")


def menu(account: dict) -> None:
    print(f"""
    Welcome, {account['full_name']}
    =================================
    Withdraw Money                =>1
    Deposit Money                 =>2
    Account Info                  =>3
    EFT                           =>4
    Exit                          =>5
    """)


def main():
    auth_user = login(
        input('Username: '),
        input('Password: ')
    )
    menu(auth_user)
    while True:
        print(f"Welcome {auth_user['full_name']}\nYour Balance: {auth_user['balance']}\nYour Additional Balance: {auth_user['additional_balance']}")
        process = input('What process want you to do? ')
        if process == '1':
            withdraw_money(auth_user, int(input('Money: ')))
        elif process == '2':
            add_money(auth_user, int(input('Money: ')))
        elif process == '3':
            show_account_information(auth_user)
        elif process == '4':
            send_money(auth_user, input('Account No: '), int(input('Money: ')))
        elif process == '5':
            break


main()
