import hashlib
import os
import uuid

import requests


def get_captcha(path, num):
    url = "https://datawarehouse.dbd.go.th/botdetectcaptcha?get=image&c=captchaCode&t=c38b6a2614ae4fb190ac331e3c4177b7&d=1663694135326"

    payload = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0',
        'Accept': 'image/avif,image/webp,*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://datawarehouse.dbd.go.th/',
        'Cookie': 'visid_incap_2466344=C6QfLTfAT7aT4tE/YoNa/EnQ8WIAAAAAQUIPAAAAAABycRb3MoRgad1jWzBCw9k+; JSESSIONID=ZTA3NzEyZWYtNGM5Mi00OGNjLWIwNmQtMTJjYmU1ZGUwZGNh; TS0162c10e=01554f3719cd6f0cb98b2e6c474f768a98aadbc016f9a50ba45ad9532a75c5e83b26ec8f878d456ce0d306c06cbac65b4057f7789ef60a39295e6f882b28e9962b79677b8a; TS45b3629a027=08aef5706eab2000a9ad4e964b8e4a3e3159fc281fca2488fc56919c3cf2c9dd25a10f8792a8e3240813c313c0113000c86888f75451d7c0b72df006136e4c11dfa4c1b770a77547dea3c41c189c50ba7715f1a8b430837b48ac460403619217; incap_ses_1222_2466344=PduxAQlWJ0EroYIsNWv1EJRlKmMAAAAAhH+zLk08Nq3RQfaemE5MLQ==; incap_ses_1556_2466344=Eg3dBRvuRwGQaS5v8gWYFQFnKmMAAAAAg6JjddXSx5AgLNs3WGVgAQ==; TS0162c10e=01554f371997a0bd866e832fc78feaccb16bee77a8822c11e1baf76f98438881e7849bbaa9b77ae560a5861ad844a46a6397be0c880319512940a51209e619646f2796f195; TS45b3629a027=08aef5706eab2000ef8e3ac3e667c32789cc419b7473f0ab9da15787c5897f720ae65c2b8a370f3d086c7ed676113000f5e0ab420eaca80771ae2413fd598af2b7a6e1dd3af5c8828116aa079e0b51b7b98fcdf2076d79f553749b5c5c9e4b02',
        'Sec-Fetch-Dest': 'image',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers'
    }
    session = requests.Session()
    for _ in range(num):
        response = session.request("GET", url, headers=headers, data=payload)
        if response.status_code == 200:
            with open(os.path.join(path, f'{uuid.uuid4().hex}.jpeg'), "wb") as f:
                f.write(response.content)


if __name__ == '__main__':
    get_captcha('.', 1)
