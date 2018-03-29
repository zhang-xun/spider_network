#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import argparse
#parser = argparse.ArgumentParser(description="argparse test for xclient start above 5000")
#parser.add_argument("above_number",type=1)
#parser.add_argument("-maxnumber",default=1000, type=1)
#parser.parse_args()

import requests
from bs4 import BeautifulSoup
beforelink = "http://openaccess.thecvf.com"
base_url = "http://openaccess.thecvf.com/CVPR2017.py"
page = 0
cookies = "ef32a55af4310acfa6c3041934ac804c"
filename = "./pdflink.txt"
def main():
    writefile = open(filename,"w")
    r = requests.get(base_url)
    print(r.text)
    #print(r.encoding)
    #print(r.cookies)
    #print(r.headers['Content-Encoding'])
    #with open("xclient{}.txt".format(i),"w") as p:
    #   p.write(r.text)
    soup = BeautifulSoup(r.text,"html.parser")
    for link in soup.find_all("dd"):
        #print(link["class"])
        a = link.find("a")
        afterlink = (a.get("href"))
        if afterlink == "#":
            continue
        #print(len(a))
        writefile.write(beforelink+"/"+afterlink)
        writefile.write("\n")
    writefile.close()

if __name__ == "__main__":
    main()
