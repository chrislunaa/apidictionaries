#rest apis
#application programming interface
import requests #request something from
#the internet
import json # json stands for javascript object notation

response = requests.get("https://randomuser.me/api/")
#print(response.json())
gender = response.json()['results'][0]['gender']
print(gender)
title = response.json()['results'][0]['name']['title']
print(title)
first_name = response.json()['results'][0]['name']['first']
print(first_name)
last_name = response.json()['results'][0]['name']['last']
print(last_name)
email = response.json()['results'][0]['email']
print(email)
phone = response.json()['results'][0]['phone']
print(phone)
location = response.json()['results'][0]['location']['city']
print(location)
postcode = response.json()['results'][0]['location']['postcode']
print(postcode)
street = response.json()['results'][0]['location']['street']
print(street)