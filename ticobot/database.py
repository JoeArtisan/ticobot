#!/usr/bin/python
from mysql.connector import connect, Error
import os

class Database:
  def __init__(self):
    self.connection = connect(
        host = 'us-cdbr-east-03.cleardb.com',
        user = 'b1315be03332e6',
        password = 'f8be715a',
        database = 'heroku_b042dac393fd9aa',
    )

  def insertTransaction(self,transaction):
    query = """ 
        INSERT INTO transactions
        (moment, market, expiration, asset, trend, trust, strength, recoil, decision,buy_id)
        VALUES ( NOW(), %s, %s, %s, %s, %s, %s, %s, %s , %s)
    """
    try:
      with self.connection.cursor() as cursor:
            cursor.executemany(query, transaction)
            self.connection.commit()
    except Error as e:
      print(e)
