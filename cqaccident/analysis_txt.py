#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
import sys
import os
import pymysql.cursors

DETAIL_URL = "http://cq.122.gov.cn/m/viopub/getVioPubDetail"
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
params = {"id":None}

connection = pymysql.connect(host="localhost",user="root",password="yananshimeinv",db="driver_accident",charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)

def main():
    for i in range(2,790):
        filename = "text{}.txt".format(i)
        d2 = json.load(open(filename))
        for j in range(20):
            ids = (d2["data"]["list"]["content"][j]["id"])
            
            gsjdsbh = d2["data"]["list"]["content"][j]["gsjdsbh"]
            gsajmc = d2["data"]["list"]["content"][j]["gsajmc"] #案件名称
            driver = d2["data"]["list"]["content"][j]["gsjsrxm"] #驾驶人姓名
            gshpzl = d2["data"]["list"]["content"][j]["gshpzl"]  #号牌种类
            gshphm = d2["data"]["list"]["content"][j]["gshphm"] #车牌号码
            gscfjg = d2["data"]["list"]["content"][j]["gscfjg"] #处罚结果
            print("id:{}\n 决定书编号:{},\n 案件名称:{}\n 驾驶人姓名:{}\n 号牌种类:{}\n 车牌号码:{} \n 处罚结果:{}\n\n\n".format(ids,gsjdsbh,gsajmc,driver,gshpzl,gshphm,gscfjg))
            
            params["id"] = ids

            r = requests.post(DETAIL_URL,params=params,headers=headers)
            print(r.status_code)
            if r.status_code == requests.codes.ok:
                Save_dir = "./page_detail{}".format(i)
                detail_filename = "text_{}detail.txt"
                if os.path.exists(Save_dir) is False:
                    os.makedirs(Save_dir)
                detail_filename  = Save_dir + "/" + detail_filename.format(j)
                with open(detail_filename,"w") as f:
                    f.writelines(r.text)

                detail_dict = json.load(open(detail_filename))
                punish_truth = detail_dict["data"]["gscfss"]   # 处罚事实
                social_credit_code = detail_dict["data"]["gsshxydm"]  # 社会信用号
                date_time = detail_dict["data"]["gscfrq"]   #时间
                
                print("id:{}\n处罚事实:{}\n社会信用代码:{}\n时间:{}".format(ids,punish_truth,social_credit_code,date_time))


            # write into database

            try:
                with connection.cursor() as cursor:
                    sql = "INSERT into `publicity`(`id`,`decide_number`,`case_name`,`driver_name`,`car_kind`,`car_number`,`punish_result`) values(%s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql,(ids,gsjdsbh,gsajmc.encode("utf-8"),driver.encode("utf-8"),gshpzl.encode("utf-8"),gshphm.encode("utf-8"),gscfjg.encode("utf-8")))

                connection.commit()
            except Exception as e:
                print(e)
                print("error in insert publicity")
                        
            try:
                with connection.cursor() as cursor:
                    sql = "INSERT into `punish_detail`(`id`,`pulish_truth`,`social_credit_code`,`date_time`) values( %s, %s, %s, %s)"
                    cursor.execute(sql,(ids, punish_truth.encode("utf-8"),social_credit_code,date_time.encode("utf-8")))

                connection.commit()
                
            except Exception as e:
                print(e)
                print("error insert pulish_detail ")
    connection.close()
if __name__ == "__main__":
    main()
