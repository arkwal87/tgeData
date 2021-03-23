from main import tgePrice
from term import holidays, termPrice
from tgeBASE import tgeBasePrice

startDay = 17
endDay = 20
tradeMonth = 3
tradeYear = 2021

tgePrice(startDay, endDay, tradeMonth, tradeYear)
termPrice(startDay, endDay, tradeMonth, tradeYear)
tgeBasePrice(startDay, endDay, tradeMonth, tradeYear)