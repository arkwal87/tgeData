from main import tgePrice
from term import holidays, termPrice, termGasPrice
from tgeBASE import tgeBasePrice
from gas import tgeGasPrice

startDay = 1
endDay = 30
tradeMonth = 9
tradeYear = 2021

tgePrice(startDay, endDay, tradeMonth, tradeYear)
termPrice(startDay, endDay, tradeMonth, tradeYear)
termGasPrice(startDay, endDay, tradeMonth, tradeYear)
tgeBasePrice(startDay, endDay, tradeMonth, tradeYear)
tgeGasPrice(startDay, endDay, tradeMonth, tradeYear)