import requests


class Input:
    def __init__(inp, sku, region):
        inp.sku = sku
        inp.region = region


uip = Input('DJ1034-200', 'EU')

url = "https://api.nike.com/deliver/available_gtins/v3?filter=styleColor({sku})&filter=merchGroup({region})".format(
    sku=uip.sku, region=uip.region)


def go():
    r = requests.request("GET", url)
    print(r.json())
go()

