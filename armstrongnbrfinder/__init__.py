import requests
from requests import get
def armstrongnbr(number):
    api = (f"https://armstrong-nbr-finder.herokuapp.com/armstrong/{number}")
    text = get(api).text
    print(text)