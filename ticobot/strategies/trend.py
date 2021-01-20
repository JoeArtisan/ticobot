#!/usr/bin/python
import numpy as np

class Trend:
    def __init__(self,closes,period):
        self.closes = closes
        self.period = period
    
    def ema(self,prices,period):
        result = np.zeros(len(prices) - period + 1)
        result[0] = np.sum(prices[0:period]) / period
        for i in range(1, len(result)):
            result[i] = result[i - 1] + (prices[i + period-1] - result[i - 1]) * (2 / (period + 1))
        return result
        
    def getSignal(self):
        ema = self.ema(self.closes, self.period)
        c1 = self.closes[-1]
        c2 = self.closes[-2]
        c3 = self.closes[-3]
        c4 = self.closes[-4]
        e1 = ema[-1]
        e2 = ema[-2]
        e3 = ema[-3]
        e4 = ema[-4]

        signal = 'call' if e1 < c1 and e2 < c2 and e3 < c3 and e4 < c4 else 'ntr'
        signal = 'put' if e1 > c1 and e2 > c2 and e3 > c3 and e4 > c4 else signal
        return signal