from main import tgePrice
from term import termPrice, termGasPrice
from tgeBASE import tgeBasePrice
from gas import tgeGasPrice
import nordpool, epex

scrap_date = "07-01-2024"

startDay = 1
endDay = int(scrap_date[0:2])
tradeMonth = 1
tradeYear = 2024

tgePrice(startDay, endDay, tradeMonth, tradeYear)
# termPrice(startDay, endDay, tradeMonth, tradeYear)
# termGasPrice(startDay, endDay, tradeMonth, tradeYear)
# tgeBasePrice(startDay, endDay, tradeMonth, tradeYear)
# tgeGasPrice(startDay, endDay, tradeMonth, tradeYear)

nordpool.np_flows(scrap_date)
nordpool.np_capacities(scrap_date)
nordpool.np_vol(scrap_date)
nordpool.np_price(scrap_date)
epex.epex_pl(scrap_date)
epex.epex_de(scrap_date)
