#!/usr/bin/python

class Mhi:
    def __init__(self,candles):
        self.candles = candles
        
    def getSignal(self):
        candles = self.candles
        action = 'ntr'
        invest_call = False
        invest_put = False

        for i in range(0,len(candles)-1):
            _open = candles[i]['open']
            _close = candles[i]['close']
            candles[i] = 'g' if _open < _close else 'r' if _open > _close else 'n'

        cores1 = candles[2] + ' ' + candles[3] + ' ' + candles[4]
        cores2 = candles[7] + ' ' + candles[8] + ' ' + candles[9]
        
        # Si la cantidad de las primeras velas crecientes es mayor a las decrecientes y no hay neutrales
        if cores1.count('g') > cores1.count('r') and cores1.count('n') == 0:
            # Puede invertir a la alza si las siguientes dos velas no son decrecientes
            invest_call = True if candles[5] != 'r' and candles[6] != 'r' else invest_call
            
        # Si la cantidad de las primeras velas decrecientes es mayor a las crecientes y no hay neutrales
        if cores1.count('r') > cores1.count('g') and cores1.count('n') == 0:
            # Puede invertir a la baja si las siguientes dos velas no son crecientes
            invest_put = True if candles[5] != 'g' and candles[6] != 'g' else invest_put
            
        # Si la cantidad de las ultimas velas crecientes es mayor a las decrecientes y no hay neutrales
        if 3 > cores2.count('g') > cores2.count('r') and cores2.count('n') == 0:
            action = 'put' if invest_put and not invest_call else action
        # Si la cantidad de las ultimas velas decrecientes es mayor a las crecientes y no hay neutrales
        if 3 > cores2.count('r') > cores2.count('g') and cores2.count('n') == 0:
            action = 'call' if invest_call and not invest_put else action

        return action if action else 'ntr'
