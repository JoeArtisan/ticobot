#!/usr/bin/python

class Ema:
    def __init__(self,candles,period):
        self.candles = candles
        self.period = period
    
    def calculate(self):
        ema = self.candles['close'].ewm(span=self.period, min_periods=self.period).mean()
        return float(ema.tail(1))
    
    def prepare(self):
        return self.calculate(),float(self.candles['close'].tail(1))
      
    def getSignal(self):
        e,c = self.prepare()
        return 'call' if c > e else 'put' if c < e else 'ntr'