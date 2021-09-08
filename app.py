from main import tgePrice
from term import holidays, termPrice
from tgeBASE import tgeBasePrice
from gas import tgeGasPrice

startDay = 30
endDay = 31
tradeMonth = 7
tradeYear = 2021

tgePrice(startDay, endDay, tradeMonth, tradeYear)
termPrice(startDay, endDay, tradeMonth, tradeYear)
tgeBasePrice(startDay, endDay, tradeMonth, tradeYear)
tgeGasPrice(startDay, endDay, tradeMonth, tradeYear)