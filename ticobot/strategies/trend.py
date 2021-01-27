#!/usr/bin/python
import numpy as np

class Trend:
    def __init__(self,closes,period):
        self.closes = closes
        self.period = period
        self.accepted = 2
    
    def ema(self,prices,period):
        result = np.zeros(len(prices) - period + 1)
        result[0] = np.sum(prices[0:period]) / period
        
        for i in range(1, len(result)):
            result[i] = result[i - 1] + (prices[i + period-1] - result[i - 1]) * (2 / (period + 1))
        return result
    
    def prepare(self):
        return self.ema(self.closes, self.period),0,0
        
    def getSignal(self) -> str:
        ema,up,dw = self.prepare()
        for i in range(0,len(ema)-1):
            if ema[i] < self.closes[i]:
                up += 1
            elif ema[i] > self.closes[i]:
                dw += 1

        return 'call' if up > dw and up >= self.accepted else 'put' if up < dw and dw >= self.accepted else 'ntr'
