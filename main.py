#!/usr/bin/python
import os,time
from win10toast import ToastNotifier as Notify
from tabulate import tabulate as tbl
from dotenv import load_dotenv

from ticobot.broker import Broker
from ticobot.strategies.fibonacci import Fibonacci as Fibo
from ticobot.strategies.pattern import Pattern 
from ticobot.strategies.trend import Trend 
 
def prepareEnv():
    load_dotenv()
    ntfy = Notify()
    user = os.getenv('user')
    passwd = os.getenv('passwd')
    mode = os.getenv('mode')
    size = int(os.getenv('candle'))
    asset = os.getenv('asset')
    market = os.getenv('market')
    bet = int(os.getenv('bet'))
    expiration = int(os.getenv('expiration'))
    slow_period = int(os.getenv('slow_period'))
    fast_period = int(os.getenv('fast_period'))

    return ntfy,user,passwd,mode,size,asset,market,bet,expiration,slow_period,fast_period

def main():
    ntfy,user,passwd,mode,size,asset,market,bet,expiration,slow_period,fast_period = prepareEnv()
    broker = Broker(user,passwd,mode)
    broker.connect()

    while True:
        start_time = time.time()
        print(f"\nTicobot: Generando el análisis para {asset} {market}")

        try:
            slow_data = broker.getCandles(asset,size,slow_period)
            fast_data = broker.getCandles(asset,size,fast_period)
            slow_candles = broker.prepareData(slow_data)
            fast_candles = broker.prepareData(fast_data)
            slow_closes = slow_candles['close']
           
            # Reconocimiento de Patrones
            pattern = Pattern(fast_candles)
            patterns_table = [
                ['Libelula Doji', pattern.dragonflyDoji(),'Hombre colgado', pattern.hangedMan()],
                ['Envolvente Alcista', pattern.bullishEngulfing(), 'Envolvente Bajista', pattern.bearishEngulfing()],
                ['Coz Alcista', pattern.cozBullish(), 'Coz Bajista', pattern.cozBearish()],
                ['Estrella de la Mañana', pattern.morningStar(), 'Estrella Vespertina', pattern.eveningStar()],
                ['Estrella de la Mañana Doji', pattern.morningStarDoji()],                
            ]
            print(tbl(patterns_table))

            # Indicador de Tendencia
            trend = Trend(slow_closes,slow_period)
            trend_signal = trend.getSignal()

            # Indicador de Retrocesos
            fibo = Fibo(slow_candles,trend_signal)
            fibo_signal = fibo.getSignal()
            
            # Evaluación final
            signal = fibo_signal

            print(f"Ticobot: Resultado del análisis")
            headers = ["Tendencia","Retroceso","Señal"]
            result_table = [[trend_signal,fibo_signal,signal]]
            print(tbl(result_table, headers))
            
            if not signal == 'ntr':
                result = [trend_signal,'ntr',fibo_signal]

                if market == 'digital':
                    broker.buyDigital(signal,bet,asset,expiration,result)
                elif market == 'binary':
                    broker.buyBinary(signal,bet,asset,expiration,result)
                ntfy.show_toast("Ticobot Notify",f"Hola, hemos realizado una compra {asset} {signal}",icon_path=None,duration=5)

                time.sleep(240)
        except Exception as error: 
            print(f'Ticobot: tenemos un problema {error}') 
        
        end_time = time.time()
        e = round(end_time - start_time,2)
        print(f'Ticobot: Tiempo de análisis {e} segundos') 

if __name__ == '__main__':
    main()
