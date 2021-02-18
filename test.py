import requests
from datetime import datetime
from pytz import timezone
BD=timezone('Asia/Dhaka')

def call_pylenin(event=None, context=None):
    tm1 = datetime.now(BD).strftime("%H:%M:%S")
    musking = 'Hourly Mont'
    txt1 = 'ada reach system'
    url1 = 'https://api.mobireach.com.bd/SendTextMessage?Username=shagor&Password=Sh@g0R21AdmiN&From=adareach&To=8801825295827&Message=' + tm1 + ' ' + txt1 + ' OK'
    r1 = requests.get(url1)
    mobireach = r1.status_code

    tm2 = datetime.now(BD).strftime("%H:%M:%S")
    txt2 = 'boomcast system'
    url2 = ('http://45.249.101.2/boomcast/WebFramework/boomCastWebService/externalApiSendSMSMobiReach?masking='+musking+'&userName=robimobireach&password=ec9fdbc5aa84840418b1a5c315655835&MsgType=UNICODE&receiver=8801717502174&message=' + tm2 + ' ' + txt2 + ' OK')
    r2 = requests.get(url2)
    boomcast = r2.status_code


    return mobireach,boomcast
print(call_pylenin())
