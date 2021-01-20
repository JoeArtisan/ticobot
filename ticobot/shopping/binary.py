from threading import Thread as Th
from ticobot.database import Database
from ticobot.log import Log
import concurrent.futures

class BuyBinary(Th):
    def __init__(self, api, signal, money, asset, expiration, result):
        Th.__init__(self)
        self.api = api
        self.signal = signal
        self.money = money
        self.asset = asset
        self.expiration = expiration
        self.result = result
        self.log = Log()
        self.db = Database()
        
    def run(self):
        check = self.api.buy(self.money,self.asset,self.signal,self.expiration)
        if check:
            print(f"Ticobot: Hemos realizado una compra {self.asset}")
            print(f"Ticobot: Pronto mostraremos los resultados\n")
        else:
            print(f"Ticobot: No hemos podido realizar la compra {self.asset}")

