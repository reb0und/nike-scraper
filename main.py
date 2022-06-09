import requests
import json
import time
from datetime import datetime


class Input:
    def __init__(inp, sku, region, delay):
        inp.sku = sku
        inp.region = region
        inp.delay = delay


uip = Input('', '', '')


def getUsrInput():
    uip.delay = input('Enter delay: ')
    uip.sku = input('Enter SKU: ')
    uip.region = input('Enter region (US/EU/MX/CA/AU): ')
    return(uip.delay, uip.sku, uip.region)


getUsrInput()


url = "https://api.nike.com/deliver/available_gtins/v3?filter=styleColor({sku})&filter=merchGroup({region})".format(
    sku=uip.sku, region=uip.region)


def go():
    r = requests.request("GET", url)
    data = r.json()
    for x in data["objects"]:
        if x["available"] is True:
            print('[{dt}] - [{sku}] - [{region}] - ***instock***'.format(dt=str(datetime.now()),
                  sku=uip.sku, region=uip.region), x["level"])
        elif x["available"] is False:
            print('[{dt}] - [{sku}] - OOS - [{region}]'.format(dt=str(datetime.now()),
                  sku=uip.sku, region=uip.region))
        print('\---------------------------------------------------------------/')

    time.sleep(int(uip.delay))


while True:
    go()
