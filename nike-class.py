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
    uip.sku = input('Enter SKU: ')
    uip.region = input('Enter region (US/EU/MX/CA/AU): ')
    uip.delay = input('Enter delay: ')
    return(uip.sku, uip.region, uip.delay)


getUsrInput()


url = "https://api.nike.com/deliver/available_gtins/v3?filter=styleColor({sku})&filter=merchGroup({region})".format(
    sku=uip.sku, region=uip.region)

rd = open("response.json", "r")


def go():
    r = requests.request("GET", url)
    data = r.json()
    for x in data["objects"]:
        if x["available"] is True:
            print('[{}] instock'.format(
                str(datetime.now())), x["level"])
        elif x["available"] is False:
            print('[{}] oos'.format(
                str(datetime.now())), x["level"])
        print('\-------------------------------------------/')

    time.sleep(int(uip.delay))

    # remove all json loading later
    # clean up and make faster


while True:
    go()
