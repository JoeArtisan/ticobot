#!/usr/bin/python
import numpy as np
import pandas as pd

class Roc:
    '''
    Rate of Change
    '''
    def __init__(self,candles,period):
        self.candles = candles
        self.closes = candles['close']
        self.period = period

    def calculate(self):
        return (self.closes.diff(self.period -1 ) / self.closes.shift(self.period -1 ))
    
    def prepare(self):
        return self.calculate(),0,0
        
    def getSignal(self):
        roc,up,dw = self.prepare()
        return 'ntr'