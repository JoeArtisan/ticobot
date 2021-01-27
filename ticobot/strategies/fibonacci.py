#!/usr/bin/python
import numpy as np
from tabulate import tabulate as tbl

class Fibonacci:
    def __init__(self,candles,trend):
        self.candles = candles
        self.trend = trend

    def getLevel(self, price_max, diff, level) -> float:
        return price_max - level * diff

    def getMinMax(self):
        return np.amax(self.candles['high']), np.amin(self.candles['low'])
    
    def getLevels(self, price,diff):
        #15%, 23,6%, 38,2%, 50%, 61,8%, 88% y 100%.
        lvl15 = self.getLevel(price, diff, 0.15)
        lvl23 = self.getLevel(price, diff, 0.236)
        lvl38 = self.getLevel(price, diff, 0.382)
        lvl50 = self.getLevel(price, diff, 0.50)
        lvl61 = self.getLevel(price, diff, 0.618)
        lvl88 = self.getLevel(price, diff, 0.88)
        return lvl15,lvl23,lvl38,lvl50,lvl61,lvl88

    def prepare(self):
        price_max, price_min = self.getMinMax()
        diff = price_max - price_min
        c3 = self.candles['close'][-3]
        c2 = self.candles['close'][-2]
        c1 = self.candles['close'][-1]

        lvl15,lvl23,lvl38,lvl50,lvl61,lvl88 = self.getLevels(price_max, diff)

        return price_max,price_min,lvl38,lvl61,c1,c2,c3

    
    def hasCrossedLevel(self,lvl,c1,c2,c3)-> bool:
        # Validamos el cruce por arriba o por abajo
        isCrossed = c3 > lvl and c2 <= lvl and c1 > lvl or c3 < lvl and c2 >= lvl and c1 < lvl
        return True if isCrossed else False
   
    def getSignal(self) -> str:
        price_max,price_min,level38,level61,c1,c2,c3 = self.prepare()

        lvl38 = self.hasCrossedLevel(level38,c1,c2,c3)
        lvl61 = self.hasCrossedLevel(level61,c1,c2,c3)

        headers = ["ANT","ACT","MIN","MAX","LVL38","LVL61","ZLVL38","ZLVL61"]
        table = [[c2,c1,price_min,price_max,level38,level61,lvl38,lvl61]]
        print(tbl(table, headers, tablefmt="plain"))

        if self.trend == 'call':
            signal = 'call' if lvl38 else 'ntr'
        elif self.trend == 'put':
            signal = 'put' if lvl61 else 'ntr'
        else:
            signal = 'ntr'
            
        return signal
