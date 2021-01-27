#!/usr/bin/python
import numpy as np

class Atr:
    '''
    Average True Range
    a is array of high prices, b is array of low prices, 
    c is array of closing prices, d is period for averaging
    '''
    def __init__(self,high_prices,low_prices,close_prices,period):
        self.high_prices = high_prices[len(high_prices)-period:len(high_prices)]
        self.low_prices = low_prices[len(low_prices)-period:len(low_prices)]
        self.close_prices = close_prices[len(close_prices)-period:len(close_prices)]
        self.period = period
        self.overhigh = 0
        self.overlow = 0
    
    def prepare(self):
        
        a = self.high_prices
        print(len(a))
        b = self.low_prices
        c = self.close_prices
        d = self.period
        tr = np.zeros(len(a))
        tr[0] = a[0]-b[0]
        return a,b,c,d,tr,np.zeros(len(a)-d+1)
        
    def getSignal(self):
        h,l,c,N,tr,result = self.prepare()
        '''
        for i in range(1,len(a)):
            hl = a[i]-b[i]
            hpc = np.fabs(a[i]-c[i-1])
            lpc = np.fabs(b[i]-c[i-1])
            tr[i] = np.amax(np.array([hl,hpc,lpc]))

        result[0] = np.sum(tr[0:d])/d

        for i in range(1,len(a)-d+1):
            result[i] = (result[i-1]*(d-1)+tr[i+d-1])/d
        '''
        h = h[-N:]
        l = l[-N:]

        print ("len(h)",len(h), "len(l)", len(l))
        print ("Close", c)
        previousclose = c[-N-1:-1]

        print ("len(previousclose)",len(previousclose))
        print ("Previous clsoe",previousclose)
        truerange = np.maximum(h-l, h-previousclose,previousclose - 1)

        print ("True range", truerange)

        atr = np.zeros(N)

        atr[0] = np.mean(truerange)

        for i in range(1,N):
            atr[i] = (N-1) * atr[i-1] + truerange[i]
            atr[i] /= N


                
        print('Average true range:',atr)

        return 'ntr'#if rsi < self.overlow else 'put' if rsi > self.overhigh else 'ntr'
