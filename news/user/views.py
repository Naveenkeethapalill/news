from django.shortcuts import render
from django.http import HttpRequest
import requests
def index(request):
    response1 = requests.get('https://inshorts.deta.dev/news?category=science')
    response2 = requests.get('https://inshorts.deta.dev/news?category=sports')
    response3 = requests.get('https://inshorts.deta.dev/news?category=automobile')
    response4 = requests.get('https://inshorts.deta.dev/news?category=entertainment')
    posts1 = response1.json()
    posts2 = response2.json()
    posts3 = response3.json()
    posts4 = response4.json()
    data1 = posts1['data']
    data2 = posts2['data']
    data3 = posts3['data']
    data4 = posts4['data']
    return render (request,'index.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4})
