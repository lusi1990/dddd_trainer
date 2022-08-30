import os
import random
import uuid

import requests


def init_web_captcha(path, num):
    session = requests.session()
    verify_code_pic_url = f"https://www.icris.cr.gov.hk/csci/shwcaptcha.do?checkPoint=login&rand={random.random()}"
    for _ in range(num):
        r = session.get(verify_code_pic_url, )
        with open(os.path.join(path, f'{uuid.uuid4().hex}.png'), "wb") as f:
            f.write(r.content)


if __name__ == '__main__':
    init_web_captcha('.', 1)
