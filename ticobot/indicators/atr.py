#!/usr/bin/python
import pandas as pd

class Atr:
    '''
    Average True Range
    '''
    def __init__(self,candles,period):
        self.candles = candles
        self.period = period
        self.high = 0.12
        self.low = 0.040

    def calculate(self):
        df = self.candles
        n = self.period
        trl = [0]
        for i in range(df.index[0],df.index[-1]):
            t = max(df.loc[i + 1, 'high'], df.loc[i, 'close']) - min(df.loc[i + 1, 'low'], df.loc[i, 'close'])
            trl.append(t)

        trs = pd.Series(trl).rolling(n).sum()
        atr = trs.loc[trs.index[-1]]
        return float(atr)
            
    def getSignal(self):
        atr = self.calculate()
        atr = round(atr,5)
        print(f'Ticobot: El rango de volatilidad es de',atr)
        return True if atr <= self.high and atr >= self.low else False