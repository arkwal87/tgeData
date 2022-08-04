import requests
import pandas as pd
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import os

winPath = f"C:/Users/{os.environ['USERNAME']}/OneDrive/Dokumenty/pyData"

startDay = 1
endDay = 1
tradeMonth = 7
tradeYear = 2022


def tgeCap(startDay, endDay, tradeMonth, tradeYear):
    for tradeDay in range(startDay, endDay + 1):
        if int(tradeDay) < 10:
            tradeDay = str("0" + str(int(tradeDay)))
        if int(tradeMonth) < 10:
            tradeMonth = str("0" + str(int(tradeMonth)))

        dateDelivery = datetime.strptime(f'{tradeDay}-{tradeMonth}-{tradeYear}', '%d-%m-%Y').date()
        dateURL = (dateDelivery).strftime('%d-%m-%Y')
        my_page = requests.get(
            f"https://tge.pl/energia-elektryczna-mc-dostepne-zdolnosci-przesylowe?dateShow={dateURL}&dateAction"
        )
        soup = BeautifulSoup(my_page.content, 'html.parser')

        # print(soup)
        #
        # new = soup.select(
        #     f".table-responsive.wyniki-table-mc > table > tbody > tr:nth-child(1) > td:nth-child(2)"
        # )[0]
        #
        # print(new.text.replace(" ", "").replace(",","."))
        #
        day = []

        data_set = {
            "Data": [],
            "Godzina": [],
            "PL AC Import": [],
            "PL AC Export": [],
            "LT-PL": [],
            "PL-LT": [],
            "SE4-PL": [],
            "PL-SE4": [],
        }
        data_keys = ["Data", "Godzina", "PL AC Import", "PL AC Export", "LT-PL", "PL-LT", "SE4-PL", "PL-SE4"]

        for element in range(2, 10):
            for hour in range(1, 25):
                if element == 2:
                    day.append(dateURL)
                elif element == 3:
                    day.append(hour)
                else:
                    new = soup.select(
                        f".table-responsive.wyniki-table-mc > table > tbody > tr:nth-child({hour}) > "
                        f"td:nth-child({element-2})")[0]
                    day.append(float(new.text.replace(",", ".").replace(" ", "")))
            data_set[data_keys[element-2]] = day
            day = []

        for element in data_keys:
            print(element, data_set[element])

        df = pd.DataFrame(data=data_set)
        print(df)
        # print(dateDelivery)
        # df.index.name = dateDelivery
        # df.columns = [i for i in range(1, 25)]
        # print(df.set_index(["Data", "Godzina"]))
        df.to_excel(f"{winPath}/capacities/{dateDelivery}_cap.xlsx", index=False)


tgeCap(startDay, endDay, tradeMonth, tradeYear)
