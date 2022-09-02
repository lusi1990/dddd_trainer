import io

import ddddocr
import pyautogui

ocr = ddddocr.DdddOcr(show_ad=False, old=True)
ok_p= pyautogui.locateCenterOnScreen('ok.png')
cancel_p= pyautogui.locateCenterOnScreen('cancel.png')
print(ok_p,cancel_p)
# while True:`
#     print(pyautogui.position())
for _ in range(2537):
    im = pyautogui.screenshot(region=(1397,864, 90, 30))
    img_byte_arr = io.BytesIO()
    im.save(img_byte_arr, format='PNG')
    image_bytes = img_byte_arr.getvalue()

    code = ocr.classification(image_bytes)
    print(code)
    if len(code)==6:
        pyautogui.moveTo(ok_p)
        pyautogui.click()
    else:
        pyautogui.moveTo(cancel_p)
        pyautogui.click()


# for int
