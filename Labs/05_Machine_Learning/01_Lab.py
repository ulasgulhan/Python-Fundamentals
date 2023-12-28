
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score
from math import floor


df = pd.read_csv('Data/FuelConsumption.csv')

cdf = df[['ENGINESIZE','CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]

# Split Data to Train & Test Sets

msk = np.random.rand(len(df)) <= 0.8
train = cdf[msk]
test = cdf[~msk]

print(f'Train Set Shape: {train.shape}')
print(f'Test Set Shape: {test.shape}')


# regression = linear_model.LinearRegression()
# train_x = np.asarray(train[['ENGINESIZE']])
# train_y = np.asarray(train[['CO2EMISSIONS']])
# regression.fit(train_x, train_y)
# print('Coefficent: %.2f' % regression.coef_[0][0])
# print('Intercept: %.2f' % regression.intercept_[0])

# x = float(input(f'Please type into engine size: '))
# y = regression.intercept_[0] + regression.coef_[0][0] * x
# print(f'Carbon Emmissions Value: {floor(y)}')
#
#
# plt.scatter(train['ENGINESIZE'], train['CO2EMISSIONS'], color='b')
# plt.plot(train_x, regression.coef_[0][0] * train_x + regression.intercept_[0], c='r')
# plt.title('Relation About Between The Engine Size and Co2', color='r')
# plt.xlabel('Engine', color='r')
# plt.ylabel('Emission', color='r')
# plt.show()


# test_x = np.asarray(train[['ENGINESIZE']])
# test_y = np.asarray(train[['CO2EMISSIONS']])
# test_pred_ = regression.predict(test_x)
# print(test_pred_)
#
# print('r2 Score: %.2f' % r2_score(test_pred_, test_y))


# Multiple yapılacak

regression = linear_model.LinearRegression()
train_x = np.asarray(train[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB']])
train_y = np.asarray(train[['CO2EMISSIONS']])
regression.fit(train_x, train_y)
print('Coefficent: ', regression.coef_)
print('Intercept: ', regression.intercept_)

x = float(input(f'Please type into engine size: '))
y = regression.intercept_[0] + regression.coef_[0][0] * x
print(f'Carbon Emmissions Value: {floor(y)}')
