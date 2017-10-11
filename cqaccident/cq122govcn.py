#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import threading 

PAGES = 5
URLS = "http://cq.122.gov.cn/m/viopub/getVioPubList"
payload = {'page': 1, 'per_page': 10}
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
form_data = "page={}&size=20&startTime=&endTime=&gsyw=01"
parms = {"page":1,"size":20,"startTime":"2017-09-10","endTime":"2017-10-10","gsyw":"01"}

def main():
    for i in range(2,PAGES):
        parms["page"] = i
        print(parms)
        r = requests.post(URLS,params=parms,headers=headers) 
        print(r.status_code)
        if r.status_code == requests.codes.ok:
            #with open("text{}.txt".format(i),"w") as p:
            #   p.writelines(r.text)
            #print((r.text))
            #print(r.text["data"]["list"]["content"][0])
            soup = BeautifulSoup(r.text,"html.parser")
            print(soup.prettify())
if __name__ == "__main__":
    main()
