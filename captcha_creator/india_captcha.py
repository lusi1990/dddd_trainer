"""
爬取 gst.gov.in 验证码
"""
import os
import time
import uuid

import requests
from loguru import logger
import random
import traceback
import urllib3

images_set_path = "E:\\india_images_set1"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_gst_captcha(num):
    url = "https://services.gst.gov.in/services/captcha?rnd={}"
    payload = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
        'Accept': 'image/avif,image/webp,*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://services.gst.gov.in/services/searchtp',
        'Cookie': 'TS01b8883c=01ab915e2c4f868b6133d95db43f09ae30570d612d41ee16940ee5734b4abfb25c216fdf8843a2cda80379cf45f94436ee94d469ea; CaptchaCookie=99dc57ed5fd84d1595ace82c6184a40d; Lang=en; CaptchaCookie=5f610b7387a548baac9e5bedaeff4df8; TS01b8883c=01ab915e2c4f868b6133d95db43f09ae30570d612d41ee16940ee5734b4abfb25c216fdf8843a2cda80379cf45f94436ee94d469ea',
        'Sec-Fetch-Dest': 'image',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin'
    }
    proxy = {
        "http": "http://127.0.0.1:10809",
        "https": "http://127.0.0.1:10809",
    }
    session = requests.session()
    for _ in range(num):
        try:
            response = session.request("GET", url.format(random.random()), headers=headers, data=payload,
                                        # proxies=proxy
                                        )
            filename = uuid.uuid4().hex + ".png"
            with open(os.path.join(images_set_path, filename), 'wb') as f:
                f.write(response.content)
        except Exception as err:
            logger.error(err)


def get_mca_captcha(num):
    """
    获取 mca.gov.in 验证码
    """
    import requests

    url = "https://www.mca.gov.in/mcafoportal/getCapchaImage.do?id={}"

    payload = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
        'Accept': 'image/avif,image/webp,*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.mca.gov.in/mcafoportal/viewCompanyMasterData.do',
        'Connection': 'keep-alive',
        'Cookie': 'HttpOnly; JSESSIONID=0000nZwe5D91bCaGG3EpiIVfp4Z:1ave0turu; JSESSIONID=0000elN9nGv7PtyYhuSc6-FXtZD:1ave0turu',
        'Sec-Fetch-Dest': 'image',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin'
    }
    session = requests.session()
    for _ in range(num):
        try:
            response = session.request("GET", url.format(random.random() / 10), headers=headers, data=payload,
                                       )
            filename = uuid.uuid4().hex + ".jpeg"
            with open(os.path.join(images_set_path, filename), 'wb') as f:
                f.write(response.content)
        except Exception as err:
            traceback.print_exc()
            # logger.error(err)
        time.sleep(3)


if __name__ == '__main__':
    # get_gst_captcha(10)
    get_mca_captcha(10)
