import os
import time
import uuid


def get_from_web(path):
    from crawl_knife.browser.base import image_interceptor
    from crawl_knife.browser.chrome import init_driver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    def save_interceptor(request, response):
        if request.path == '/Search_By_BN.aspx':
            if 'DXCache' in request.params:
                with open(os.path.join(path, f'{uuid.uuid4().hex}.png'), 'wb') as f:
                    f.write(response.body)

    driver = init_driver()
    try:
        driver.request_interceptor = image_interceptor
        driver.response_interceptor = save_interceptor
        driver.get('https://ner.economy.ae/Search_By_BN.aspx')

        for _ in range(1000):
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="ctl00_MainContent_View_ucSearch_By_BN_cbpBreadCrumbOverAll_BAs_ctlCaptcha_IMGD"]')))
            driver.refresh()

    finally:
        driver.quit()


def init_by_captcha(images_set_path, num: int):
    """

    """

    import random

    import os

    from captcha.image import ImageCaptcha

    char_set = ['n', '9', 'v', 'e', 'j', 'h', 'u', 'b', 'a', 'm', 'y', 'f', 'p', 'r', '4', '8', 'd', 'q', '3',
                'z', 'l', 'x', '2', '7', '6', 'c', 's', '5', 'k', 't']

    random_string = ''.join(char_set)
    print(random_string)

    image = ImageCaptcha(width=100, height=50, fonts=['./fonts/CALISTI.TTF'])
    for _ in range(num):
        code = ''.join(random.choices(random_string, k=6))
        name = f'{code}.png'
        file_path = os.path.join(images_set_path, name)
        image.write(code, file_path)


if __name__ == '__main__':
    init_by_captcha(r'E:\are3', 10000)
