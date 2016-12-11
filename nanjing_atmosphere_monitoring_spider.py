#!/usr/local/bin/python3
# _*_ coding:utf-8  _*_ 

import requests 
import bs4
from bs4 import BeautifulSoup
import time
import re
import os


headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"en-US,en;q=0.5",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"

}



def login(username,passwd):
    data = {
            'username':username,
            'password':passwd,
            'btnSubmit':""
    }

    session = requests.session()
    html = session.get("http://58.213.159.173/Login.aspx",headers=headers).text
    #print("header",html.headers)
    #print("cookie",html.request.headers)
    
    soup = BeautifulSoup(html,'lxml')
    data['__VIEWSTATE']=soup.find('input',id='__VIEWSTATE').get('value')
    data['__VIEWSTATEGENERATOR']= soup.find('input',id="__VIEWSTATEGENERATOR").get('value')
    data['__EVENTVALIDATION']=soup.find('input',id='__EVENTVALIDATION').get('value')
    session.post('http://58.213.159.173/Login.aspx',data=data,headers=headers)

    return session

def crawl(session,filedir):
    try:
        os.mkdir(filedir)
    except:
        pass
    #os.chdir(filedir)

    html = session.get('http://58.213.159.173/Atmosphere/left.aspx',headers=headers).text
    table = bs4.BeautifulSoup(html,'lxml').find('div',id='TreeView1n0Nodes').find_all('td',{'class':"TreeView1_3"})
    
    sites={}
    for item in table:
        try:
            name=item.find('a').get_text()
            amdb_Js_station_id=re.findall("doGet\('','(\d+)'\)", str(item) )[0]
        except:
            continue

        sites[name]=amdb_Js_station_id

    for site in sites:
        count = 0
        while True:
            try:
                get_data(session,filedir,site,sites)
                break
            except:
                count+=1
                if count == 3:
                    break

def get_data(session,filedir,site,sites):
    html = session.get("http://58.213.159.173/Atmosphere/view/HistoryDataList.aspx",cookies={'amdb_Js_station_id':sites[site]},headers=headers)
    count = 0
    filename = str(site)+str(count)+".txt"

    os.chdir(filedir)
    with open(filename,'w') as f:
        f.writelines(html.text)
        os.chdir(os.path.pardir)
    soup = BeautifulSoup(html.text,'lxml')
    inputs = soup.find_all('input')
    data={}








def main():
    users = ['nj-nj','sz-sz','wx-wx','cz-cz','yz-yz','nt-nt','xz-xz','tz-tz','yc-yc','ha-ha',
            'lyg-lyg','sq-sq']
    for item in users:
        user=item.split('-')
        session = login(user[0],user[1])
        
        crawl(session,item)

if __name__ == "__main__":
    main()
