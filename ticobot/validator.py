#!/usr/bin/python
from tabulate import tabulate as tbl

class Validator:
    def __init__(self,trend,trust,fibo,pattern,stoch,rsi,cci):
        self.trend = trend
        self.trust = trust
        self.fibo = fibo
        self.pattern = pattern
        self.stoch = stoch
        self.rsi = rsi
        self.cci = cci
    
    def isFibo(self):
        return True if not self.fibo == 'ntr' and self.fibo == self.trend or self.fibo == self.pattern or self.fibo == self.trust else False
    
    def isStoch(self):
        return True if not self.stoch == 'ntr' and self.stoch == self.rsi or self.stoch == self.cci else False

    def signal(self):
        print(self.isFibo(), self.isStoch())

        print(f"Ticobot: A continuación le mostramos el resultado del análisis")
        headers = ["Tendencia","Confianza","Retroceso","Oscilador","Velocidad","Fuerza","Patron","Resumen"]

        signal = self.fibo if self.isFibo() else self.stoch if self.isStoch() else 'ntr'

        result_table = [[self.trend,self.trust,self.fibo,self.stoch,self.cci,self.rsi,self.pattern,signal]]
        print(tbl(result_table, headers))
        return signal
