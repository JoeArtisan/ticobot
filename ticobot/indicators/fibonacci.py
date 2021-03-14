#!/usr/bin/python
import numpy as np

class Fibonacci:
    def __init__(self,candles):
        self.candles = candles
        self.close = self.candles['close'].tail(3).values

    def getLevel(self, price_max, diff, level):
        return price_max - level * diff

    def getMinMax(self):
        return np.amax(self.candles['high']), np.amin(self.candles['low'])
    
    def getLevels(self,price,diff):
        lvl38 = self.getLevel(price, diff, 0.382)
        lvl61 = self.getLevel(price, diff, 0.618)
        return lvl38,lvl61
    
    def hasCrossedUnder(self,lvl):
        return self.close[1] < lvl and self.close[2] >= lvl and self.close[3] < lvl

    def hasCrossedAbove(self,lvl):
        return self.close[1] > lvl and self.close[2] <= lvl and self.close[3] > lvl

    def prepare(self):
        price_max, price_min = self.getMinMax()
        lvl38,lvl61 = self.getLevels(price_max, price_max - price_min)
        return self.hasCrossedUnder(lvl38),self.hasCrossedAbove(lvl61)

    def getSignal(self,trend):
        lvl38,lvl61 = self.prepare()
        return trend if trend == 'call' and lvl38 or trend == 'put' and lvl61 else 'ntr'