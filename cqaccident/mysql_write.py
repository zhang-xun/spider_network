#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql.cursors

def main():
connection = pymysql.connect(host="localhost",user="root",password="yananshimeinv",db="driver_accident",charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql = "INSERT into `publicity`(`id`,`decide_number`,`case_name`,`driver_name`,`car_kind`,`punish_result`) values(%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql,("1","2","3","4","5","6","7"))

    connection.commit()
except Exception as e:
    print("error ")
if __name__ == "__main__":
    main()
