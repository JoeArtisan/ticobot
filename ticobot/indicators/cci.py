#!/usr/bin/python

class Cci:
    '''
    Commodity Channel Index
    '''
    def __init__(self,candles,period):
        self.candles = candles
        self.period = period
        self.high = 150
        self.low = -150
        
    def calculate(self):
        pp = (self.candles['high'] + self.candles['low'] + self.candles['close']) / 3
        cci = (pp - pp.rolling(self.period, min_periods=self.period).mean()) / pp.rolling(self.period, min_periods=self.period).std()
        return float(cci.tail(1))

    def getSignal(self):
        cci = self.calculate() * 100
        print(f'Ticobot: El rango de Velocidad es de', cci)
        return 'call' if cci < self.low else 'put' if cci > self.high else 'ntr'