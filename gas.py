import os
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime, timedelta


def tgeGasPrice(startDay, endDay, tradeMonth, tradeYear):
    data_set = {"date": [], "price": []}
    for tradeDay in range(startDay, endDay + 1):
        if int(tradeDay) < 10:
            tradeDay = str("0" + str(int(tradeDay)))
        if int(tradeMonth) < 10:
            tradeMonth = str("0" + str(int(tradeMonth)))

        dateDelivery = datetime.strptime(f'{tradeYear}-{tradeMonth}-{tradeDay}', '%Y-%m-%d').date()
        dateURL = (dateDelivery - timedelta(days=1)).strftime("%d-%m-%Y")

        my_page = requests.get(f"https://tge.pl/gaz-rdn?dateShow={dateURL}")
        soup = BeautifulSoup(my_page.content, 'html.parser')

        data_set["date"].append(dateDelivery.strftime("%d-%m-%Y"))
        data_set["price"].append(float(soup.find_all("td", class_="footable-visible")[1].get_text().replace(",", ".")))

        # print(data_set)
        df = pd.DataFrame(data=data_set).set_index("date")

    df.to_excel(f"C:/Users/{os.environ['USERNAME']}/Documents/pyData/tgeGas/{tradeMonth}-{tradeYear}_tgeGasDA.xlsx")

# startDay = 1
# endDay = 31
# tradeMonth = 7
# tradeYear = 2021
#
# tgeGasPrice(startDay, endDay, tradeMonth, tradeYear)
