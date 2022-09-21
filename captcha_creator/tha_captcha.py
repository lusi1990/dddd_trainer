import hashlib
import os
import time
import uuid

import requests


def get_captcha(path, num):
    url = "https://datawarehouse.dbd.go.th/botdetectcaptcha?get=image&c=captchaCode&t=c38b6a2614ae4fb190ac331e3c4177b7&d={}"

    payload = {}
    headers = {
        'authority': 'datawarehouse.dbd.go.th',
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'cookie': 'JSESSIONID=NTU3NzYxNDAtY2FmMi00NWZhLWExOTItMTc3ZGM4MmJjNjc1; TS0162c10e=01554f37199e80dbc4c66e821d39497af25300e8d64c70fe09216a38c53af5ca0221d1d2d809051365af2e548130b7f1965d4d240d3f4bbc0c895dd712c6de06253654f3df; visid_incap_2466344=qBg47nhmTg6eKtHG+h5KOB1xKmMAAAAAQUIPAAAAAABT0L47xOdVuT38I4iskukk; incap_ses_1046_2466344=U3J5PSX0e3luL/43JiSEDh1xKmMAAAAAgsIBmjBvhkAwXTIyhzlPUA==; TS45b3629a027=08aef5706eab2000b2b212949ca877a11b275032b7eff20365827ffc4f83a3e9bcdde43eb5fcdb020883f36fec113000a85c41cd8ec586d2c237f565dac0455c591597a9eac64590c324ac6c578b4b861f87bba7adce4a8fb46c63483bf117a3',
        'dnt': '1',
        'referer': 'https://datawarehouse.dbd.go.th/',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    session = requests.Session()
    for _ in range(num):
        response = session.request("GET", url.format(int(time.time())), headers=headers, data=payload,timeout=5)
        if response.status_code == 200:
            with open(os.path.join(path, f'{uuid.uuid4().hex}.jpeg'), "wb") as f:
                f.write(response.content)
        else:
            print(response.status_code)


if __name__ == '__main__':
    get_captcha(r'E:\tha1', 2000)
