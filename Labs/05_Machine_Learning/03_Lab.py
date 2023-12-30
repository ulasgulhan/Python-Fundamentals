
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing, metrics, tree
from sklearn.model_selection import train_test_split


df = pd.read_csv('Data/drug200.csv')


X = df[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values

# X isimli matrix incelendiğinde Sex, BP, Cholesterol gibi featuresların değerlerinin sözel olduğunu görebilirsiniz. Bir bu çalışmada karar ağacı oluşturacağız ve bunun içinde entropi hesaplaması yapacağız. Bu bağlamda bu categorical featuresları scaler büyüklüklere dönüştürmemiz lazım.

le_sex = preprocessing.LabelEncoder()
le_sex.fit(['F', 'M'])
X[:, 1] = le_sex.transform(X[:, 1])

le_BP = preprocessing.LabelEncoder()
le_BP.fit(['LOW', 'NORMAL', 'HIGH'])
X[:, 2] = le_BP.transform(X[:, 2])


le_Chol = preprocessing.LabelEncoder()
le_Chol.fit(['NORMAL', 'HIGH'])
X[:, 3] = le_Chol.transform(X[:, 3])

X = preprocessing.StandardScaler().fit_transform(X)

y = df['Drug']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

drug_tree = DecisionTreeClassifier(criterion='entropy')
drug_tree.fit(X_train, y_train)
pred = drug_tree.predict(X_test)

print(f'Decision Tree Accurcy Score: {metrics.accuracy_score(y_test, pred)}')
