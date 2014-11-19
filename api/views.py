from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from pprint import pprint

base_url = 'http://theculture.wikia.com/api/v1/'

def categories(request):
	r = requests.get(base_url + 'Articles/List?expand=1&category=The_Culture_Universe')
	return HttpResponse(r.text)

def category(request, slug):
	r = requests.get(base_url + 'Articles/List?expand=1&category=' + slug)
	return HttpResponse(r.text)

def article(request, id):
	r = requests.get(base_url + 'Articles/AsSimpleJson?id=' + id)
	return HttpResponse(r.text)

def search(request, term, batch):
	r = requests.get(base_url + 'Search/List?query=' + term + '&batch=' + batch + '&limit=10')
	return HttpResponse(r.text)
