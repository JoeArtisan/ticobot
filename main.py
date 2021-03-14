#!/usr/bin/python
import time
from tabulate import tabulate as tbl
from ticobot.broker import Broker
from ticobot.env import Env
from ticobot.notify import Notify
from ticobot.indicators.main import Indicators
 
def worker(broker,size,asset,market,bet,expiration):
    candles = broker.getCandles(asset,size,200)
    indicator = Indicators(candles)
    atr,ema,fibo,cci,rsi,stoch,vtx,nt = indicator.resume()

    if atr:
        # Regla #1: Cuando coincide la tendencia y el retroceso
        signal = fibo if not fibo == nt and fibo == ema else nt

        # Regla #2: Cuando coincide la tendencia y el Impulso
        signal = vtx if signal == nt and not vtx == nt and vtx == ema else signal
        
        # Regla #3: Cuando coinciden la fuerza y la velocidad
        signal = rsi if signal == nt and not rsi == nt and rsi == cci and cci == ema else signal
        
        # Es Stoch si: es diferente de neutro y la señal anterior tambien. igual a la ema, igual al cci e igual al rsi
        #signal = stoch if signal == 'ntr' and not stoch == 'ntr' and stoch == ema and stoch == cci and stoch == rsi else signal
        
        # Presentación
        headers = ["Tipo","Mercado","Expiración","Apuesta","Tendencia","Velocidad","Fuerza","Retroceso","Oscilador","Impulso","Resumen"]
        packet = [market,asset,expiration,bet,ema,cci,rsi,fibo,stoch,vtx,signal]
        result_table = [packet]
        print(tbl(result_table,headers))
    
        # Ejecución
        if not signal == 'ntr':
            # Compramos 
            broker.buy(packet)
            # Notificamos sobre el resultados a todas las partes
            ntfy = Notify(candles,packet)
            ntfy.send()
            # Esperamos 4 minutos o 8 velas antes de volver a iniciar
            time.sleep(240)
    else:
        print(f'Ticobot: La volatilidad del mercado {asset} no es aceptable') 


def main():
    # Preparación de Datos
    env = Env()
    user,passwd,mode,size,market,bet,expiration,assets = env.prepare()
    # Conexión con el broker
    broker = Broker(user,passwd,mode)
    broker.connect()
    # Iniciamos el ciclo
    while True:
        try:
            # Realizamos un analisis por cada mercado
            for i in range(0,len(assets)):
                start_time = time.time()
                asset = assets[i]
                print(f"\nTicobot: Estamos analisando {asset}")
                # Iniciamos el proceso de análisis
                worker(broker,size,asset,market,bet,expiration)
                print(f'Ticobot: Tiempo estimado {round(time.time() - start_time,2)} segundos') 

        except Exception as error: 
            print(f'Ticobot: tenemos un problema {error}') 
    
if __name__ == '__main__':
    main()