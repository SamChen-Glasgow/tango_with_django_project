from re import A
from urllib import response
from xml.etree.ElementInclude import include
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)
    

def about(request):
    return render(request, 'rango/about.html')
    # return HttpResponse("Rango says here is the about page." + '<a href=\'/rango/\'>Index</a>')
