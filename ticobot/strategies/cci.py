#!/usr/bin/python
import numpy as np

class Cci:
    '''
    Commodity Channel Index
    a is array of high prices, b is array of low prices,
    c is array of closing prices, d is the number of periods
    '''
    def __init__(self,high_prices,low_prices,close_prices,period):
        self.high_prices = high_prices[len(high_prices)-period:len(high_prices)]
        self.low_prices = low_prices[len(low_prices)-period:len(low_prices)]
        self.close_prices = close_prices[len(close_prices)-period:len(close_prices)]
        self.period = period
        self.overhigh = 100
        self.overlow = -100
    
    def prepare(self):
        a = self.high_prices
        b = self.low_prices
        c = self.close_prices
        return a,self.period,(a+b+c)/3,np.zeros(len(a)),np.zeros(len(a)),np.zeros(len(a))       
                
    def getSignal(self) -> str:
        # tp -> typical price
        # atp -> average typical price
        # md -> mean deviation
        a,d,tp,atp,md,result = self.prepare()

        for i in range(d-1,len(a)):
            atp[i] = np.sum(tp[i-(d-1):i+1])/d
            md[i] = np.sum(np.fabs(atp[i]-tp[i-(d-1):i+1]))/d
            result[i] = (tp[i]-atp[i])/(0.015*md[i])

        c1 = result[-1]

        return 'call' if c1 <= self.overlow else 'put' if c1 >= self.overhigh else 'ntr'
