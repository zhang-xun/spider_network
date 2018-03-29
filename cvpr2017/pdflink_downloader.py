#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import urllib.request 
file =  "./pdflink.txt"

def downloader():
    with open(file) as p:
        for i in p.readlines():
            print(i)
            filenames = i.split("/")[-1]
            response = urllib.request.urlopen(i)
            u =  open('./pdf/'+filenames[:-1],"wb")
            block_sz = 8192
            while True:
                buffers = response.read(block_sz)
                if not buffers:
                    break
                u.write(buffers)
            u.close()
            print ("Sucessful to download" + " " + filenames)

if __name__ == "__main__":
    downloader()
