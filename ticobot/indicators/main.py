#!/usr/bin/python
import pandas as pd

from ticobot.indicators.rsi import Rsi
from ticobot.indicators.cci import Cci
from ticobot.indicators.ema import Ema
from ticobot.indicators.atr import Atr
from ticobot.indicators.fibonacci import Fibonacci as Fibo
from ticobot.indicators.stochastic import Stochastic as Stoch
from ticobot.indicators.vortex import Vortex as Vtx

class Indicators:
    def __init__(self,candles):
        self.candles = candles
    
    def atr(self,df,n):
        atr = Atr(df,n)
        return atr.getSignal()
        
    def ema(self,df,n):
        ema = Ema(df,n)
        return ema.getSignal()
    
    def cci(self,df,n):
        cci = Cci(df,n)
        return cci.getSignal()
        
    def fibo(self,df,ema):
        fibo = Fibo(df)
        return fibo.getSignal(ema)

    def rsi(self,df,n):
        rsi = Rsi(df,n)
        return rsi.getSignal()
    
    def stoch(self,df):
        stoch = Stoch(df)
        return stoch.getSignal()

    def vtx(self,df,n):
        vtx = Vtx(df,n)
        return vtx.getSignal()
    
    def prepare(self):
        df = pd.DataFrame(self.candles)
        return df.tail(7),df.tail(14),df.tail(100)

    def resume(self):
        df7,df14,df100 = self.prepare()

        # Indicador de Volatilidad
        atr = self.atr(df14,14)
        # Indicador de Tendencia
        ema = self.ema(df100,100)
        # Indicador de Velocidad
        cci = self.cci(df14,14)
        # Indicador de Fuerza
        rsi = self.rsi(df7,7)
        # Indicador de Retrocesos
        fibo = self.fibo(df100,ema)
        
        # Indicador de Oscilación
        stoch = 'ntr'#self.stoch(df14)
        # Indicador de Impulso
        vtx = self.vtx(df14,14)

        return atr,ema,fibo,cci,rsi,stoch,vtx,'ntr'