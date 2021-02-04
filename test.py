import requests


def call_pylenin(event=None, context=None):
    r = requests.get(
        "https://api.mobireach.com.bd/SendTextMessage?Username=shagor&Password=Sh@g0R21AdmiN&From=adareach&To=8801833182268&Message=FomAWS")
    return r.status_code


print(call_pylenin())
