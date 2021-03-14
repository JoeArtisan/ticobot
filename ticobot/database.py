#!/usr/bin/python
from mysql.connector import connect, Error

class Database:
  def __init__(self):
    self.connection = connect(
        host = 'us-cdbr-east-03.cleardb.com',
        user = 'b1315be03332e6',
        password = 'f8be715a',
        database = 'heroku_b042dac393fd9aa',
    )

  def insert(self,buy_id,packet,result):
    # (expiration,asset,ema,cci,rsi,fibo,stoch,resume,buy_id)
    packet = [(packet[2],packet[1],packet[4],packet[5],packet[6],packet[7],packet[8],packet[9],buy_id,result)]

    query = """ 
        INSERT INTO transactions (moment,expiration,asset,ema,cci,rsi,fibo,stoch,resume,buy_id,state)
        VALUES (NOW(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    try:
      with self.connection.cursor() as cursor:
        cursor.executemany(query,packet)
        self.connection.commit()
    except Error as e:
      print(e)
