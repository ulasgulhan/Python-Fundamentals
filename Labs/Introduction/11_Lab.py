
# lst = [12, 11, 19, 2, 99]
# lst_1 = []
#
# # lst içerisindeki sayılardan çift sayıları 2 ile tek sayıları 3 ile çarparak lst_1 içerisine ekleyelim.
#
#
# def tek_cift_mi(sayi: int) -> str:
#     if sayi % 2 == 0:
#         return 'çift'
#     else:
#         return 'tek'
#
#
# def append_list(result: str, counter: int) -> None:
#     if result == 'çift':
#         lst_1.append(counter * 2)
#     else:
#         lst_1.append(counter * 3)
#
#     print(lst_1)
#
#
# def main():
#     for i in lst:
#         result = tek_cift_mi(i)
#         append_list(result, i)
#
#
# main()


# Kullanıcıdan alınan 3 adet sayıyı topladıktan sonra karesini alarak nihai sonucu kullanıcıya çıktı verelim.

# def toplam(s1: int, s2: int, s3: int) -> int:
#     return s1 + s2 + s3
#
#
# def kare(result: int) -> None:
#     print(f'Sonuc: {result ** 2}')
#
#
# def main():
#     x = int(input('Sayı: '))
#     y = int(input('Sayı: '))
#     z = int(input('Sayı: '))
#
#     sonuc = toplam(x, y, z)
#
#     kare(sonuc)
#
#
# main()


# Kullanıcı sign up sonra sing in olsun.
# Kullanıcı bilgileri dict tutulsun.

# user_dict = {
#     '1': {
#         'user_name': 'beast',
#         'password': '123'
#     },
#     '2': {
#         'user_name': 'bear',
#         'password': '123'
#     }
# }
#
#
# def get_user_name(users: dict) -> list:
#     user_name_list = []
#
#     for i in range(1, len(users) + 1):
#         user_name_list.append(users.get(str(i)).get('user_name')) #.get mantığı 91.satırdaki user_dict[str(id)]['user_name'] mantığı ile aynı.
#
#     return user_name_list
#
#
# def sign_up(username: str, password: str) -> None:
#     if username in get_user_name(user_dict):
#         print('Kullanıcı adı daha önce alınmış')
#     else:
#         user_dict[str(len(user_dict) + 1)] = {
#             'user_name': username,
#             'password': password
#         }
#         print('Kullanıcı oluşturuldu')
#
#
# def sign_in(username: str, password: str) -> None:
#     test = False
#     for id in user_dict:
#         if user_dict[str(id)]['user_name'] == username and user_dict[str(id)]['password'] == password:
#             print('Giriş yapıldı')
#             test = True
#             break
#     if not test:
#         print('Kullanıcı adı ya da şifre hatalı')
#
#
# def main():
#     while True:
#         process = input('İşlem giriniz: ').lower()
#
#         if process == 'çıkış':
#             print('Çıkış yapılıyor...')
#             break
#         elif process == 'giriş yap':
#             username = input('Kullanıcı adı: ')
#             password = input('Şifre: ')
#             sign_in(username, password)
#         elif process == 'kayıt ol':
#             username = input('Kullanıcı adı: ')
#             password = input('Şifre: ')
#             sign_up(username, password)
#         else:
#             print('Lütfen uygun işlem türü giriniz...')
#
#
# main()



# Aşağıdaki listede bulunan rakamların sıklığını bulun ve  sözlük tipinde çıktı verin

# rakamlar = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 4, 3, 2, 2, 2, 1]
#
# def how_many(sayi: list) -> list:
#     numbers = set(sayi)
#     adet_rakam = {}
#     for i in numbers:
#         adet_rakam.update({i: sayi.count(i)})
#
#     print(adet_rakam)
#
#
#
# def main():
#     how_many(rakamlar)
#
#
# main()


# Bir söz öbeğinde tekrar eden kelimelerden arındırılarak çıktı verilsin
# input => merhaba ben burak burak ben burak
# output => merhaba ben burak


# def unique(input: str) -> None:
#     words = input.split()
#     clean_words = []
#     for word in words:
#         if word not in clean_words:
#             clean_words.append(word)
#     print(' '.join(clean_words))
#
#
# def main():
#     say = input('Bir şey söyle: ')
#     unique(say)
#
#
# main()


# Kullanıcıdan alınan söz öbeğindeki kelimeleri alfabetik olarak sıralayan fonksiyonu yazın

#
# def alph(input: str) -> None:
#     words = input.split()
#     alph_words = sorted(words)
#     print(alph_words)
#
#
# def main():
#     say = input('Bir şey söyle: ')
#     alph(say)
#
#
# main()


# Bir kullanıcı listesi geliyor. Bu kullanıcılara mail adresi yaratılacak
# birinic_isim.ikinic_isim@bilgeadam.com
# oluşturulan mailler de mails = [] listesine eklenecek
# kendinize bu listeyi mail atın


import smtplib
import unidecode
import xlsxwriter
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


users = [
    ('Burak Yılmaz', 'ARGE'),
    ('Murat', 'IK'),
    ('İpek Bayar Yılmaz', 'Software Developer'),
    ('Hakan Mesut Kerim Yılmaz', 'Simyacı'),
    (' ', 'Kaçakçı')
]

mails = []


def add_list(the_mail):
    if len(the_mail) > 1:
        mails.append(f'{unidecode.unidecode(the_mail[0])}.{unidecode.unidecode(the_mail[1])}@bilgeadam.com')
    elif len(the_mail) == 1:
        mails.append(f'{unidecode.unidecode(the_mail[0])}@bilgeadam.com')
    else:
        pass


def send_mail(name: str, excel_name: str):
    message = MIMEMultipart()
    part = MIMEBase('application', 'octet-stream')
    with open(f'{excel_name}.xlsx', 'rb') as attachment:
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={excel_name}.xlsx')
    message.attach(part)
    message["To"] = 'ulasgulhan9@gmail.com'
    message["From"] = 'Ulaş Gülhan'
    message["Subject"] = 'Şirket Mailleri'

    message_text = MIMEText(f'''{name} selam,

Şirketimizde bulunan kişilerin mail adreslerini ekte görebilirsiniz.

İyi çalışmalar dilerim.''')
    message.attach(message_text)

    email = 'ulasgulhan9@gmail.com'
    password = 'grwv grrm mkoc gkqb'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo('Gmail')
    server.starttls()
    server.login(email, password)
    fromaddr = 'ulasgulhan9@gmail.com'
    toaddrs = 'ulasgulhan9@gmail.com'
    server.sendmail(fromaddr, toaddrs, message.as_string())

    server.quit()
    os.remove(f'{excel_name}.xlsx')


def excel(excel_name):
    with xlsxwriter.Workbook(f'{excel_name}.xlsx') as workbook:
        worksheet = workbook.add_worksheet()

        for row_num, data in enumerate(mails):
            worksheet.write(row_num, 0, data)
    return excel_name


def main():
    for employers in users:
        for names in employers:
            get_name = names.lower()
            split_name = get_name.split()
            add_list(split_name)

    send_mail('Ulaş', excel('deneme'))


main()
