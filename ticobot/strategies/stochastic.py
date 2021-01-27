#!/usr/bin/python
import numpy as np

class Stochastic:
    '''
    Stochastic oscillator
    a is an array of high prices, b is array of low prices,
    c is an array of closing prices, d is the look back period
    e is number of periods for %K SMA, f is the number of
    periods for %D SMA
    '''
    def __init__(self,high_prices,low_prices,close_prices,smoothing,period_k,period_d):
        self.high_prices = high_prices
        self.low_prices = low_prices
        self.close_prices = close_prices
        self.smoothing = smoothing
        self.period_k = period_k
        self.period_d = period_d
        self.overbought = 80
        self.oversold = 20
    
    def prepare(self):
        a = self.high_prices
        b = self.low_prices
        c = self.close_prices
        d = self.smoothing
        e = self.period_k
        f = self.period_d

        return a,b,c,d,e,f,np.zeros(len(a))
    
    # Simple Moving Average
    # a is an array of prices, b is a period for averaging
    def sma(self,a,b):
        result = np.zeros(len(a)-b+1)
        for i in range(len(a)-b+1):
            sm = np.sum(a[i:i+b])
            result[i] = sm / b
        return result
                
    # a is an array of high prices, b is array of low prices,
    # c is an array of closing prices, d is the look back period
    # e is number of periods for %K SMA, f is the number of
    # periods for %D SMA
    def getSignal(self) -> str:
        a,b,c,d,e,f = self.prepare()

        t = np.zeros(len(a))
        for i in range(d-1,len(a)):
            t[i] = ((c[i]-np.amin(b[i-(d-1):i+1]))/(np.amax(a[i-(d-1):i+1])-np.amin(b[i-(d-1):i+1])))*100

        t = t[d-1:]
        pk = self.sma(t,e)
        pd = self.sma(pk,f)
        print(pk,pd)

        return 'ntr' #if pd <= self.oversold and pk <= self.oversold else 'put' if pd >= self.overbought and pk >= self.overbought else 'ntr'
