import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm

print("=================== Naive Bayes =======================")
dataset = pd.read_excel(r'Cleaned Data\Sentiment\features_cv_s21.xlsx')

X = dataset.iloc[1:, 1:231].values
y = dataset.iloc[1:, 232].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
naive_bayes_classifier = MultinomialNB()
naive_bayes_classifier.fit(X_train,y_train)
y_pred = naive_bayes_classifier.predict(X_test)
print("---------------- Classification Report -----------------------")
print(metrics.classification_report(y_test, y_pred,target_names=['Negative','Positive']))
print("----------------- Confusion Matrix ----------------------------")
print(metrics.confusion_matrix(y_test,y_pred))
print("=============== Decision Tree ===========================")

DTclassifier = DecisionTreeClassifier()
DTclassifier.fit(X_train, y_train)
y_predict = DTclassifier.predict(X_test)

print("---------------- Classification Report -----------------------")
print(metrics.classification_report(y_test, y_predict, target_names=['Negative','Positive']))
print("----------------- Confusion Matrix ----------------------------")
print(metrics.confusion_matrix(y_test,y_predict, labels=DTclassifier.classes_))

print("=============== SVM ===========================")
clf = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)
print("---------------- Classification Report -----------------------")
print(metrics.classification_report(y_test, y_pred, target_names=['Negative','Positive']))
print("----------------- Confusion Matrix ----------------------------")
print(metrics.confusion_matrix(y_test,y_pred, labels=clf.classes_))
