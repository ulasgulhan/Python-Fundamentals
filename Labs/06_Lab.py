
# List
# Uygulama içerisinde anlık olarak bizim için içerisinde bir yada birden fazla değer tutan yapıdır. Birden fazla tipte farklı değer tutabilir. Listeler RAM üzerinde heap alanında tutulduğu için uygulama kapatıldığında yaratıldıkları hallerine geri dönerler.

# Listeler index mantığı ile çalışırlar. Liste içerisinde sakladığı değerleri sıfırıncı index'ten başlayarak pozitif yönde artan index değerleri içerisinde saklar. Yani tutulan her değerin bir index'i vardır

top_boxers = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewis', 'Evander Holyfiled', 'Rocky Marcio']
print(top_boxers[0])

# region Task 1
# George Forman bilgisini listeye ekleyin
top_boxers.append('George Forman')
print(top_boxers)

# endregion

# region Task 2
# İlgili listenin 3 index'ine 'Floyd Meyweater' bilgisini ekletin
top_boxers.insert(3, 'Floyd Meyweater')
print(top_boxers)

# endregion

# region Task 3
# İlgili listeden 'Floyd Meyweather' bilgisini silin
# top_boxers.remove('Floyd Meyweater')
# print(top_boxers)
# endregion

# region Task 4
# İlgili listeden 4.index'te bulunan bilgiyi silin
top_boxers.pop(4)
print(top_boxers)
# endregion

# region Task 5
# current_boxers = ['Tyson Fury', 'Deantony Wilder', 'Antony Jasua'] listesi ile top_boxers listesini birleştirin
current_boxers = ['Tyson Fury', 'Deantony Wilder', 'Antony Jasua']
top_boxers.extend(current_boxers)
print(top_boxers)
# endregion

# region Task 6
# Boş bir liste içerisinde 0 ile 100 arasında random olacak şekilde 10 adet sayı ile doldurun
# from random import randint
# sayilar = []
# for i in range(10):
#     random_number = randint(0, 100)
#     sayilar.append(random_number)
# print(sayilar)

# endregion

# region Task 7
# Kullanıcıdan bir söz öbeği alıyoruz
# Örneğin merhaba ben ulaş.
# Bu söz öbeğindeki her bir harfi bir listeye ekleyelim. not: string ifadeler birer harf listesidir
# list = []
# soz = input('Bir şey yazınız: ')
# for i in soz:
#     list.append(i)
# print(list)

# endregion

# region Example 2
# iki listeyi random sayılar ile dolduralım. akabinde benzer index'lerde tutulan değerler toplatılarak 3.bir listede gene aynı
# indexe'e yazılsın
# from random import randint
#
# list_1 = []
# list_2 = []
# toplam = []
#
# for i in range(10):
#     list_1.insert(i, randint(0, 100))
#     list_2.insert(i, randint(0, 100))
#     toplam.insert(i, (list_1[i] + list_2[i]))
#
# print(toplam)


# endregion

# List Comprehansions
# print([i * i for i in range(10)])

# region Example 3
# 0-100 arasında tam bölünen sayıların karesini listeye dökelim

# print([i * i for i in range(100) if i % 3 == 0])

# endregion