#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import argparse
#parser = argparse.ArgumentParser(description="argparse test for xclient start above 5000")
#parser.add_argument("above_number",type=1)
#parser.add_argument("-maxnumber",default=1000, type=1)
#parser.parse_args()

import requests
from bs4 import BeautifulSoup
base_url = "http://xclient.info/s/{}/?_={}"
page = 0
cookies = "ef32a55af4310acfa6c3041934ac804c"
filename = "./above5thousand_software_result.txt"
def main():
    writefile = open(filename,"w")
    for i in range(2,41):
        r = requests.get(base_url.format(i,cookies))
        #print(r.encoding)
        #print(r.cookies)
        #print(r.headers['Content-Encoding'])
        #with open("xclient{}.txt".format(i),"w") as p:
        #   p.write(r.text)
        print("the {} pages ".format(i))
        soup = BeautifulSoup(r.text,"html.parser")
        for link in soup.find_all("ul"):
            #print(link["class"])
            if (link["class"][0]=="post_list"):
                a = link.find_all("li")
                #print(len(a))
                for i in a:
                    b = (i.find("span",class_="item download"))
                    if int(b.get_text()) > 5000:
                        writefile.write(i.find("div",class_="info").h3.get_text())
                        writefile.write("\t"+b.get_text())
                        writefile.write("\n")

        #ul class="post_list"
     

        #i icon-download "13433"

        #lim-icon src

        #a href  title="XXXXX"

    writefile.close()

if __name__ == "__main__":
    main()
