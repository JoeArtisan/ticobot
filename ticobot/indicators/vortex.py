#!/usr/bin/python
import pandas as pd

class Vortex:
    '''
    Indicador Técnico Vortex
    Consiste de dos osciladores que capturan el movimiento de tendencia positiva y de tendencia negativa. 
    Un cruce por encima o por debajo de un nivel particular puede señalar el inicio de una tendencia y
    estos niveles pueden usarse para afirmar la dirección de la tendencia.
    '''
    def __init__(self,df,n):
        self.df = df
        self.n = n
        self.high = 1.1
        self.low = -0.57
    
    def calcTR(self):
        df = self.df
        tr = [0]
        i = 0
        while i < df.index[-1]:
            mx = max(df.loc[i + 1, 'high'], df.loc[i, 'close'])
            mn = min(df.loc[i + 1, 'low'], df.loc[i, 'close'])
            r = mx - mn
            tr.append(r)
            i = i + 1
        return tr
    
    def calcVM(self):
        df = self.df
        vm = [0]
        i = 0
        while i < df.index[-1]:
            a1 = abs(df.loc[i + 1, 'high'] - df.loc[i, 'low'])
            a2 = abs(df.loc[i + 1, 'low'] - df.loc[i, 'high'])
            vm.append(a1 - a2)
            i = i + 1
        return vm

    def prepare(self):
        return self.n,self.calcTR(),self.calcVM()

    def calculate(self):
        n,tr,vm = self.prepare()
        v = pd.Series(vm).rolling(n).sum()
        t = pd.Series(tr).rolling(n).sum()
        print(v,t)
        return (v / t)
            
    def getSignal(self):
        #vtx = self.calculate()
        #print('Vortex Indicator:',vtx)
        #return 'ntr'
        df = self.df
        n = self.n

        TR = [0]
        VM = [0]
        for i in range(df.index[0],df.index[-1]):
            t = max(df.loc[i + 1, 'high'], df.loc[i, 'close']) - min(df.loc[i + 1, 'low'], df.loc[i, 'close'])
            v = abs(df.loc[i + 1, 'high'] - df.loc[i, 'low']) - abs(df.loc[i + 1, 'low'] - df.loc[i, 'high'])
            TR.append(t)
            VM.append(v)

        v = pd.Series(VM).rolling(n).sum()
        t = pd.Series(TR).rolling(n).sum()
        vi = pd.Series(v / t, name='Vortex_' + str(n))
        vtx = round(vi.loc[v.index[-1]],3)
        print('Ticobot: El rango de redireccionamiento es',vtx)

        return 'call' if vtx > self.high else 'put' if vtx < self.low else 'ntr'