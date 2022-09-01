# coding=UTF-8
from re import T
from flask import Flask, request, abort
app = Flask(__name__)

from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from pack import *
# import pygsheets
import os, psycopg2
import pandas as pd

line_bot_api = LineBotApi('v0BDiUk0aouFvnlMRc6oZhJmZp/PiTU9nUOPmiSNRx8k93h+j0VZYIDC0tXtOijl+SJxvwxa1VRVW8Cexuc1DjeXPIaGUZ9cQsT0GroDjRhlxrmVFXdD78uNpFswY5gfxDsyBRzV6nsrCgcRoriOfAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7c651b67f436cb7624efb6b02bd51e71')

# database_url = os.popen("heroku config:get DATABASE_URL -a datainnovation").read()[:-1]
# conn = psycopg2.connect(database_url, sslmode="require")
conn = psycopg2.connect(
            database='d67v4hn1akdbf8',
            user='nptohtweqdbtow',
            password='81dd087e8ad2b1d94fe78acd2f2d7df9c6dfe3fd0980820b727faf8fcdc7555e',
            host='ec2-3-234-131-8.compute-1.amazonaws.com',
            port='5432'
        )
cursor = conn.cursor()
cursor.execute("SELECT * FROM agent")
conn.commit()
data = []
while True:
    temp = cursor.fetchone()
    if temp:
        data.append(temp)
    else:
        break
cursor.close()
conn.close()
df1 = pd.DataFrame(data, columns=["name", "region", "address", "phone", "money"])

# gc = pygsheets.authorize(service_file="googlesheetapi.json")
# sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1qqRxyZCNlCRNY0qm_sYk5nLvx5sUEYegSRiJc-ruVhY/edit#gid=0")
# sht = gc.open_by_key("1qqRxyZCNlCRNY0qm_sYk5nLvx5sUEYegSRiJc-ruVhY")
# ws = sht[0]
# df1 = ws.get_as_df(start="A1", index_colum=0, empty_value='', include_tailing_empty=False)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text=="我想要詢問":
        try:
            message = FM1_1()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="老年年金給付請領資格":
        try:
            message = FM1_2()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="老年年金給付請領手續":
        try:
            message = FM1_3()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="老年年金給付核付":
        try:
            message = FM1_4()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="老年年金給付與勞保老年年金關係":
        try:
            message = FM1_5()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="老年基本保證金請領資格":
        try:
            message = FM1_6()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="老年基本保證金請領手續":
        try:
            message = FM1_7()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="老年基本保證金注意事項":
        try:
            message = FM1_8()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="老年基本保證金給付核付":
        try:
            message = FM1_9()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="試算系統":
        try:
            message = FM2_1()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="每月領取":
        try:
            message = FM2_2()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="展延年金":
        try:
            message = FM2_3()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="勞工月退休金":
        try:
            message = FM2_4()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="每月領取A式":
        try:
            message = FM2_5("A1 36300 35.5")
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="每月領取B式":
        try:
            message = FM2_5("B1 33300 35.5")
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="展延年金A式":
        try:
            message = FM2_6("A2 38200 35.5 2.83")
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="展延年金B式":
        try:
            message = FM2_6("B2 42000 35.5 2.83")
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="勞工月退休金金額估算":
        try:
            message = FM2_7()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text[:2]=="A1" or event.message.text[:2]=="a1":
        formula, num1, num2 = event.message.text.split()
        num1 = float(num1)
        num2 = float(num2)
        money = int(round(num1 * num2 * 0.00775 + 3000, 0))
        try:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="預計您每月領取金額為"+str(money)+"元(台幣)"))
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text[:2]=="B1" or event.message.text[:2]=="b1":
        formula, num1, num2 = event.message.text.split()
        num1 = float(num1)
        num2 = float(num2)
        money = int(round(num1 * num2 * 0.0155, 0))
        try:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="預計您每月領取金額為"+str(money)+"元(台幣)"))
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text[:2]=="A2" or event.message.text[:2]=="a2":
        formula, num1, num2, num3 = event.message.text.split()
        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)
        if num3>5:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="最多延展5年，請重新輸入!!!"))
        money = num1 * num2 * 0.00775 + 3000
        money = int(round(money * (1 + 0.04 * num3), 0))
        try:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="預計您每月領取金額為"+str(money)+"元(台幣)"))
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text[:2]=="B2" or event.message.text[:2]=="b2":
        formula, num1, num2, num3 = event.message.text.split()
        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)
        if num3>5:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="最多延展5年，請重新輸入!!!"))
        money = num1 * num2 * 0.0155
        money = int(round(money * (1 + 0.04 * num3), 0))
        try:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="預計您每月領取金額為"+str(money)+"元(台幣)"))
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text[0]=="C" or event.message.text[0]=="c":
        formula, num1, num2 = event.message.text.split()
        num1 = float(num1)
        num2 = float(num2)
        if num2<60:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="年齡必須大於等於60歲，請重新輸入!!!"))
        if num2>=60 and num2<=69:
            factor = 18.55
        if num2>=70 and num2<=79:
            factor = 12.55
        if num2>=80:
            factor = 8.55
        money = int(round((num1 / factor) / 12, 0))
        try:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="預計您每月領取金額為"+str(money)+"元(台幣)"))
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text=="推薦長照":
        try:
            message = FM3_1()
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))
    if event.message.text[0]=="D" or event.message.text[0]=="d":
        formula, address, money = event.message.text.split()
        try:
            message = FM3_2(address, money, df1)
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統錯誤!!!"))

if __name__ == '__main__':
    app.run()