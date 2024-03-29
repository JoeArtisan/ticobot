#!/usr/bin/python
from iqoptionapi.stable_api import IQ_Option as IQ
from ticobot.shopping.binary import BuyBinary
from ticobot.shopping.digital import BuyDigital
import numpy as np

class Broker:
  def __init__(self,email,passwd,mode):
    self.email = email
    self.passwd = passwd
    self.api = None
    self.mode = mode
    
  def connect(self):
    self.api = IQ(self.email,self.passwd)
    header = {"User-Agent":r"Mozilla/12.0 (X12; Linux x64; rv:70.0) Gecko/20100101 Firefox/666.0"}
    cookie = {"api":"GOOD"}
    self.api.set_session(header,cookie)
    self.api.connect()
    self.api.change_balance(self.mode)
    
  def getCandles(self,asset,size,period):
    self.api.start_candles_stream(asset,size,period)
    data = self.api.get_realtime_candles(asset,size)
    self.api.stop_candles_stream(asset,size)
    return self.prepareData(data)
  
  def prepareData(self,candles):
    data = {'open': np.array([]), 'high': np.array([]), 'low': np.array([]), 'close': np.array([]), 'volume': np.array([])}
    for i in candles:
      data["open"] = np.append(data["open"],candles[i]["open"])
      data["high"] = np.append(data["high"],candles[i]["max"])
      data["low"] = np.append(data["low"],candles[i]["min"])
      data["close"] = np.append(data["close"],candles[i]["close"])
      data["volume"] = np.append(data["volume"],candles[i]["volume"])
    return data
    
  def buyDigital(self,packet):
    buy = BuyDigital(self.api,packet)
    buy.start()
    buy.join

  def buyBinary(self,packet):
    buy = BuyBinary(self.api,packet)
    buy.start()
    buy.join
  
  def buy(self,packet):        
    if packet[0] == 'digital':
        self.buyDigital(packet)
    elif packet[0] == 'binary':
        self.buyBinary(packet)