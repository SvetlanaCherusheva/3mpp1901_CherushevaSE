from django.shortcuts import render

from django.shortcuts import render
from django import template

from django.http import HttpResponse

def home(request):
    return render(request, 'templates/index.html')

def  hello(request):
     return HttpResponse(u'Привет, Мир!!', content_type="text/plain")
	
