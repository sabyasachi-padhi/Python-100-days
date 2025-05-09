# in day 89 we are learn about Request module in python.......

# '''the python request module in an HTTP liabrary that enbale devlopers to send HTTP request in python'''
import requests

# for get request in requests module....
response = requests.get("https://www.google.com")

print(response.text)
