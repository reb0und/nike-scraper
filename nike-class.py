import requests


class Input:
    def __init__(inp, sku, region):
        inp.sku = sku
        inp.region = region


uip = Input('', '')


def getUsrInput():
    uip.sku = input('Enter SKU: ')
    uip.region = input('Enter region (US/EU): ')


getUsrInput()


url = "https://api.nike.com/deliver/available_gtins/v3?filter=styleColor({sku})&filter=merchGroup({region})".format(
    sku=uip.sku, region=uip.region)


def go():
    r = requests.request("GET", url)
    print(r.json())


go()
