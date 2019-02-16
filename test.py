import requests
from flask import Flask
import json

app = Flask(__name__)

country = "IN"
year = "2018"
url = "https://calendarific.com/api/v2/holidays?country={}&year={}&api_key=7fb42d57b3f2f2f5e9dce6d5abc8802c2c3350d2".format(country, year)


data = json.loads(requests.get(url).text)
holidays = data['response']['holidays']

for i in holidays:
	print("Name: " + i['name'])
	print("-----------")

