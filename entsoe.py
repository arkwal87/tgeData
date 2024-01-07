import requests
import json
import tokens
from zipfile import ZipFile

URL = 'https://transparency.entsoe.eu/api?'

API_TOKEN = tokens.ENTSOE_TOKEN

def mojeZaciaganie():
    # headers = {
    #     'securityToken': API_TOKEN,
    #     # 'Content-Type': 'application/xml',
    #     'documentType': 'A65',
    #     'processType': 'A16',
    #     'OutBiddingZone_Domain': '10YCZ-CEPS-----N',
    #     'periodStart': '201512312300',
    #     'periodEnd': '201612312300'
    # }
    # params = {
    #     'DocumentType': 'A89',
    #     'Type_MarketAgreement.Type': 'A01',
    #     'BusinessType': 'A96',
    #     'ControlArea_Domain': '10YCZ-CEPS-----N',
    #     'TimeInterval': '2020-01-10T23:00Z/2020-01-11T23:00Z'
    # }
    # r = requests.get(url=URL, headers=headers, data=params)
    headers = {
        'securityToken': API_TOKEN,
        'Content-Type': 'application/xml',
        'documentType': 'A85',
        # 'processType': 'A16',
        'ControlArea_Domain': '10YPL-AREA-----S',
        'periodStart': '202001102300',
        'periodEnd': '202001112300'
    }

    r = requests.post(url=URL, params=headers, headers={'Content-Type': 'application/xml'})
    print(r.headers)
    print(r.url)
    print(r.text)
    print(r)
    # with ZipFile(r,'r') as zip:
    #         zip.printdir()
    # data_dict = xmltodict.parse(r.text)
    # json_data = json.dumps(data_dict)
    # print(json_data)
    return print(r)


mojeZaciaganie()
