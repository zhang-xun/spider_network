#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = "https://www.nihaowua.com"
base_filename = "result{}.txt"
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
def main():
    file_handle  = open(base_filename.format(0), "a")
    count = 0
    while count < 10000:
        #print(requests.get("http://www.nihaowua.com/").text)
        try:
            content = requests.get("http://www.nihaowua.com/")
            content.encoding = "utf-8"
            soup = BeautifulSoup(content.text, "html.parser")
            text = soup.find("section").find("div").p.get_text()
            print(text)
            file_handle.write(text)
            file_handle.write("\n")
            count -= 1
        except Exception as e:
            continue
    file_handle.close()

if __name__ == "__main__":
    main()
