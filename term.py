from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime, timedelta

holidays = [
    "25-12-2020",
    "26-12-2020",
    "01-01-2021",
    "06-01-2021",
    "05-04-2021",
    "06-04-2021",
    "01-05-2021",
    "03-05-2021",
    "03-06-2021",
    "15-08-2021",
    "01-11-2021",
    "11-11-2021",
    "25-12-2021",
    "26-12-2021"
]

holidays = list(map(lambda singleDate: datetime.strptime(singleDate, '%d-%m-%Y').date().strftime('%Y-%m-%d'), holidays))

startDay = 1
endDay = 5
tradeMonth = 2
tradeYear = 2021

for tradeDay in range(startDay, endDay + 1):
    if int(tradeDay) < 10:
        tradeDay = str("0" + str(int(tradeDay)))
    if int(tradeMonth) < 10:
        tradeMonth = str("0" + str(int(tradeMonth)))
    tradeDate = f'{tradeDay}-{tradeMonth}-{tradeYear}'
    conv_date = datetime.strptime(tradeDate, '%d-%m-%Y').date()
    if conv_date.isoweekday() in range(1, 6) and str(conv_date) not in holidays:
        my_page = requests.get(f'https://tge.pl/energia-elektryczna-otf?dateShow={tradeDate}&dateAction=prev')
        soup = BeautifulSoup(my_page.content, 'html.parser')
        new = soup.find_all("tr", class_='period-')
        data_set = []
        keys = [
            "Instrument"
            "First trade",
            "Settlement price",
            "Min Price",
            "Max Price",
            "Total Volume",
            "Lots",
            "Total Value",
            "Number of transactions",
            "Total number of open interests"
        ]

        for element in new:
            new_array = [
                element.select("td", class_='footable-visible footable-first-column col-instrument_name')[0].get_text()]
            for key in keys:
                textVal = element.select(f"td:nth-child({keys.index(key) + 3})")[0].get_text().replace(",", ".")
                if textVal != "-":
                    textVal = float(textVal)
                new_array.append(textVal)
            data_set.append(new_array)
        df = pd.DataFrame(data=data_set)
        df.set_index(df.columns[0], inplace=True)
        df.columns = [key for key in keys]
        df.index.name = tradeDate
        print(conv_date)
        df.to_excel(f'C:/Users/waliszewski_a/Documents/pyData/FW/{conv_date}_FW.xlsx')
