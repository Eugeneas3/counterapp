from http.client import HTTPResponse
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

def index(requests):
    return render(requests, 'index.html')

def counter(requests):
    text = requests.GET['text']
    amount_of_words = len(text.split())
    return render(requests, 'counter.html',{'amount':amount_of_words})

# Create your views here.
