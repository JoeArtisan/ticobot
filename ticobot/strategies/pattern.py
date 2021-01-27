#!/usr/bin/python
from tabulate import tabulate as tbl

class Pattern:
    def __init__(self,candles):
        self.candles = candles
        
    def dragonflyDoji(self) -> bool:
        '''
        Con una sombra inferior muy larga y con una sombra superior muy corta o inexistente. Aparece tras unas tendencia bajista.
        Si esta figura se crea estando cerca de un soporte o con mucha sobreventa la fiabilidad aumenta.
        Una siguiente vela alcista, un gap al alza, o un cierre más alto al día siguiente vendría a confirmar el cambio de tendencia.
        Patrón: De cambio. Tendencia: Alcista. Fiabilidad: Media-Alta.
        '''
        c = self.candles
        c5 = c['open'][-5] > c['close'][-5] # Vela bajista
        c4 = c['open'][-4] > c['close'][-4] and c['close'] [-4]< c['close'][-5] # Vela bajista menor que anterior
        c3 =  c['open'][-3] > c['close'][-3] and c['close'][-3] < c['close'][-4]# Vela bajista menor que anterior
        doji = c['low'] [-2]< c['close'][-3] and c['low'] [-2]< c['close'][-2] and c['open'][-2] == c['close'][-2] and c['high'][-2] >= c['close'][-2]
        last = c['close'][-1] > c['close'][-2] # Vela con cierre más alto
        
        return True if c5 and c4 and c3 and doji and last else False

    def hangedMan(self) -> bool:
        '''
        Sin sombra superior pero con una sombra inferior al menos dos veces más grande que el cuerpo. Aparece tras una tendencia alcista.
        Marca, o al menos está cerca de una resistencia. Vela de confirmación que cierre por debajo del cuerpo de esta vela.
        Patrón: De cambio. Tendencia: Bajista. Fiabilidad: Alta.
        '''
        c = self.candles
        c5 = c['open'][-5] < c['close'][-5]
        c4 = c['open'][-4] < c['close'][-4] and c['close'] [-4] > c['close'][-5]
        c3 =  c['open'][-3] < c['close'][-3] and c['close'][-3] > c['close'][-4]
        hanged = c['high'][-2] == c['close'][-2] or c['low'][-2] == c['open'][-2] and c['open'][-2] > c['close'][-3] or c['open'][-2] < c['close'][-3] and c['low'][-2] < (c['close'][-2] - c['open'][-2]) * 2 or c['low'][-2] < (c['open'][-2] - c['close'][-2]) * 2
        last = c['close'][-1] < c['open'][-2] or c['close'][-1] < c['close'][-2]
        
        return True if c5 and c4 and c3 and hanged and last else False

    def bearishEngulfing(self) -> bool:
        '''
        La «pauta envolvente bajista» está compuesta por una primera vela alcista pequeña, y una segunda vela bajista más  grande que cubre todo el cuerpo de la vela anterior.
        Viene precedido de una tendencia alcista. Las sombras de ambas velas marcan máximos decrecientes. Si la pauta envolvente aparece tras un doji, la fiabilidad será muy alta.
        Si aparece una tercera vela bajista que cierra por debajo del cierre de nuestra segunda vela, se formaría lo que llamamos Tres velas exteriores bajistas, con una fiabilidad muy alta.
        Patrón: De cambio. Tendencia: Bajista. Fiabilidad: Alta.
        '''
        c = self.candles
        c6 = c['open'][-6] < c['close'][-6]
        c5 = c['open'][-5] < c['close'][-5] and c['close'] [-5] > c['close'][-6]
        c4 = c['open'][-4] < c['close'][-4] and c['close'] [-4] > c['close'][-5]
        engulfing = c['open'][-3] < c['close'][-3] and c['high'][-3] > c['close'][-3] and c['low'][-3] < c['open'][-3]
        bearish = c['open'][-2] > c['close'][-2] and c['high'][-2] > c['open'][-2] and c['low'][-2] < c['close'][-2] and  c['close'][-2] < c['close'][-3] and  c['open'][-2] > c['close'][-3]
        last = c['close'][-1] < c['close'][-2] and c['low'][-1] < c['low'][-2] < c['low'][-3]

        return True if c6 and c5 and c4 and engulfing and bearish and last else False

    def bullishEngulfing(self) -> bool:
        '''
        La «pauta envolvente alcista» está compuesta por una primera  vela bajista pequeña, y una segunda vela alcista más grande
        que cubre todo el cuerpo de la vela anterior. Viene precedido de una tendencia bajista previa. Las sombras de ambas velas
        marcan máximos crecientes. Si la pauta envolvente aparece tras un doji, la fiabilidad será muy alta.
        Además si aparece una tercera vela alcista que cierra por encima del cierre de nuestra segunda vela, se formaría lo que
        llamamos Tres velas exteriores alcistas, con una fiabilidad  muy alta. Patrón: De cambio. Tendencia: Alcista. Fiabilidad: Alta.
        '''
        c = self.candles
        c6 = c['open'][-6] > c['close'][-6]
        c5 = c['open'][-5] > c['close'][-5] and c['close'] [-5] < c['close'][-6]
        c4 = c['open'][-4] > c['close'][-4] and c['close'] [-4] < c['close'][-5]
        engulfing = c['open'][-3] > c['close'][-3] and c['high'][-3] > c['open'][-3] and c['low'][-3] < c['close'][-3]
        bullish = c['open'][-2] < c['close'][-2] and c['high'][-2] > c['close'][-2] and c['low'][-2] < c['open'][-2] and  c['close'][-2] > c['open'][-3] and  c['open'][-2] < c['close'][-3]
        last = c['close'][-1] < c['close'][-2] and c['high'][-1] > c['high'][-2] > c['high'][-3]
        
        return True if c6 and c5 and c4 and engulfing and bullish and last else False

    def cozBullish(self) -> bool:
        '''
        La «coz alcista» es una pauta compuesta por dos marubozus separados por un gap. El primer marubozu es bajista, y el segundo
        alcista. La tendencia previa no importa, y el gap que se crea servirá como soporte futuro. Esta reversión tan brusca del mercado implica
        una alta probabilidad de tendencia alcista, aunque es procedente esperar la confirmación de una tercera vela.
        Patrón: De cambio. Tendencia: Alcista. Fiabilidad: Alta.
        '''
        c = self.candles
        red = c['open'][-3] > c['close'][-3] and c['high'][-3] == c['open'][-3] and c['low'][-3] == c['close'][-3]
        green = c['open'][-2] < c['close'][-2] and c['high'][-2] == c['close'][-2] and c['low'][-2] == c['open'][-2] and c['close'][-3] == c['open'][-2]
        last = c['open'][-1] < c['close'][-1]

        return True if red and green and last else False

    def cozBearish(self) -> bool:
        '''
        La «coz bajista» es una pauta compuesta por dos marubozus separados por  un gap. El primer marubozu es alcista, y el segundo bajista. La tendencia
        previa no importa, y el gap que se crea servirá como resistencia futura. Esta reversión tan brusca del mercado implica una alta probabilidad de tendencia
        bajista, aunque es prudente esperar la confirmación de una tercera vela. Patrón: De cambio. Tendencia: bajista. Fiabilidad: Alta.
        '''
        c = self.candles
        green = c['open'][-3] > c['close'][-3] and c['high'][-3] == c['close'][-3] and c['low'][-3] == c['open'][-3]
        red = c['open'][-2] > c['close'][-2] and c['high'][-2] == c['open'][-2] and c['low'][-2] == c['close'][-2] and c['close'][-3] == c['open'][-2]
        last = c['open'][-1] < c['close'][-1]
        
        return True if red and green and last else False

    def morningStar(self) -> bool:
        '''
        Una «estrella de la mañana» está representada por una vela bajista larga, un gap con otra vela, y una tercera vela alcista. Se
        produce tras una tendencia bajista previa, con un gap a la baja entre la vela bajista larga y la segunda vela. Da igual que esta
        segunda vela sea alcista o bajista, pero será una vela corta. La tercera vela abre por encima del mínimo de la segunda vela y
        cerrará por encima de la media de la primera vela. Patrón: De cambio. Tendencia: Alcista. Fiabilidad: Alta.
        '''
        c = self.candles
        c6 = c['open'][-6] > c['close'][-6]
        c5 = c['open'][-5] > c['close'][-5] and c['close'] [-5] < c['close'][-6]
        c4 = c['open'][-4] > c['close'][-4] and c['close'] [-4] < c['close'][-5]
        red = c['high'][-4] > c['high'][-3] and c['open'][-3] < c['close'][-3] and c['high'][-3] > c['open'][-3] and c['high'][-3] > c['open'][-3]
        gap = c['high'][-2] < c['low'][-3] and c['high'][-2] > c['low'][-2]
        green = c['open'][-1] > c['low'][-2] and c['open'][-1] < c['high'][-1] and c['low'][-1] < c['open'][-1] and c['high'][-1] < c['close'][-1]
        
        return True if c6 and c5 and c4 and red and gap and green else False

    def morningStarDoji(self) -> bool:
        '''
        La «Estrella de la mañana doji» es un patrón que sigue a la estrella doji alcista. Aparece tras una tendencia bajista donde se
        crea una primera vela bajista larga, seguida por un gap a la baja con un doji, y una tercera vela alcista.
        Patrón: De cambio. Tendencia: Alcista. Fiabilidad: Alta.
        '''
        c = self.candles
        c6 = c['open'][-6] > c['close'][-6]
        c5 = c['open'][-5] > c['close'][-5] and c['close'] [-5] < c['close'][-6]
        c4 = c['open'][-4] > c['close'][-4] and c['close'] [-4] < c['close'][-5]
        red = c['high'][-4] > c['high'][-3] and c['open'][-3] < c['close'][-3] and c['high'][-3] > c['open'][-3] and c['high'][-3] > c['open'][-3]
        doji = c['high'][-2] > c['close'][-3] and c['close'][-2] > c['low'][-2] and c['open'][-2] == c['close'][-2]
        green = c['open'][-1] > c['low'][-2] and c['open'][-1] < c['high'][-1] and c['low'][-1] < c['open'][-1] and c['high'][-1] < c['close'][-1]
        
        return True if c6 and c5 and c4 and red and doji and green else False

    def eveningStar(self) -> bool:
        '''
        Una «estrella vespertina» está representada por una vela alcista larga, un gap con otra vela, y una tercera vela bajista. Se produce
        tras una tendencia alcista previa, con un gap al alza entre la vela alcista larga y la segunda vela. Da igual que esta segunda vela sea
        alcista o bajista, pero será una vela corta. La tercera vela abre por debajo del mínimo de la segunda vela y cerrará por debajo de la
        media de la primera vela. Patrón: De cambio. Tendencia: Bajista. Fiabilidad: Alta.
        '''
        c = self.candles
        c6 = c['open'][-6] < c['close'][-6]
        c5 = c['open'][-5] < c['close'][-5] and c['close'] [-5] > c['close'][-6]
        c4 = c['open'][-4] < c['close'][-4] and c['close'] [-4] > c['close'][-5]
        green = c['high'][-4] > c['high'][-3] and c['open'][-3] < c['close'][-3] and c['high'][-3] > c['open'][-3] and c['high'][-3] > c['open'][-3]
        star = c['high'][-2] < c['low'][-3] and c['high'][-2] > c['low'][-2]
        red = c['open'][-1] > c['low'][-2] and c['open'][-1] < c['high'][-1] and c['low'][-1] < c['open'][-1] and c['high'][-1] < c['close'][-1]
        
        return True if c6 and c5 and c4 and red and star and green else False
    
    def getSignal(self) -> str:
        dragonflyDoji = self.dragonflyDoji()
        bullishEngulfing = self.bullishEngulfing()
        cozBullish =  self.cozBullish()
        morningStar = self.morningStar()
        morningStarDoji = self.morningStarDoji()

        hangedMan = self.hangedMan()
        bearishEngulfing = self.bearishEngulfing()
        cozBearish = self.cozBearish()
        eveningStar = self.eveningStar()

        patterns_table = [
            ['Libelula Doji', dragonflyDoji,'Hombre colgado', hangedMan],
            ['Envolvente Alcista', bullishEngulfing, 'Envolvente Bajista', bearishEngulfing],
            ['Coz Alcista', cozBullish, 'Coz Bajista', cozBearish],
            ['Estrella de la Mañana', morningStar, 'Estrella Vespertina', eveningStar],
            ['Estrella de la Mañana Doji', morningStarDoji],                
        ]
        print(tbl(patterns_table))

        signal = 'call' if dragonflyDoji or bullishEngulfing or cozBullish or morningStar or morningStarDoji else 'ntr'
        signal = 'put' if hangedMan or bearishEngulfing or cozBearish or eveningStar else signal

        return signal