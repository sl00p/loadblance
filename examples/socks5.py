#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re


def fun():
    proxy = {
        "http": "socks5://127.0.0.1:1081",
        "https": "socks5://127.0.0.1:1081"
    }

    r = requests.get("http://www.baidu.com/s?wd=我的ip", proxies=proxy)
    r.encoding = "utf-8"
    try:
        pattern = re.compile(u"我的ip地址(.*?)。查ip", re.S)
        items = re.findall(pattern, r.text)
        print(items)
    except:
        print("[E]: Content is not right.")

if __name__ == "__main__":
    fun()