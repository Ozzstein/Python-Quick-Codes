import requests
from pprint import pprint

APPID = "ef29e1f100cb2a25ce2fb9f5816faa5d"  # Your key here

params = {'q': 'Sydney,AUS', 'units': 'metric', "APPID": APPID}

response = requests.get(base_url, params=params)
pprint(response.json())

print(response.json()["main"]["temp"])
print(response.json()["sys"]["sunrise"])
