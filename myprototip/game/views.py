from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def indexx(request):
    #print(request)
    return HttpResponse('<h1>Hello world</h1>')

def test(request):
    return HttpResponse('<h1>Test page<h/1>')