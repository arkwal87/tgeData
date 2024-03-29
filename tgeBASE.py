from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime, timedelta
from main import winPath


def tgeBasePrice(startDay, endDay, tradeMonth, tradeYear):
    for tradeDay in range(startDay, endDay + 1):
        if int(tradeDay) < 10:
            tradeDay = str("0" + str(int(tradeDay)))
        if int(tradeMonth) < 10:
            tradeMonth = str("0" + str(int(tradeMonth)))

        dateDelivery = datetime.strptime(f'{tradeYear}-{tradeMonth}-{tradeDay}', '%Y-%m-%d').date()
        dateURL = dateDelivery - timedelta(days=1)

        my_page = requests.get(f"https://tge.pl/energia-elektryczna-rdn-tge-base?date_start={dateURL}&iframe=1")
        soup = BeautifulSoup(my_page.content, 'html.parser')
        data_set = {"price": [], "vol": []}

        for h in range(4, 28):
            if "-" in soup.find_all("tr")[h].find_all("td")[1].get_text():
                data_set["price"].append(0)
            else:
                data_set["price"].append(float(soup.find_all("tr")[h].find_all("td")[1].get_text().replace(",", ".")))
            data_set["vol"].append(float(soup.find_all("tr")[h].find_all("td")[2].get_text().replace(",", ".")))
        df = pd.DataFrame(data=data_set).T
        df.index.name = dateDelivery
        df.columns = [i for i in range(1, 25)]
        print(dateDelivery)
        df.to_excel(f"{winPath}/tgeBase/{dateDelivery}_tgeBase.xlsx")
