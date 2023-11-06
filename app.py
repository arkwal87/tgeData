from main import tgePrice
from term import termPrice, termGasPrice
from tgeBASE import tgeBasePrice
from gas import tgeGasPrice
import nordpool, epex

scrap_date = "07-11-2023"
startDay = 1
endDay = 30
tradeMonth = 6
tradeYear = 2023

# tgePrice(startDay, endDay, tradeMonth, tradeYear)
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