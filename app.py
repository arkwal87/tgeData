import os

from main import tgePrice
from term import termPrice, termGasPrice
from tgeBASE import tgeBasePrice
from gas import tgeGasPrice

startDay = 1
endDay = 28
tradeMonth = 2
tradeYear = 2022

tgePrice(startDay, endDay, tradeMonth, tradeYear)
termPrice(startDay, endDay, tradeMonth, tradeYear)
termGasPrice(startDay, endDay, tradeMonth, tradeYear)
tgeBasePrice(startDay, endDay, tradeMonth, tradeYear)
tgeGasPrice(startDay, endDay, tradeMonth, tradeYear)
