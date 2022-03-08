import os
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime, timedelta

from main import winPath


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

        df = pd.DataFrame(data=data_set).set_index("date")

    df.to_excel(f"{winPath}/tgeGas/{tradeMonth}-{tradeYear}_tgeGasDA.xlsx")