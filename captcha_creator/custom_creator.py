"""
生成 自定义验证码
"""
import base64
import random
import string
import os

from captcha.image import ImageCaptcha, DEFAULT_FONTS

from my_test import md5file
images_set_path=r'E:\captcha_data\numbe_chars'
ALL_STRING = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
RANDOM_STRING = 'abcdefghijklmnpqrstuvwxyz023456789'
INT_STRING = string.digits
CHARS_STRING = 'abcdefghijklmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ'
print(ALL_STRING)
names = os.listdir('./fonts')
for n in names:
    DEFAULT_FONTS.append('./fonts/'+n)

image = ImageCaptcha()
for _ in range(22000):
    code = ''.join(random.choices(ALL_STRING, k=random.randint(4,6)))
    name=f'{code}.png'
    file_path= os.path.join(images_set_path,name)
    image.write(code,file_path)

    md5_str = md5file(file_path)
    new_name = name[:name.find('.')] + '_' + md5_str + name[name.find('.'):]
    # print(new_name)
    os.rename(file_path, os.path.join(images_set_path, new_name))
    # image_bytes = open(f'Z:\ccc\{code}.png', 'rb').read()
    # r = base64.b64encode(image_bytes).decode('utf-8')
    # print(r)
