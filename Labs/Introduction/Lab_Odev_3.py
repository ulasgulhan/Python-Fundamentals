
# Kullanıcı girdiği password is valid mi?
# 1.girilen şifre en az 16 karakter olmalıdır.
# 2.en az bir büyük harf bir küçük harf içermelidir.
# 3.en az bir rakam olmasını istiyoruz.
# 4.mutlaka noktalama işaretleri olmalı.
# 5.herhangi bir ifade tekrar etmemeli.

password = input('Password: ')

if len(password) > 16 and any(i.isdigit() for i in password) and any(i in 'password' for i in password):
    if any(i.isupper() for i in password) and any(i.islower() for i in password) and len(set(password)) == len(password):
        print('Valid')
    else:
        print('Not Valid')
else:
    print('Not Valid')

