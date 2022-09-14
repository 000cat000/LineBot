from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage
import requests, statistics, json, time
from cgi import test
from flask import Flask, request, abort

from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
import json
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('E2q3tt9gvK/ILqLzKf4drF42Ih3+bG9VRUg+vR1pdMCmiQ6gEPxbMl8R5QyMI66WkOcglJNZTkSlkh/msizYXpK/pIpyyP9eS4f/fxQuORVQwEyvEqmmcD1Ig5dpopuJVAW7/eRNi0VuofWtcKbykAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('06c53dd89138805007c80455f57e7b68')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
cities = ['基隆市','嘉義市','臺北市','嘉義縣','新北市','臺南市','桃園縣','高雄市','新竹市','屏東縣','新竹縣','臺東縣','苗栗縣','花蓮縣','臺中市','宜蘭縣','彰化縣','澎湖縣','南投縣','金門縣','雲林縣','連江縣']


import requests
def getWeather(city):
    tokena = 'CWB-0CB2B120-451C-4417-AE1E-8038A5BE654E'
    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=' + tokena + '&format=JSON&locationName=' + str(city)
    # https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-0CB2B120-451C-4417-AE1E-8038A5BE654E&format=JSON&locationName=臺北市'
    Data = requests.get(url)
    # return Data
    # Data = (json.loads(Data.text,encoding='utf-8'))['records']['location'][0]['weatherElement'] #bug
    Data=json.loads(Data.text)
    #Data = Data['records']['location'][0]['weatherElement']
    Data = Data['records']['location'][0]['weatherElement']
    res = [[] , [] , []]
    for j in range(3):
        for i in Data:
            res[j].append(i['time'][j])
    return res


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '最新合作廠商' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '本日運勢' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '貓咪大戰爭' in msg:
        message = TextSendMessage(text=f'傻眼貓咪')
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '早安' in msg:
        message = TextSendMessage(text=f'芊慧趕快起床要去上班了!')
        line_bot_api.reply_message(event.reply_token, message)

    elif '下班了' in msg:
        message = TextSendMessage(text=f'611公車再3分鐘即將進站')
        line_bot_api.reply_message(event.reply_token, message) 

    elif '家裡有晚餐嗎' in msg:
        message = TextSendMessage(text=f'媽媽有煮一大鍋牛肉麵在廚房等妳趕快回來吃!')
        line_bot_api.reply_message(event.reply_token, message)  
    
    elif '家裡有晚餐嗎?' in msg:
        message = TextSendMessage(text=f'媽媽有煮一大鍋牛肉麵在廚房等妳趕快回來吃!')
        line_bot_api.reply_message(event.reply_token, message)

    elif '好的' in msg:
        message = TextSendMessage(text=f'那等會見，已幫妳準備好餐具和茶杯放桌上。')
        line_bot_api.reply_message(event.reply_token, message)

    elif '我愛你' in msg:
        message = TextSendMessage(text=f'我也愛你')
        line_bot_api.reply_message(event.reply_token, message)

    elif '老公早安' in msg:
        message = TextSendMessage(text=f'老婆早安')
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '老公晚安' in msg:
        message = TextSendMessage(text=f'老婆晚安')
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '誰是大美女' in msg:
        message = TextSendMessage(text=f'宋芊慧')
        line_bot_api.reply_message(event.reply_token, message)

    elif '提摩西' in msg:
        message = TextSendMessage(text="https://www.instagram.com/tchalamet")
        line_bot_api.reply_message(event.reply_token, message)
    elif '我的男神ig' in msg:
        message = TextSendMessage(text="https://www.instagram.com/tchalamet")
        line_bot_api.reply_message(event.reply_token, message)
    else:
        # message = TextSendMessage(text=msg)
        # line_bot_api.reply_message(event.reply_token, message)
        if(msg[:2] == '天氣'):
            city = msg[3:]
            city = city.replace('台','臺')
            if(not (city in cities)):
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text="查詢格式為: 天氣 縣市"))
            else:
                res = getWeather(city)
                #line_bot_api.reply_message(event.reply_token,TextSendMessage(text="123"))
                line_bot_api.reply_message(event.reply_token,TemplateSendMessage(
                    alt_text = city + '未來 36 小時天氣預測',
                    template = CarouselTemplate(
                        columns = [
                            CarouselColumn(
                                thumbnail_image_url = 'https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png',
                                title = '{} ~ {}'.format(res[0][0]['startTime'][5:-3],res[0][0]['endTime'][5:-3]),
                                text = '天氣狀況 {}\n溫度 {} ~ {} °C\n降雨機率 {}'.format(data[0]['parameter']['parameterName'],data[2]['parameter']['parameterName'],data[4]['parameter']['parameterName'],data[1]['parameter']['parameterName']),
                                actions = [
                                    URIAction(
                                        label = '詳細內容',
                                        uri = 'https://www.cwb.gov.tw/V8/C/W/County/index.html'
                                    )
                                ]
                            )for data in res
                        ]
                    )
                ))
        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))


@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data) 


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)



      
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
