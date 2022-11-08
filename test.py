import requests
# from datetime import datetime
# from pytz import timezone

BD = timezone('Asia/Dhaka')


# list =['8801553084509','8801825295827','8801938388871','8801717502174']
# https://api.mobireach.com.bd/SendTextMessage?Username=shagor&Password=m@MeN@07aDmIn&From='+ Masking +'&To='+ list +'&Message=
def call_pylenin(event=None, context=None):
    # tm1 = datetime.now(BD).strftime("%H:%M:%S")
    # tm2 = datetime.now(BD).strftime("%H:%M:%S")
    # tm3 = datetime.now(BD).strftime("%H:%M:%S")
    # tm4 = datetime.now(BD).strftime("%H:%M:%S")
    musking = 'Smart.Lab'
    txt1 = 'CES SMS System'
    url1 = 'https://api.mobireach.com.bd/SendTextMessage?Username=shagor&Password=@M0MeN@@ADm1n@@&From=' + musking + '&To=8801553084509&Message=' + ' ' + txt1 + ' OK'
    url2 = 'https://api.mobireach.com.bd/SendTextMessage?Username=shagor&Password=@M0MeN@@ADm1n@@&From=' + musking + '&To=8801825295827&Message=' + ' ' + txt1 + ' OK'
    url3 = 'https://api.mobireach.com.bd/SendTextMessage?Username=shagor&Password=@M0MeN@@ADm1n@@&From=' + musking + '&To=8801938388871&Message=' + ' ' + txt1 + ' OK'
    url4 = 'https://api.mobireach.com.bd/SendTextMessage?Username=shagor&Password=@M0MeN@@ADm1n@@&From=' + musking + '&To=8801717502174&Message=' + ' ' + txt1 + ' OK'
    url5 = 'https://api.mobireach.com.bd/SendTextMessage?Username=shagor&Password=@M0MeN@@ADm1n@@&From=' + musking + '&To=8801321317989&Message=' + ' ' + txt1 + ' OK'
    url6 = 'https://api.mobireach.com.bd/SendTextMessage?Username=shagor&Password=@M0MeN@@ADm1n@@&From=' + musking + '&To=8801404441730&Message=' + ' ' + txt1 + ' OK'
    r1 = requests.get(url1)
    r2 = requests.get(url2)
    r3 = requests.get(url3)
    r4 = requests.get(url4)
    r5 = requests.get(url5)
    r6 = requests.get(url6)
    mobireach09 = r1.status_code
    mobireach27 = r2.status_code
    mobireach71 = r3.status_code
    mobireach74 = r4.status_code
    mobireach89 = r5.status_code
    mobireach30 = r6.status_code

    return mobireach09, mobireach27, mobireach71, mobireach74, mobireach89, mobireach30


print(call_pylenin())
