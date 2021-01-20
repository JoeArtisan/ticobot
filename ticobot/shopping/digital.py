from threading import Thread as Th
from ticobot.database import Database

class BuyDigital(Th):
    def __init__(self, api, signal, money, asset, expiration, result):
           Th.__init__(self)
           self.api = api
           self.signal = signal
           self.money = money
           self.asset = asset
           self.expiration = expiration
           self.result = result
           self.db = Database()
        
    def run(self):
            status, buy_id = self.api.buy_digital_spot(self.asset,self.money,self.signal,self.expiration)
            if not status == "error":
                print(f"Ticobot: Hemos realizado una compra #{buy_id} {self.asset} {self.signal}")
                transaction = [("digital",self.expiration,self.asset,self.result[0],'ntr',self.result[1],self.result[2],self.signal, buy_id)]
                self.db.insertTransaction(transaction)
            else:
                print(f"Ticobot: No hemos podido realizar la compra #{buy_id} {self.asset}")
