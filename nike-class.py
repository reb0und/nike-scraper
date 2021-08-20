import json_parser
import requests


class Input:
    def __init__(inp, sku, region):
        inp.sku = sku
        inp.region = region


class Headers:
    payload = {}
    headers = {
        'authority': 'api.nike.com',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'accept': '*/*',
        'origin': 'https://www.nike.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.nike.com/',
        'accept-language': 'en-US,en;q=0.9',
    }


hdrs = Headers()

uip = Input('CZ0328-400', 'EU')

url = "https://api.nike.com/deliver/available_gtins/v3?filter=styleColor({sku})&filter=merchGroup({region})".format(
    sku=uip.sku, region=uip.region)


response = requests.request("GET", url, headers=hdrs.headers)


data = json_parser.parse(response.text)

# You can manipulate this data however you want from this point on
# You can also remove the json_parser and use your own thing or do what you want

print(data)
