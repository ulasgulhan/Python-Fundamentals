
# Tuple (Demetler)
# List objesi ile benzer mantığa sahiptir. Lakin listelere uyguladığımız gömülü (built-in) fonksiyonlara sahip değildir
# Lakin index mantıkları aynıdır. Hem listelerde hem de demetlerdeki bir ortak nokta dilimleme (slicing) işlemi yapılabilir.

# tuple_1 = ('Fenerbahçe', 'Galatasaray', 'Beşiktaş', 'Trabzonspor', 'Adana Demir Spor')
# tuple_2 = (12, 35.5, 'b', 'Eagels', 'Patrios', 'Red Skins', ' Seahwak')
#
# # Demetleri (tuple) birbirleriyle birleştirebiliyoruz. Bunu listelerdeki extend() fonskiyonu gibi düşünebilirsiniz
#
# tuple_3 = tuple_1 + tuple_2
# print(tuple_3)
#
# # Dilimleme(Slicing)
# print(tuple_3[0:3]) # output => ('Fenerbahçe', 'Galatasaray', 'Beşiktaş')
# print(tuple_3[2:4]) # output => ('Beşiktaş', 'Trabzonspor')
#
# print(tuple_3[::2]) # output => ('Fenerbahçe', 'Beşiktaş', 'Adana Demir Spor', 35.5, 'Eagels', 'Red Skins')
# print(tuple_3[-1]) # output => Seahwak
# print(tuple_3[::-1]) # output => (' Seahwak', 'Red Skins', 'Patrios', 'Eagels', 'b', 35.5, 12, 'Adana Demir Spor', 'Trabzonspor', 'Beşiktaş', 'Galatasaray', 'Fenerbahçe')
# print(tuple_3[::-2]) # output => (' Seahwak', 'Patrios', 'b', 12, 'Trabzonspor', 'Galatasaray')
# print(tuple_3[3::-2]) # output => ('Trabzonspor', 'Galatasaray')

tuple_4 = ('Sarıyer', ('Suadiye', 'Erenköy'), ('Yeniköy', 'Bebek', ('Etiler', 'Ulus')))
print(tuple_4[2])
print(tuple_4[1][1])
print(tuple_4[2][2][0])

my_family = [
    ('Burak Yılmaz', 34, 'beast'),
    ('Hakan Yılmaz', 37, 'bear'),
    ('İpek Yılmaz', 39, 'keko')
]

for x, y, z in my_family:
    print(f'Full Name: {x}\n'
          f'Age: {y}\n'
          f'Alias: {z}')
