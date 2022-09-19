import base64
import hashlib
import os
import random
import string
import uuid
from collections import defaultdict

import ddddocr


def md5file(file_path):
    """
    提取文件 md5
    """
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5()
        chunk = f.read(8192)
        while chunk:
            file_hash.update(chunk)
            chunk = f.read(8192)
        return file_hash.hexdigest()


def first_ocr(images_set_path):
    """
    先用识别跑一编看看识别率
    :return:
    """
    # ocr = ddddocr.DdddOcr(show_ad=False,
    #                       import_onnx_path="projects/india/models/india_1.0_76_7000_2022-04-08-20-44-46.onnx",
    #                       charsets_path="projects/india/models/charsets.json")
    ocr = ddddocr.DdddOcr(show_ad=False, old=True)

    for name in os.listdir(images_set_path):
        file_path = os.path.join(images_set_path, name)
        with open(file_path, 'rb') as f:
            image_bytes = f.read()
            code = ocr.classification(image_bytes)
            if not code:
                print('failed')
                continue
            print(code)
        new_name = os.path.join(images_set_path, code + os.path.splitext(name)[-1])
        if not os.path.isfile(new_name):
            os.rename(file_path, new_name)


def test_models(file_path, import_onnx_path, charsets_path):
    """

    """
    ocr = ddddocr.DdddOcr(ocr=False, show_ad=False,
                          import_onnx_path=import_onnx_path,
                          charsets_path=charsets_path)
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            image_bytes = f.read()
            code = ocr.classification(image_bytes)
            print(code)
    if os.path.isdir(file_path):
        listdir = os.listdir(file_path)
        count = 0
        for name in listdir:
            with open(os.path.join(file_path, name), 'rb') as f:
                image_bytes = f.read()
                code = ocr.classification(image_bytes)
                org_code = name.split('_')[0]
                print(code, org_code)
                if code == org_code:
                    count += 1
        print(count, len(listdir), count / len(listdir))


def add_md5_suffix(images_set_path):
    # images_set_path = "E:\\india_images_set1"
    # images_set_path = "E:\\custom"

    files = os.listdir(images_set_path)
    for name in files:
        if '_' in name:
            print(f'name:{name} 包含 _,captcha len:{len(name[:name.find("_")])}', )
            continue

        file_path = os.path.join(images_set_path, name)
        md5_str = md5file(file_path)
        new_name = name[:name.find('.')] + '_' + md5_str + name[name.find('.'):]
        print(new_name)
        os.rename(file_path, os.path.join(images_set_path, new_name))


def base64tofile():
    """

    """

    splitlines = open('captcha_tmp_file2.txt').read().splitlines()
    print(len(splitlines))
    for line in splitlines:
        print(line)
        ret = base64.b64decode(line.encode('utf-8'))
        open(f'E:\\india_images_set1\\{uuid.uuid4().hex}.png', 'wb+').write(ret)


def remove_duplicates(images_set_path):
    """
    文件去重
    """
    data = defaultdict(list)
    for name in os.listdir(images_set_path):
        file_path = os.path.join(images_set_path, name)
        md5_str = md5file(file_path)
        if data.get(md5_str):
            print(f'remove {file_path}')
            os.remove(file_path)
        else:
            data[md5_str].append(name)


def check_captcha_length(images_set_path, target_len=6):
    """
    检查验证码长度
    """
    files = os.listdir(images_set_path)
    for name in files:
        if '_' in name:
            captcha = name[:name.find("_")]
        else:
            captcha = name[:name.find(".")]
        if len(captcha) != target_len:
            print(name)
        if '1' in captcha:
            print(name)
        if 'o' in captcha:
            print(name)


def image_ocr(file_path):
    """

    """
    ocr = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False, )
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            image_bytes = f.read()
            code = ocr.classification(image_bytes)
            print(code)
    if os.path.isdir(file_path):
        listdir = os.listdir(file_path)
        for name in listdir:
            with open(os.path.join(file_path, name), 'rb') as f:
                image_bytes = f.read()

                code = ocr.classification(image_bytes)
                print(code, name)


if __name__ == '__main__':
    test_models("/Users/lu/Downloads/label",
                import_onnx_path="projects/are/models/are_1.0_554_46000_2022-09-07-00-21-58.onnx",
                charsets_path="projects/are/models/charsets.json")
    # image_ocr("E:\ARE_data")
    # remove_duplicates(images_set_path=r"E:\vermont")
    # first_ocr(images_set_path=r"E:\are2")
    # add_md5_suffix(r'E:\ARE_data')
    # check_captcha_length(r'E:\ARE_data')
