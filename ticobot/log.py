#!/usr/bin/python
import logging

class Log:
  def __init__(self):
    logging.basicConfig(filename='ticobot.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

  def add(self,msg):
    logging.warning(f'Ticobot: {msg}')

  def addp(self,msg):
    print(f'Ticobot: {msg}')
    self.add(msg)
