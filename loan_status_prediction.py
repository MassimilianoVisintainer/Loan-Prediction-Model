# -*- coding: utf-8 -*-
"""Loan Status Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KdBAtKUhTugwKr7DZyQWjwgve8tK8XN4

Import dependecies
"""

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Import the data and processing"""

loan_dataset = pd.read_csv('/content/train_u6lujuX_CVtuZ9i (1).csv')

loan_dataset.head()

loan_dataset.shape

loan_dataset

np.sum(loan_dataset.isnull())

loan_dataset = loan_dataset.dropna()
print(np.sum(loan_dataset.isnull()))

# Plot loan compared to graduated
sns.countplot(x='Education', hue='Loan_Status', data=loan_dataset)

# Plot loan status compared to married or not
sns.countplot(x='Married', hue='Loan_Status', data=loan_dataset)

# Processing string into numerical values
loan_dataset.replace({"Loan_Status":{'Y': 1, 'N':0}, "Self_Employed":{'Yes':1, 'No':0}, "Gender":{'Male': 1, 'Female': 0}, "Married": {'No': 0, 'Yes':1}, "Education": {'Graduate':1, 'Not Graduate' : 0}, 'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2} },inplace=True)
loan_dataset = loan_dataset.replace(to_replace='3+', value=4)
print(loan_dataset.head())

"""Split data and label"""

X = loan_dataset.drop(columns=['Loan_ID', 'Loan_Status'])
Y = loan_dataset['Loan_Status']
print(X)
print(Y)

"""Split Train and Test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.1, stratify=Y, random_state=2)
print(X.shape, X_train.shape, X_test.shape  )

"""Train your Model"""

model = svm.SVC(kernel='linear')

model.fit(X_train, Y_train)

# Accurancy of your train

X_train_prediction = model.predict(X_train)
X_train_accurancy = accuracy_score(X_train_prediction, Y_train)
print('Accurancy of train data : ', X_train_accurancy)

# Accurancy of test data
X_test_prediction = model.predict(X_test)
X_test_accurancy = accuracy_score(X_test_prediction,Y_test)
print('Accurancy of test data : ', X_test_accurancy)