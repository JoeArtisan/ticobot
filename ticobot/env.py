#!/usr/bin/python
from dotenv import load_dotenv as dot
import os

class Env:
  # def __init__(self):

  def prepare(self):
    dot()
    return os.getenv('user'),os.getenv('passwd'),os.getenv('mode'),int(os.getenv('candle')),os.getenv('market'),int(os.getenv('bet')),int(os.getenv('expiration')),eval(os.getenv('assets'))

