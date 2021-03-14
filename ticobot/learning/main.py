#!/usr/bin/python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

from sklearn.neural_network import MLPClassifier


class Learning:
    def __init__(self,asset):
        self.dataset = pd.read_csv("data.csv")
        self.asset = asset
    
    def pct(self, df):
        return df.pct_change(fill_method ='ffill')
    
    def target(self,t):
        for i in range(len(t)):
            t[i] = 1 if float(t[i]) > 0 else 0
        return t

    def prepare(self):
        df = self.dataset
        pct = self.pct(df["close"])
        target = self.target(pct)
        df = df.dropna()
        return df.values,target
    
    def scalar(self,X_train,X_test):
        scal = StandardScaler()
        xtrain = scal.fit_transform(X_train)
        xtest = scal.transform(X_test)
        return xtrain, xtest
    
    def separate(self,x,y):
        xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, stratify=y, random_state=1)
        xtrain, xtest = self.scalar(xtrain,xtest)
        return xtrain,xtest,ytrain,ytest
        
    def plot(self,x,n):
        plt.plot(x, label=n, color='red')
        plt.axis('equal')
        plt.legend()  
        plt.show() 
    
    def linearRegression(self,xtr, xts, ytr, yts):
        model = LinearRegression()
        model.fit(xtr, ytr)
        ypd = model.predict(xts)
        predictions = pd.DataFrame(ypd)
        print(ypd,predictions)
        #self.plot(predictions,'Linear Regression')
        precision = model.score(yts, ypd)
        print(f'Ticobot IA: La precisión de la predicción de la Regresión Lineal Simple es: {precision}')

        #mtrz = confusion_matrix(yts, ypd)
        #print(f'Ticobot IA: La matriz de confusión de la Regresión Lineal Simple es: {mtrz}')

        #accuracy = accuracy_score(yts, ypd)
        #print(f'Ticobot IA: La exactitud de la Regresión Lineal Simple es: {accuracy}')

        #sensitivity  = recall_score(yts, ypd)
        #print(f'Ticobot IA: La sensibilidad de la Regresión Lineal Simple es: {sensitivity}')

        #f1  = f1_score(yts, ypd)
        #print(f'Ticobot IA: El puntaje F1 de la Regresión Lineal Simple es: {f1}')

        #roc_auc  = roc_auc_score(yts, ypd)
        #print(f'Ticobot IA: La curva ROC-AUC de la Regresión Lineal Simple es: {roc_auc}')

        return predictions
    
    def logisticRegression(self,xtr, xts, ytr, yts):
        model = LogisticRegression()
        model.fit(xtr, ytr)
        predictions = pd.DataFrame(model.predict(xts))
        self.plot(predictions,'Logistic Regression')
    
    def estimate(self):
        # Preparación de los muestras
        x,y = self.prepare()
        # Separación de muestras
        xtr, xts, ytr, yts = self.separate(x,y)
        # Entrenamiento
        linear_regression_predictions = self.linearRegression(xtr, xts, ytr, yts)

        return 'ntr'
        
learn = Learning('NZDUSD-OTC')
result = learn.estimate()    

        




