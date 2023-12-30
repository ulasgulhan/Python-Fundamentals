import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing, metrics
from sklearn.model_selection import train_test_split

df = pd.read_csv('Data/teleCust1000t.csv')
print(df.head().to_string())

# Hangi pakatte kaç kullanıcı var
# print(df['custcat'].value_counts())


# KNN algoritmasında her bir noktanın diğer bir noktaya olan mesafesini hesaplamak için geometrik hesaplamalar yapılmaktadır. Bunun için veri setimizdeki her bir value alacağız. Esasen burada bir matrix oluşturuyorum.

# Değerleri incelediğimizde income sütununda bir değer 944 iken age sütunundaki değerler ya da regionda ise 1 ve 0 var. Bu tüm değerler scaler olarak farklı büyüklüklere sahip. Bu yüzden veri setimizdeki valueları normalize etmemiz gerekmektedir.


# Normalizasyon İşlemi
# Adım 1: Sütun isimlerini dökelim. Bu sütun başlklarından faydanalarak bu sütunda tutulan valuelara erişeceğiz.

# print(df.columns)

# Adım 2: Yukarıda aldığımız sütun isimlerinden faydanalarak değerlere erişerek 'features matrix' elde edeceğiz.

X = df[['region', 'tenure', 'age', 'marital', 'address', 'income', 'ed',
        'employ', 'retire', 'gender', 'reside']].values

# print(X)
# Adım 3: Custcat sütunu için de bir features matrix elde edelim.

y = df['custcat'].values

# Adım 4: Normalize edilecek alanlar yukarıda oluşturuldu. Şimdi sklearn preprocessing modülünden faydalanarak normalizasyon işlemini yerine getirelim.

X = preprocessing.StandardScaler().fit_transform(X)

# Veri setini split edelim.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# print(f'Train Sets: {X_train.shape} - {y_train.shape}')
# print(f'Test Sets: {X_test.shape} - {y_test.shape}')

# train veri setimizdeki her bir nokta için yani features için en yakın 4 komşusuna bakacak şekilde KNN modelimi train ediyorum. Burada 4 komşuyu her hangi bir mantık gözetmeksizin rasgele verdik.

neighbor = KNeighborsClassifier(n_neighbors=4).fit(X_train, y_train)
y_result = neighbor.predict(X_test)
# print(y_result)

# Doğruluk değerlendirmesi
# Birden fazla sınıf oluşturulacak ya da etiket oluşturulacak modellerde her bir sub class için doğrulama yapmak önemlidir. Burada istatistik alanında yoğun olarak kullanılan Jaccard Similarty Index kullanarak bunu yapabiliriz. Yani 'y_train' ile 'neighbor.predict(X_train)' ve 'y_test' 'ile neighbor.predict(X_test)' arasındaki benzerliği ve çeşitliliği bulmak için kullanacağız. Bunun için sklearn modülünde bulunan accuracy_score() fonksiyonunu kullanacağız. Bu fonksiyonun döndüğü sonuç 1'e yaklaşırsa başarılı, 0'a yakınsarsa başarısız.

print(f'Train Set Accuracy: {metrics.accuracy_score(y_train, neighbor.predict(X_train))}')
print(f'Test Set Accuracy: {metrics.accuracy_score(y_test, neighbor.predict(X_test))}')

# KNN algoritmasında en iyi 4 sınıfı bulmak için en yakın kaç komşuya bakmalıyım sorusunu irdeleyelim. Biz yukarıda kafamıza göre 4 verdik. Şimdi en yakın 1 komşudan 10 komşuya bakacak şekilde modelimizi tekrar train edelim.

k_neigh = int(input('Please type K number: '))
array_length = k_neigh - 1
jsi_acc = np.zeros(array_length)
std_acc = np.zeros(array_length)

for k in range(1, k_neigh):
    neigh = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    y_pred = neigh.predict(X_test)
    jsi_acc[k-1] = metrics.accuracy_score(y_test, y_pred)
    std_acc[k-1] = np.std(y_pred == y_test) / np.sqrt(y_pred.shape[0])

print(f'JSI Score: {jsi_acc}')
print(f'JSI Score: {std_acc}')

plt.plot(range(1, k_neigh), jsi_acc, c='g')
plt.fill_between(range(1, k_neigh), jsi_acc - 1 * std_acc + 1 * std_acc, alpha=0.10)
plt.legend(('accuracy', 'std'))
plt.ylabel('Accuracy')
plt.xlabel('Number of Neighbor')
plt.grid(True)
plt.tight_layout()
plt.show()

print(f'The best accuracy was with: {jsi_acc.max()}, with k={jsi_acc.argmax()}')
