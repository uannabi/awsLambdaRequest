import requests
from datetime import datetime
from pytz import timezone

BD = timezone('Asia/Dhaka')
# list =['8801553084509','8801825295827','8801938388871','8801717502174']
# https://api.mobireach.com.bd/SendTextMessage?Username=shagor&Password=m@MeN@07aDmIn&From='+ Masking +'&To='+ list +'&Message=
def call_pylenin(event=None, context=None):
    tm1 = datetime.now(BD).strftime("%H:%M:%S")
    tm2 = datetime.now(BD).strftime("%H:%M:%S")
    tm3 = datetime.now(BD).strftime("%H:%M:%S")
    tm4 = datetime.now(BD).strftime("%H:%M:%S")
    musking = 'SMART LAB'
    txt1 = 'CES SMS System'
    url1 = 'https://api.mobireach.com.bd/SendTextMessage?Username=shagor&Password=m@MeN@07aDmIn&From='+ musking + '&To=8801553084509&Message=' + tm1 + ' ' + txt1 + ' OK'
    url2 = 'https://api.mobireach.com.bd/SendTextMessage?Username=shagor&Password=m@MeN@07aDmIn&From=' + musking + '&To=8801825295827&Message=' + tm2 + ' ' + txt1 + ' OK'
    url3 = 'https://api.mobireach.com.bd/SendTextMessage?Username=shagor&Password=m@MeN@07aDmIn&From=' + musking + '&To=8801938388871&Message=' + tm3 + ' ' + txt1 + ' OK'
    url4 = 'https://api.mobireach.com.bd/SendTextMessage?Username=shagor&Password=m@MeN@07aDmIn&From=' + musking + '&To=8801717502174&Message=' + tm4 + ' ' + txt1 + ' OK'
    r1 = requests.get(url1)
    mobireach = r1.status_code
    r2 = requests.get(url2)
    r3 = requests.get(url3)
    r4=requests.get(url4)
    boomcast2 = r2.status_code
    boomcast3 = r3.status_code
    boomcast4 = r4.status_code


    return mobireach


print(call_pylenin())
