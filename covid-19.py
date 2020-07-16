"""API for live information about COVID-19

GET https://coronavirus-19-api.herokuapp.com/all -> global info

GET https://coronavirus-19-api.herokuapp.com/countries -> all countries info

GET https://coronavirus-19-api.herokuapp.com/countries/{countryName} -> country specific information
"""
from win10toast import ToastNotifier
import requests
import json
import time

def update_all():
    r=requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data=r.json()
    text = f'Confirmed case : {data["cases"]}\n Death : {data["deaths"]}\n Recovered : {data["recovered"]}'

    while True:
        toaster=ToastNotifier()
        toaster.show_toast("Covid-19 Notification Total",text,duration=10)
        time.sleep(60)

"""def update_countrywise():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/countries')
    data = r.json()
    text = f'Confirmed Cases : {data["cases"]}\n Deaths : {data["deaths"]}\n Recovered: {data["recovered"]}\n Today Cases : {data["todayCases"]}'

    while True:
        toaster=ToastNotifier()
        toaster.show_toast("Covid-19 Notification Countrywise",text,duration=10)
        time.sleep(60)        
"""

def update_country(countryname):
    r=requests.get("https://coronavirus-19-api.herokuapp.com/countries/"+countryname)
    data=r.json()
    text = f'Confirmed Cases : {data["cases"]}\n Deaths : {data["deaths"]}\n Recovered : {data["recovered"]}'

    while True:
        toaster=ToastNotifier()
        toaster.show_toast("Covid-19 Notification of "+countryname,text,duration=10)
        time.sleep(60)

def show():
    print("1. All Countries?")
    print("2 Enter country name:")
    #print("3. Country Wise")
    print("3.Exit")

show()

while True:
    x=int(input("Enter your choice:"))
    if x == 3:
        #update_countrywise()
        break
    elif x == 1:
        update_all()
        break
    elif x == 2:
        countryname=str(input())
        update_country(countryname)
        break
    else:
        print("Wrong choice entered!")
        print("Enter again!")
        show()

