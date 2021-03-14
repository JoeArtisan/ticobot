#!/usr/bin/python
import pandas as pd

class Rsi:
    def __init__(self,candles,period):
        self.candles = candles
        self.period = period  

    def calculate(self):
        df =  self.candles
        n = self.period
        UpI = [0]
        DoI = [0]
        
        for i in range(df.index[0],df.index[-1]):
            UpMove = df.loc[i + 1, 'high'] - df.loc[i, 'high']
            DoMove = df.loc[i, 'low'] - df.loc[i + 1, 'low']
            if UpMove > DoMove and UpMove > 0:
                UpD = UpMove
            else:
                UpD = 0
            UpI.append(UpD)
            if DoMove > UpMove and DoMove > 0:
                DoD = DoMove
            else:
                DoD = 0
            DoI.append(DoD)

        UpI = pd.Series(UpI)
        DoI = pd.Series(DoI)
        PosDI = pd.Series(UpI.ewm(span=n, min_periods=n).mean())
        NegDI = pd.Series(DoI.ewm(span=n, min_periods=n).mean())
        rsi = PosDI / (PosDI + NegDI)
        return rsi
    
    def getSignal(self):
        rsi = float(self.calculate().tail(1) * 100)
        print(f'Ticobot: El rango de Fuerza es de', rsi)
        return 'call' if rsi < 20 else 'put' if rsi > 80 else 'ntr'