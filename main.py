#!/usr/bin/python
import os,time
from win10toast import ToastNotifier as Notify
from tabulate import tabulate as tbl
from dotenv import load_dotenv

import matplotlib.pyplot as plt
from matplotlib import cm
import mplfinance as mpf
import numpy as np
import pandas as pd

from ticobot.broker import Broker
from ticobot.strategies.fibonacci import Fibonacci as Fibo
from ticobot.strategies.trend import Trend
from ticobot.strategies.pattern import Pattern
from ticobot.strategies.rsi import Rsi
from ticobot.strategies.cci import Cci
from ticobot.strategies.atr import Atr
from ticobot.strategies.stochastic import Stochastic as Stoch
 
def prepareEnv():
    load_dotenv()
    ntfy = Notify()
    user = os.getenv('user')
    passwd = os.getenv('passwd')
    mode = os.getenv('mode')
    size = int(os.getenv('candle'))
    market = os.getenv('market')
    bet = int(os.getenv('bet'))
    expiration = int(os.getenv('expiration'))
    period = int(os.getenv('period'))
    assets = os.getenv('assets')
    assets = eval(assets)

    return ntfy,user,passwd,mode,size,market,bet,expiration,period,assets

def saveData(candles,asset):
    #path = os.getcwd()
    df = pd.DataFrame(candles) 
    dr = r'C:\Users\JoeAlv\Desktop\TicoTraderBot\ticobot\learning\data\market.csv'
    df.to_csv(dr, index = False, header=True)


def worker(broker,ntfy,size,asset,market,bet,expiration,period):
    data = broker.getCandles(asset,size,period)
    candles = broker.prepareData(data)
    candlesCsv = broker.prepareDataCsv(data)
    closes = candles['close']
    highs = candles['high']
    lows = candles['low']

    # Reconocimiento de Patrones
    #pattern = Pattern(candles)
    pattern_signal = 'ntr'#pattern.getSignal()

    # Indicador de tendencia
    trend = Trend(closes,period)
    trend_signal = trend.getSignal()

    # Indicador de confianza
    trust_signal = broker.getTrustSignal(asset)

    # Indicador de Retrocesos
    fibo = Fibo(candles,trend_signal)
    fibo_signal = fibo.getSignal()

    # Indicador de velocidad
    cci = Cci(highs,lows,closes,28)
    cci_signal = cci.getSignal()

    # Indicador de fuerza
    rsi = Rsi(closes,7,80,20)
    rsi_signal = rsi.getSignal()

    # Indicador de oscilación
    #stoch = Stoch(highs,lows,closes,3,3,14)
    stoch_signal = 'ntr'#stoch.getSignal()

    # Indicador de volatilidad
    #atr = Atr(highs,lows,closes,14)
    #atr_signal = atr.getSignal()

    std = np.std(closes)
    mean = np.mean(closes)
    median = np.median(closes)
    ptp = np.ptp(closes)

    print('Desviación:',std,'Media:',mean,'Mediana:',median,'Rango:',ptp)
    
    # Evaluación final
    signal = fibo_signal if fibo_signal == trend_signal or fibo_signal == pattern_signal or fibo_signal == trust_signal else 'ntr'
    signal = cci_signal if not signal == 'ntr' and cci_signal == rsi_signal and not cci_signal == 'ntr' else signal


    print(f"Ticobot: Le mostramos a continuación el resultado del análisis")
    headers = ["Tendencia","Confianza","Retroceso","Oscilador","Velocidad","Fuerza","Patron","Resumen"]
    result_table = [[trend_signal,trust_signal,fibo_signal,stoch_signal,cci_signal,rsi_signal,pattern_signal,signal]]
    print(tbl(result_table, headers))
    
    # Data to Machine Learning
    saveData(candlesCsv,asset)

    if not signal == 'ntr':
        result = [trend_signal,'ntr',fibo_signal]
        if market == 'digital':
            broker.buyDigital(signal,bet,asset,expiration,result)
        elif market == 'binary':
            broker.buyBinary(signal,bet,asset,expiration,result)
        ntfy.show_toast("Ticobot Notify",f"Hola, hemos realizado una compra {asset} {signal}",icon_path=None,duration=5)

        time.sleep(240)

def main():
    ntfy,user,passwd,mode,size,market,bet,expiration,period,assets = prepareEnv()
    broker = Broker(user,passwd,mode)
    broker.connect()

    while True:
        try:
            for i in range(0,len(assets)):
                start_time = time.time()
                asset = assets[i]
                print(f"\nTicobot: Generando el análisis para {asset} {market}")
                worker(broker,ntfy,size,asset,market,bet,expiration,period)

                end_time = time.time()
                e = round(end_time - start_time,2)
                print(f'Ticobot: Tiempo de análisis {e} segundos') 
        except Exception as error: 
            print(f'Ticobot: tenemos un problema {error}') 
    
if __name__ == '__main__':
    main()
