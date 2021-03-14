#!/usr/bin/python
import numpy as np
import pandas as pd

class Stochastic:
    '''
    Stochastic oscillator
    '''
    def __init__(self,df):
        self.df = df
        self.dp = 14
    
    def calculate(self):
        dfk = self.df.tail(3)
        k = (dfk['close'] - dfk['low']) / (dfk['high'] - dfk['low'])
        kk = pd.Series((self.df['close'] - self.df['low']) / (self.df['high'] - self.df['low']), name='SO%kk')
        d = kk.ewm(span=self.dp, min_periods=self.dp).mean()
        return k,d

    def getSignal(self):
        k,d = self.calculate()
        #k = float(k.tail(1))
        d = float(d.tail(1))
        print(k,d)
        '''k1 = k[-1]
        k2 = k[-2]
        d1 = d[-1]'''

        #signal = 'call' if k1 > self.oversold and k1 > d1 and k2 < self.oversold else 'ntr'
        #signal = 'put' if signal == 'ntr' and k1 < self.overbought and k1 < d1 and k2 > self.overbought else signal

        return 'ntr' #signal