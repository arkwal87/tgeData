import wapi, os, glob
import pandas as pd
import xlwings as xw
import tokens
from datetime import datetime

# dateDelivery = "2024-01-06"
# issueHour = "13"

ws = xw.Book(f"C:/Users/{os.environ['USERNAME']}/OneDrive/Dokumenty/trading/model/model.xlsm").sheets("model")
date_delivery = str(ws.range("B2").value)[:10]
# print(dateDelivery)

issue_hour = str(int(datetime.now().strftime("%H")) - 1).zfill(2)
# print(issueHour)

winPath = f"C:/Users/{os.environ['USERNAME']}/OneDrive/Dokumenty/trading/model/model_data/volue/"
areas = ["de", "cz", "sk", "se4", "lt"]

volue_id = tokens.VOLUE_ID
volue_secret = tokens.VOLUE_SECRET


def download_volue_prices(date_delivery, issue_hour):
    final_df = pd.DataFrame()
    # print(final_df)
    session = wapi.Session(client_id=volue_id, client_secret=volue_secret)
    for area in areas:
        curve = session.get_curve(name=f'pri {area} spot ec00 €/mwh cet h f')
        ts = curve.get_instance(issue_date=f"{date_delivery}T{issue_hour}:00:00+01:00")
        # ts = curve.get_latest()
        pd_s = ts.to_pandas()  # convert TS object to pandas.Series object
        pd_df = pd_s.to_frame()  # convert pandas.Series to pandas.DataFrame
        final_df = pd.concat([final_df, pd_df[0:24]], axis=1)
        final_df.rename(columns={f"pri {area} spot ec00 €/mwh cet h f": area}, inplace=True)
        print(area)

    final_df = final_df.set_axis([i + 1 for i in range(24)], axis=0)
    final_df = final_df.set_axis(areas, axis='columns')
    # print(final_df)
    final_df.to_excel(f"{winPath}{date_delivery}T{issue_hour}_price.xlsx")


def latest_file():
    list_of_files = glob.glob(f'{winPath}*')
    latest_f = max(list_of_files, key=os.path.getmtime)
    latest_f = latest_f.replace(winPath[:-1], "")[1:]
    return latest_f


if latest_file() != f'{date_delivery}T{issue_hour}_price.xlsx':
    download_volue_prices(date_delivery, issue_hour)
else:
    print("Dane aktualne")
