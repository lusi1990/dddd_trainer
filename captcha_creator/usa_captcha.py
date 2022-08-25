import os
import uuid

import requests
from loguru import logger

images_set_path = "E:\\vermont"


def get_vermont_captcha(num):
    """

    """
    url = "https://bizfilings.vermont.gov/online/BusinessInquire/ShowCaptchaImage"

    payload = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://bizfilings.vermont.gov/online/BusinessInquire',
        'Cookie': 'visid_incap_2276107=U2rIKyobRLu+RHWrYzY8tx22Z2IAAAAAQUIPAAAAAABvPXGV7jnZSYiVdhKNdDAo; incap_ses_1449_2276107=VFvwNcLuziy5YbLeDOIbFB22Z2IAAAAA8L2Ro/uHJY+vRtNk1B+JwQ==; incap_ses_258_2276107=aiM3PaN1hBQL1AENRZqUAx+2Z2IAAAAAhBcJ2udrv2gDWZAXJCm3EQ==; incap_ses_1295_2276107=UXjTS5wG1zhhC6nsJcT4EU+2Z2IAAAAABtIcU3XkevabgLsVKLOo4g==; __RequestVerificationToken=ZmejDo1LbW-0FykysS4d9G7r8lYLcQJUQawpPljG7YK6ILnHwz_8iFoCZHJ5JBeSSzY7kz51Rpk61uovwDOoo-xnywRD4gYKoKKx93ja_BzE0ZVdtu4faK8TJlOo5OhEWLp8qsy0Ue3zoinKDqo4GA2; ASP.NET_SessionId=hlw3mkbhksfl2axfvug1kzgm; onlinecollapsibleheaderid=0; incap_ses_1356_2276107=ZF7fbeBrlhbqR4WQQHvREjy3Z2IAAAAAbmmJI1kxP/s9ltLRi0dxIg==; incap_ses_1449_2276107=wM4IER/4Qh65CLHeDOIbFOKyZ2IAAAAAYHxpzdtmXNSon6EPp0BthQ==; incap_ses_258_2276107=juH9RJY97Tbs5/8MRZqUA/SzZ2IAAAAAaq8DnDLLGyPbEXxG1kUe6A==',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'iframe',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers'
    }
    proxy = {
        "http": "http://127.0.0.1:10809",
        "https": "http://127.0.0.1:10809",
    }
    session = requests.session()
    for _ in range(num):
        try:
            response = session.request("GET", url, headers=headers, data=payload,
                                       # proxies=proxy
                                       )
            if response.status_code == 200:
                # print(response.text)
                if response.headers['Content-Type'] == 'image/jpeg':
                    filename = uuid.uuid4().hex + ".jpeg"
                    with open(os.path.join(images_set_path, filename), 'wb') as f:
                        f.write(response.content)
                else:
                    print(response.text)
            else:
                print(response.text)
        except Exception as err:
            logger.error(err)


if __name__ == '__main__':
    get_vermont_captcha(1000)
    # print("visid_incap_2276107=S788HDqVSISYdFYtIkHqcL+uZ2IAAAAAQUIPAAAAAAA0wXYh1t4kOPwP4ha8BUuR; incap_ses_977_2276107=gNDJbG25exwjMtfe5wCPDb+uZ2IAAAAAOCtFkoOYAilKLcN9XIg0hQ==; __RequestVerificationToken=1mlzDwsmRHZylK62CSm9CgV92uv6NMMLn9y4L0kRtE2ydb0J9qa18xrqFtRw2yRQ7ECuN5ZXiUEdHUDJN76-MggzIxFngGZ0xYn10i0DOVzl2fsSMpz9sf46B604yF6vLBV1UPydYv14UohU49FwPg2; onlinecollapsibleheaderid=0; ASP.NET_SessionId=11qfgfpeu3tu1vzqivzhkrr3"=="visid_incap_2276107=S788HDqVSISYdFYtIkHqcL+uZ2IAAAAAQUIPAAAAAAA0wXYh1t4kOPwP4ha8BUuR; incap_ses_977_2276107=gNDJbG25exwjMtfe5wCPDb+uZ2IAAAAAOCtFkoOYAilKLcN9XIg0hQ==; __RequestVerificationToken=1mlzDwsmRHZylK62CSm9CgV92uv6NMMLn9y4L0kRtE2ydb0J9qa18xrqFtRw2yRQ7ECuN5ZXiUEdHUDJN76-MggzIxFngGZ0xYn10i0DOVzl2fsSMpz9sf46B604yF6vLBV1UPydYv14UohU49FwPg2; onlinecollapsibleheaderid=0; ASP.NET_SessionId=11qfgfpeu3tu1vzqivzhkrr3")
