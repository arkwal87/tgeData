import os

from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime, timedelta
#
# scrap_date = "02-04-2023"

def epex_pl(scrap_date):
    dateDelivery = datetime.strptime(f'{scrap_date}', '%d-%m-%Y').date()
    scrap_page = requests.get(
        f"https://www.epexspot.com/en/market-data?market_area=PL&trading_date={dateDelivery - timedelta(days=1)}"
        f"&delivery_date={dateDelivery}"
        f"&underlying_year=&modality=Auction&sub_modality=DayAhead&product=60&data_mode=table&period=")
    soup = BeautifulSoup(scrap_page.content, 'html.parser')

    data_set = [[], []]

    for hour in range(24):
        data_set[0].append(float(soup.select(f"tr.child > td:nth-child(3)")[hour].text.replace(",", "")))
        data_set[1].append(float(soup.select(f"tr.child > td:nth-child(4)")[hour].text.replace(",", "")))

    headers = ["Volume", "Price"]

    df = pd.DataFrame(data_set, index=headers, columns=range(1, 25)).T

    print(df)
    df.to_excel(f"C:/Users/{os.environ['USERNAME']}/OneDrive/Dokumenty/pyData/epex/{scrap_date}_PL.xlsx")


def epex_de(scrap_date):
    dateDelivery = datetime.strptime(f'{scrap_date}', '%d-%m-%Y').date()
    scrap_page = requests.get(
        f"https://www.epexspot.com/en/market-data?market_area=DE-LU&trading_date={dateDelivery - timedelta(days=1)}"
        f"&delivery_date={dateDelivery}"
        f"&underlying_year=&modality=Auction&sub_modality=DayAhead&product=60&data_mode=table&period=")
    soup = BeautifulSoup(scrap_page.content, 'html.parser')

    data_set = [[], []]

    for hour in range(24):
        data_set[0].append(float(soup.select(f"tr.child > td:nth-child(3)")[hour].text.replace(",", "")))
        data_set[1].append(float(soup.select(f"tr.child > td:nth-child(4)")[hour].text.replace(",", "")))

    headers = ["Volume", "Price"]

    df = pd.DataFrame(data_set, index=headers, columns=range(1, 25)).T

    print(df)
    df.to_excel(f"C:/Users/{os.environ['USERNAME']}/OneDrive/Dokumenty/pyData/epex/{scrap_date}_DE.xlsx")


# epex_pl(scrap_date)
# epex_de(scrap_date)
