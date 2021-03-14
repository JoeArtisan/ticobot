#!/usr/bin/python
import numpy as np
import pandas as pd

class Momentum:
    '''
    Indicador Momentum
    Cuando los precios dan un nuevo máximo y el impulso máximo es menor que el anterior,
    la divergencia de los osos da una fuerte señal de venta. 
    '''
    def __init__(self,candles,period):
        self.candles = candles
        self.closes = candles['close']
        self.period = period

    def calculate(self):
        return self.closes.diff(self.period)
    
    def prepare(self):
        return self.calculate(),0,0
        
    def getSignal(self):
        mmt,up,dw = self.prepare()
        return 'ntr'