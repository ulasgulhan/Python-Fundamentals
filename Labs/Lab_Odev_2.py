import timeit

# region Example 1
# Kullanıcıdan bir söz öbeği alıyoruz
# Örneğin merhaba ben Ulaş
# Bu söz öbeğindeki her harfi bir listeye ekleyeceğiz. Sesli ve sessiz harfler ayrı listelerde tutulacak.
# Bir harf bir kere listeye girebilecek. Listede boşluk karakteri bulunmayacak.

# start = timeit.default_timer()
#
# sesli_harf = []
# sessiz_harf = []
# soz = input('Bir şey yazınız: ')
#
# for i in soz:
#     if i not in sessiz_harf and i not in sesli_harf:
#         match i:
#             case ' ':
#                 pass
#             case 'a' | 'e' | 'ı' | 'i' | 'o' | 'ö' | 'u' | 'ü':
#                 sesli_harf.append(i)
#             case _:
#                 sessiz_harf.append(i)
#     else:
#         pass
#
# print(f'Yazdığınız yazıdaki sesli harfler: {sesli_harf}')
# print(f'Yazdığınız yazıdaki sessiz harfler: {sessiz_harf}')
#
# stop = timeit.default_timer()
#
# print(f'Time 1: {start}, {stop}')


# endregion

# region Example 1 - 2

# start2 = timeit.default_timer()
#
# sesli_harf = []
# sessiz_harf = []
# soz = input('Bir şey yazınız: ')
#
# for i in soz:
#     if i.isalpha() and i not in sesli_harf and i not in sessiz_harf:
#         if i in 'aeıioöuüAEIİOÖUÜ':
#             sesli_harf.append(i)
#         else:
#             sessiz_harf.append(i)
#
# print(f'Sesli Harfler: {sesli_harf}')
# print(f'Sessiz Harfler: {sessiz_harf}')
#
# stop2 = timeit.default_timer()
#
# print(f'Time 2: {start2}, {stop2}')

# endregion

