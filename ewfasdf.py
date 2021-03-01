import requests

cookies = {
    'eu_cookieClosed': 'true',
    'ROUTEID': '.lifereay1',
    '_pk_ref.1.c235': '^%^5B^%^22^%^22^%^2C^%^22^%^22^%^2C1610015399^%^2C^%^22https^%^3A^%^2F^%^2Fwww.google.com^%^2F^%^22^%^5D',
    '_pk_id.1.c235': '5b4b37a0823f275c.1603882963.27.1610015434.1610015399.',
    'JSESSIONID': '58234C58B1B440FC53A90F2D56C8DE5F.liferay1',
    'LFR_SESSION_STATE_20159': '1610019049062',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.pse.pl/dane-systemowe/plany-pracy-kse/plan-koordynacyjny-5-letni/wielkosci-podstawowe',
    'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
    'Origin': 'https://www.pse.pl',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Content-Length': '0',
}

data = {
  'safeargs_data': '5f5f7265706f72743d504c5f50445f474f5f42494c414e53265f5f63616c6c547970653d7026646174615f6f643d323032312d30312d303726646174615f646f3d323032312d30322d3037265f737667737570706f72743d74727565267265736f7572636549443d646f63756d656e7455524c'
}

response = requests.post('https://www.pse.pl/dane-systemowe/plany-pracy-kse/plan-koordynacyjny-5-letni/wielkosci-podstawowe', headers=headers, cookies=cookies, data=data)
