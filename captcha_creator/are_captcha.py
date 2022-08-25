import time
import uuid

from crawl_knife.browser.base import image_interceptor
from crawl_knife.browser.chrome import init_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def save_interceptor(request, response):
    if request.path == '/Search_By_BN.aspx':
        if 'DXCache' in request.params:
            with open(f'E:/ARE/{uuid.uuid4().hex}.png','wb') as f:
                f.write(response.body)


driver = init_driver()
try:
    driver.request_interceptor = image_interceptor
    driver.response_interceptor = save_interceptor
    driver.get('https://ner.economy.ae/Search_By_BN.aspx')

    for _ in range(1000):
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="ctl00_MainContent_View_ucSearch_By_BN_cbpBreadCrumbOverAll_BAs_ctlCaptcha_IMGD"]')))
        driver.refresh()

finally:
    driver.quit()