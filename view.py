# -*- coding:utf-8 -*-

import  http.client ,  urllib, json
conn  =  http.client.HTTPSConnection ( 'api.tianapi.com' )   #接口域名
params  =  urllib.parse.urlencode ({ 'key' : '你的APIKEY' , 'astro' : 'taurus' }) 
headers  =  { 'Content-type' : 'application/x-www-form-urlencoded' } 
conn.request ( 'POST' , '/star/index' , params , headers ) 
res  = conn.getresponse() 
data  =  res.read() 
print ( data.decode ( 'utf-8' ))

from liffpy import (
    LineFrontendFramework as LIFF,
    ErrorResponse
)


def main():
    liff_api = LIFF("BAyDRggU9nan1LtebdW+wSh5HiNm1SMuhEtZmBThjPOdoDrfBaKWbd5rOWnsAMUdWkegE9IDLYv5xnbaRXnqV5VRbA0NMDz6dS+pztosDgqp6mqLCduIzbCcbh3EgpCaYkea6BN3xJmkSn/Y9H7Q4wdB04t89/1O/w1cDnyilFU=")

    try:
        # If you want to add LIFF app
        liff_id = liff_api.add(
            view_type="compact",
            view_url="https://{YOUR LIFF-SITE}")
            # 400 Error or 401 Error
        try:
            # If you want to update LIFF app
            liff_api.update(liff_id, 
            view_type="full",
            view_url="https://{YOUR LIFF-SITE}")
        except ErrorResponse as err:
            # 401 Error or 404 Error
            print(err.message)
            return 
    except ErrorResponse as err:
        # 401 Error or 404 Error
        print(err.message)
        return 

    try:
        # If you want to get all LIFF apps
        apps_info = liff_api.get()
        for app_info in apps_info:
            try:
                # If you want to delete LIFF app
                liff_api.delete(app_info["liffId"])
            except ErrorResponse as err:
                # 401 Error or 404 Error
                print(err.message)
                return 
    except ErrorResponse as err:
        # 401 Error or 404 Error
        print(err.message)
        return 

if __name__ == '__main__':
    main()