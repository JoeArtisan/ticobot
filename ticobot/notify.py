#!/usr/bin/python
from win10toast import ToastNotifier
import pandas as pd

class Notify():
    
    def __init__(self,csv,packet):
        self.csv = csv
        self.packet = packet

    def send(self):
        df = pd.DataFrame(self.csv) 
        df.to_csv('data.csv', index=False, header=True)
        ToastNotifier().show_toast("Ticobot",f"Hemos tomado una operación en el mercado {self.packet[1]} estimando un {self.packet[-1]} en {self.packet[2]} minutos.",icon_path='favicon.ico',duration=5)
