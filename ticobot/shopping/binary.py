from threading import Thread as Th
from ticobot.database import Database

class BuyBinary(Th):
    def __init__(self, api, packet):
        Th.__init__(self)
        self.api = api
        self.packet = packet
        
    def run(self):
        packet = self.packet
        status, buy_id = self.api.buy(packet[3],packet[1],packet[-1],packet[2])
        if status:
            print(f"Ticobot: Hemos realizado una compra #{buy_id} {packet[1]} {packet[-1]}")
            result,profit = self.api.check_win_v3(buy_id)
            print(f"Ticobot: El resultado de la compra #{buy_id} {packet[1]} {packet[-1]} es {result} {profit}")
            db = Database()  
            db.insert(buy_id,packet,result)
        else:
            print(f"Ticobot: No hemos podido realizar la compra #{buy_id} {packet[1]}")