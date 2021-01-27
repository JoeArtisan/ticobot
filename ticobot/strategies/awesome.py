#!/usr/bin/python
import numpy as np
import pandas as pd
from tapy import Indicators
from tabulate import tabulate as tbl


class Awesome:
    def __init__(self,candles,period):
        self.candles = candles
        self.period = period
    
    def prepareData(self):
        candles = self.candles
        data = { 'Open': np.array([]), 'High': np.array([]), 'Low': np.array([]), 'Close': np.array([]), 'Volume': np.array([]), 'Date': np.array([]) }
        for i in candles:
            if candles[i]["open"] > 0 and candles[i]["max"] > 0 and candles[i]["min"] > 0 and candles[i]["close"] > 0 and candles[i]["volume"] > 0:
                data["Open"] = np.append(data["Open"],candles[i]["open"] )
                data["High"] = np.append(data["High"],candles[i]["max"] )
                data["Low"] = np.append(data["Low"],candles[i]["min"] )
                data["Close"] = np.append(data["Close"],candles[i]["close"] )
                data["Volume"] = np.append(data["Volume"],candles[i]["volume"] )
        return data
                
    def getSignal(self) -> str:
        data = self.prepareData()
        df = pd.DataFrame(data) 
        #indicators = Indicators(df)
        #indicators.accelerator_oscillator(column_name='AC')
        #indicators.sma()
        #df = indicators.df
        print((df.tail()))
        return 'ntr'
