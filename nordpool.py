import os

from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import numpy as np

# scrap_date = "02-04-2023"

def np_flows(scrap_date):
    scrap_page = requests.get(
        f"https://www.nordpoolgroup.com/api/marketdata/page/411514?currency=,EUR,EUR,EUR&endDate={scrap_date}")
    soup = BeautifulSoup(scrap_page.content, 'html.parser')
    soup_json = json.loads(soup.text)

    headers = []
    data_list = []

    for header in range(10):
        headers.append(soup_json['data']['Rows'][0]['Columns'][header]['Name'])
        hour_list = []
        for hour in range(24):
            hour_val = soup_json['data']['Rows'][hour]['Columns'][header]['DisplayNameOrDominatingDirection']
            if hour_val != "-":
                hour_list.append(float(hour_val.replace(" ", "").replace(",", ".")))
        data_list.append(hour_list)

    df = pd.DataFrame(data_list, index=headers, columns=range(1, 25)).T
    df["export"] = round(- df["PL - CZ"] - df["PL - SK"] - df["PL - DE"] - df["PL - LT"] - df["PL - SE4"], 2)
    df["import"] = round(df["CZ - PL"] + df["SK - PL"] + df["DE - PL"] + df["LT - PL"] + df["SE4 - PL"], 2)
    df["flow"] = round(df["export"] + df["import"], 2)
    print(df)
    df.to_excel(f"C:/Users/{os.environ['USERNAME']}/OneDrive/Dokumenty/pyData/nordpool/{scrap_date}_flows.xlsx")


def np_capacities(scrap_date):
    scrap_page = requests.get(
        f"https://www.nordpoolgroup.com/api/marketdata/page/411340?currency=,EUR,EUR,EUR&endDate={scrap_date}")
    soup = BeautifulSoup(scrap_page.content, 'html.parser')
    soup_json = json.loads(soup.text)

    headers = []
    data_list = []

    for header in range(6):
        headers.append(soup_json['data']['Rows'][0]['Columns'][header]['Name'])
        hour_list = []
        for hour in range(1, 25):
            hour_list.append(float(
                soup_json['data']['Rows'][hour]['Columns'][header]['DisplayNameOrDominatingDirection']
                .replace(",", ".").replace(" ", "")))
        data_list.append(hour_list)

    df = pd.DataFrame(data_list, index=headers, columns=range(1, 25)).T
    print(df)
    df.to_excel(f"C:/Users/{os.environ['USERNAME']}/OneDrive/Dokumenty/pyData/nordpool/{scrap_date}_cap.xlsx")


def np_vol(scrap_date):
    scrap_page = requests.get(
        f"https://www.nordpoolgroup.com/api/marketdata/page/391602?currency=,EUR,EUR,EUR&endDate={scrap_date}")
    soup = BeautifulSoup(scrap_page.content, 'html.parser')
    soup_json = json.loads(soup.text)

    headers = []
    data_list = []

    for header in range(2):
        headers.append(soup_json['data']['Rows'][0]['Columns'][header]['Name'])
        hour_list = []
        for hour in range(24):
            hour_list.append(float(
                soup_json['data']['Rows'][hour]['Columns'][header]['DisplayNameOrDominatingDirection']
                .replace(",", ".").replace(" ", "")))
        data_list.append(hour_list)

    df = pd.DataFrame(data_list, index=headers, columns=range(1, 25)).T
    print(df)
    df.to_excel(f"C:/Users/{os.environ['USERNAME']}/OneDrive/Dokumenty/pyData/nordpool/{scrap_date}_vol.xlsx")


def np_price(scrap_date):
    scrap_page = requests.get(
        f"https://www.nordpoolgroup.com/api/marketdata/page/391921?currency=,EUR,EUR,EUR&endDate={scrap_date}")
    soup = BeautifulSoup(scrap_page.content, 'html.parser')
    soup_json = json.loads(soup.text)

    headers = []
    data_list = []
    h_rng = 24

    for header in range(1):
        headers.append(soup_json['data']['Rows'][0]['Columns'][header]['Name'])
        hour_list = []
        for hour in range(h_rng):
            hour_value = soup_json['data']['Rows'][hour]['Columns'][header]['DisplayNameOrDominatingDirection']
            print(hour, hour_value)
            if hour_value != "-":
                hour_list.append(float(hour_value.replace(",", ".")))
            else:
                h_rng += 1
            # print(hour, len(hour_list))
            print(h_rng)
        data_list.append(hour_list)

    df = pd.DataFrame(data_list, index=headers, columns=range(1, len(hour_list)+1)).T
    print(df)
    df.to_excel(f"C:/Users/{os.environ['USERNAME']}/OneDrive/Dokumenty/pyData/nordpool/{scrap_date}_price.xlsx")

#
# np_flows(scrap_date)
# np_capacities(scrap_date)
# np_vol(scrap_date)
# np_price(scrap_date)
