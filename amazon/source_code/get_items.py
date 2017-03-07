#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import xlwt
import random
from bs4 import BeautifulSoup
import time




class Get_url(object):

    """Docstring for Get_url. """

    def __init__(self,keyword,page):
        """TODO: to be defined1.

        :page: TODO
        :keyword: TODO

        """
        self.session = requests.Session()
        self.page = page
        self.keyword = keyword

    def get_html(self):
        header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, sdch, br",
        "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
        "Connection":"keep-alive",
        "DNT":1 }
        url ="http://guozimami.m.shaibaoj.com/index.php?action=search&q={}&ipage={}".format(self.keyword, str(self.page))
        print(url)
        #html= self.session.get("http://guozimami.m.shaibaoj.com/index.php?action=search&q=" + self.keyword + "&ipage=" + str(self.page)).text
        html = self.session.get(url).text
        #print(type(BeautifulSoup(html)))
        table = BeautifulSoup(html,"lxml").find('div',attrs={'id':"dtk_mian"}).find_all("li")
        #print(type(table))
        #print(len(table))
        #table  = re.findall(re.compile(r'<li(.*?)</li>'),str(table))

        rel = re.compile(r"href='(.*?)'")
        urls = []
        for i,item in enumerate(table):
            s = "http://guozimami.m.shaibaoj.com"+item.a.get("href")
            #print(item)
            #print(i,"th item showed")
            #print(type(item))
            urls.append(s)
        return urls[9:]
            
        

class GetInfo(object):

    """Docstring for GetInfo. """

    def __init__(self,url):
        """TODO: to be defined1. """
        self.url = url
        self.session = requests.Session()
        
        self.name = None
        self.image = None
        self.now_price = None
        self.orignal_price = None
        self.people_of_buyit = None
        ip = "{}.{}.{}.{}".format(str(random.randint(0, 255)),str(random.randint(0, 255)),str(random.randint(0, 255)),str(random.randint(0, 255)))
        self.header = {
        "X-Forwarded-For":ip,
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, sdch, br",
        "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
        "Connection":"keep-alive",
        "DNT":"1"
        }
        

    def getinfo(self):
        html = self.session.get(self.url).text
        soup = BeautifulSoup(html).find("div",attrs={"id":"dtk_mian"})
        if soup == None:
            return
        if  soup.find_all("div",class_="detail-row clearfix")[0].find("div",class_="detail-col").find("div",class_="coupon-wrap clearfix").find("span",class_="now-price").b.next_sibling == None:
            return 'no more discount'
        self.name = soup.find_all("div",class_="detail-row clearfix")[0].find("div",class_="detail-col").a.find("span",class_="title").get_text()
        #print(self.name)
        #print(self.url)
        self.image = soup.find_all("div",class_="detail-row clearfix")[0].a.img.get("src")
        #print(self.image)

        self.now_price = soup.find_all("div",class_="detail-row clearfix")[0].find("div",class_="detail-col").find("div",class_="coupon-wrap clearfix").find("span",class_="now-price").b.next_sibling.next_sibling.i.get_text()
        #print(self.now_price) 
        self.orignal_price = soup.find_all("div",class_="detail-row clearfix")[0].find("div",class_="detail-col").find("div",class_="coupon-wrap clearfix").find("span",class_="org-price").i.get_text()
        #print(self.orignal_price) 
        self.people_of_buyit = soup.find_all("div",class_="detail-row clearfix")[0].find("div",class_="detail-col").find("div",class_="text-wrap").span.next_sibling.next_sibling.i.get_text() 
        #print(self.people_of_buyit)

class WriteExcel(object):

    """Docstring for WriteExcel. """

    def __init__(self):
        """TODO: to be defined1. """
        self.count = 0
        self.workbook = xlwt.Workbook()
        self.sheet = self.workbook.add_sheet("sheet1",cell_overwrite_ok=True)
    
    def writeing(self):
        keyword = input("please input the keyworkd")
        page = input("please input the page")
        for i in range(int(page)):
           urls = Get_url(keyword,i+1).get_html()
           for url in urls:
               item_info = GetInfo(url)
               item_info.getinfo()
               self.sheet.write(self.count,0,item_info.name)
               self.sheet.write(self.count,1,item_info.image)
               self.sheet.write(self.count,2,item_info.url)
               self.sheet.write(self.count,3,item_info.now_price)
               self.sheet.write(self.count,4,item_info.orignal_price)
               self.sheet.write(self.count,5,item_info.people_of_buyit)
               self.count += 1
               self.workbook.save("data.xls")
               print(self.count)
    
def main():
    WriteExcel().writeing()
    





if __name__ == "__main__":
    main()
