"""
生成 自定义验证码
"""
import random
import string

from captcha.image import ImageCaptcha, DEFAULT_FONTS

RANDOM_STRING = string.ascii_lowercase + string.digits
fonts = DEFAULT_FONTS.append('fonts/simsunb.ttf')
image = ImageCaptcha(fonts=fonts)
for _ in range(3000):
    code = ''.join(random.choices(RANDOM_STRING, k=5))
    image.write(code, f'E:/custom/{code}.png')
