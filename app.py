import os

from main import tgePrice
from term import holidays, termPrice, termGasPrice
from tgeBASE import tgeBasePrice
from gas import tgeGasPrice

winPath = f"C:/Users/{os.environ['USERNAME']}/OneDrive/Documents/pyData"

startDay = 1
endDay = 31
tradeMonth = 1
tradeYear = 2022

tgePrice(startDay, endDay, tradeMonth, tradeYear)
termPrice(startDay, endDay, tradeMonth, tradeYear)
termGasPrice(startDay, endDay, tradeMonth, tradeYear)
tgeBasePrice(startDay, endDay, tradeMonth, tradeYear)
tgeGasPrice(startDay, endDay, tradeMonth, tradeYear)