#!/usr/bin/python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

class Learning:
    def __init__(self,asset):
        self.candles = pd.read_csv(r"C:\Users\JoeAlv\Desktop\TicoTraderBot\ticobot\learning\data\market.csv") 
        self.test = pd.read_csv(r"C:\Users\JoeAlv\Desktop\TicoTraderBot\ticobot\learning\data\market2.csv") 
        self.asset = asset
    
    def prepare(self):
        data = self.candles
        print('Información del DataSet:')
        print(data.keys())
        return data
    
    def compute(self,c):
        return 1 if c > 0 else -1
            
    def plot(self,df):
        # Getting the data and making it usable
        df.drop(['Volume'], axis='columns', inplace=True)
        #df = df.to_numpy()

        # Splitting the data into test and train sets
        x = df #.reshape((-1,1))
        y = df["Close"]
        x = x.to_numpy()
        y = y.to_numpy()
        
        data_X_train, data_X_test, data_Y_train, data_Y_test = train_test_split(x, y, test_size=0.2)
    
        #lr = linear_model.LinearRegression()
        #lr.fit(x_train,y_train)
        #y_pred = lr.predict(x_test)

        plt.plot(y)
        plt.title('Regresión Lineal')
        plt.xlabel('Precio de Cierre')
        plt.ylabel('Media de Cierre')
        plt.show()

    def training(self):
        print()
        df = self.prepare()
        self.plot(df)


learn = Learning('NZDUSD-OTC')
learn.training()    

        




