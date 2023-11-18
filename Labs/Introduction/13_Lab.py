
# Dandik bankamatik uygulaması

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

# Çekilmek istenilen bakiye tarafından karşılanmalı
# Miktar bakiyeden fazla iste ek hesap kullanılsın mı diye müşteriden onay alınsın
# Müşteri evet derse ek hesap devreye girsin para çekilsin
# Hayır derse işlem iptal edilsin
# Adamın balance ve additional balance çekilmek istenilen tutarı karşılamıyorsa feedback verip işlem otomatik olarak durdurulsun

# region Ben yaptım

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

# endregion


# region Hoca yaptı

# def withdraw_money(amount: int, account: dict) -> None:
#     if account['balance'] >= amount:
#         account['balance'] -= amount
#         print("Don't forget to take your money..!")
#         balance_result(account)
#     else:
#         total_balance = account['balance'] + account['additional_balance']
#         if total_balance >= amount:
#             use_additional_balance = input('Insufficent balance. Do you want to use additioanl balance? ').lower()
#
#             match use_additional_balance:
#                 case 'yes':
#                     amount_used_additional_balance = amount - account['balance']
#                     account['balance'] = 0
#                     account['additional_balance'] -= amount_used_additional_balance
#                     balance_result(account)
#                 case 'no':
#                     print('Transaction has been cancalled..!')
#                     balance_result(account)
#                 case _:
#                     print('Please choose valid answer..! ("yes" or "no")')
#         else:
#             print('Insufficent total balance. Transaction cancalled..!')
#
#
# def balance_result(account: dict) -> None:
#     print(f"You have {account['balance']} TL account number {account['account_no']}.\n"
#           f"Additional balance has {account['additional_balance']}")
#
#
# def deposit_money(account: dict, amount: int) -> None:
#     account['balance'] += amount
#     if account['additional_balance'] < 1000:
#         transfered_amount = 1000 - account['additional_balance']
#         account['balance'] -= transfered_amount
#         account['additional_balance'] += transfered_amount
#     balance_result(account)
#
#
# def menu(account: dict) -> None:
#     print(f"""
#     Welcome, {account['full_name']}
#     =================================
#     Withdraw Money                =>1
#     Deposit Money                 =>2
#     Account Info                  =>3
#     EFT                           =>4
#     Exit                          =>5
#     """)
#
#
# def show_account_information(account: dict) -> None:
#     print(f"Account Infrmation\n"
#           f"==================\n"
#           f"Full Name: {account['full_name']}\n"
#           f"Account No: {account['account_no']}\n"
#           f"User Name: {account['user_name']}\n"
#           f"Password: {account['password']}\n"
#           f"Balance: {account['balance']}\n"
#           f"Additional Balance: {account['additional_balance']}")
#
#
# def eft_transaction(sender_account: dict, reciver_account_no: str, amount: int) -> None:
#     for user in users:
#         if user['account_no'] == reciver_account_no:
#             if sender_account['balance'] >= amount:
#                 sender_account['balance'] -= amount
#                 user['balance'] += amount
#                 balance_result(sender_account)
#             else:
#                 total_balance = sender_account['balance'] + sender_account['additional_balance']
#                 if total_balance >= amount:
#                     use_additional_balance = input('Insufficent balance. Do you want to use additional balance? ("yes" or "no") ').lower()
#                     if use_additional_balance == 'yes':
#                         amount_used_additional_balance = amount - sender_account['balance']
#                         sender_account['balance'] = 0
#                         sender_account['additional_balance'] -= amount_used_additional_balance
#                         balance_result(sender_account)
#                         user['balance'] += amount
#                     elif use_additional_balance == 'no':
#                         print('Transaction has been cancaled..!')
#                         balance_result(sender_account)
#                     else:
#                         print('Please type valid answer like "yes" or "no"')
#                 else:
#                     print('Insufficent balance. Transaction has been cancaled..!')
#
#
#
# def log_in(user_name: str, password: str) -> dict:
#     account = {}
#     for user in users:
#         if user['user_name'] == user_name and user['password'] == password:
#             account = user
#             break
#
#     return account
#
#
# def main():
#     user_account = log_in(
#         input('User Name: ').lower(), input('Password: ')
#     )
#     if user_account != {}:
#         menu(user_account)
#         process = input('Please choose a process: ')
#         match process:
#             case '1':
#                 withdraw_money(int(input('Amount: ')), user_account)
#             case '2':
#                 deposit_money(user_account, int(input('Amount: ')))
#             case '3':
#                 show_account_information(user_account)
#             case '4':
#                 eft_transaction(user_account, input('IBAN: '), int(input('Amount: ')))
#             case '5':
#                 print('Application has been closing')
#             case _:
#                 print('Please choose valid process number..!')
#     else:
#         print('Authentication faild. Please check your information..!')
#
#
# main()

# endregion
