#!/usr/bin/env python
# -*- coding: utf-8 -*-

html = """
<div id="xzTableContent">
    <div class="mem-block">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th style="text-align: center;width: 50px">公示类型</th>
                    <th style="text-align: center;width: 50px">1</th>
                    <th style="text-align: center;width: 50px">2</th>
                    <th style="text-align: center;width: 50px">3</th>
                    <th style="text-align: center;width: 50px">4</th>
                    <th style="text-align: center;width: 50px">5</th>
                    <th style="text-align: center;width: 50px">6</th>
                </tr>
            </head>
        </table>
    </div>
</div>
"""

import requests
from bs4 import BeautifulSoup

def main():
    r = BeautifulSoup(html,"html.parser")
    a = r.find_all("div",attrs={"class":"mem-block"})
    for item in a:
        print(item)

if __name__ == "__main__":
    main()
