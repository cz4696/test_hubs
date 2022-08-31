# -*- coding: utf-8 -*-
"""
Time:2022/8/26 22:08
Author:CAOZHENG
File:get_image.py
"""

import requests
import re
import time


def get_image():
    time_str = time.strftime("%Y_%m_%d_%H_%M_%S")
    word = input('输入关键字:')
    page_size = int(input('输入下载次数:'))
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/78.0.3904.70 Safari/537.36'
    }
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8625941786006681501&' \
          'ipn=rj&ct=201326592&is=&fp=result&fr=&' \
          f'word={word}&queryWord={word}&cl=2' \
          '&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=' \
          '&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1' \
          '&expermode=&nojc=&isAsync=&pn=60&rn=30&gsm=3c&1661522362370='

    res = requests.get(url=url, headers=header)

    data = re.findall('"thumbURL":"(.*?)"', res.text)

    for i in data[:page_size]:
        image = requests.get(i, headers=header)
        with open(r'C:\\Users\OKAI\Pictures\\test\\' + time_str + '.png', 'wb') as f:
            f.write(image.content)
            f.close()


if __name__ == '__main__':
    get_image()
