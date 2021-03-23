import requests
import pandas as pd
import os
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

startDay = 17
endDay = 20
tradeMonth = 3
tradeYear = 2021


def tgePrice(startDay, endDay, tradeMonth, tradeYear):
    for tradeDay in range(startDay, endDay + 1):
        if int(tradeDay) < 10:
            tradeDay = str("0" + str(int(tradeDay)))
        if int(tradeMonth) < 10:
            tradeMonth = str("0" + str(int(tradeMonth)))

        dateDelivery = datetime.strptime(f'{tradeDay}-{tradeMonth}-{tradeYear}', '%d-%m-%Y').date()
        dateURL = (dateDelivery - timedelta(days=1)).strftime('%d-%m-%Y')
        my_page = requests.get(f"https://tge.pl/energia-elektryczna-rdn?dateShow={dateURL}&dateAction=prev")
        soup = BeautifulSoup(my_page.content, 'html.parser')

        day = []

        data_set = {"fix1": [], "vol1": [], "fix2": [], "vol2": []}
        date_keys = ["fix1", "vol1", "fix2", "vol2"]

        for element in range(2, 6):
            for hour in range(1, 25):
                new = \
                    soup.select(
                        f"#footable_kontrakty_godzinowe > tbody > tr:nth-child({hour}) > td:nth-child({element})")[
                        0]
                day.append(float(new.get_text().replace(",", ".")))
            data_set[date_keys[element - 2]] = day
            day = []

        for element in date_keys:
            print(element, data_set[element])

        df = pd.DataFrame(data=data_set).T
        print(dateDelivery)
        df.index.name = dateDelivery
        df.columns = [i for i in range(1, 25)]
        df.to_excel(f"C:/Users/{os.environ['USERNAME']}/Documents/pyData/tge/{dateDelivery}_tge.xlsx")
