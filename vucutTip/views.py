from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def home(request):
  sablon = loader.get_template('vucutTip.html')
  return HttpResponse(sablon.render())

def tipDetay(request):
  return HttpResponse('vucut tipi detay')

def otomatikLink(request,link):
  return HttpResponse(f'{link} sayfasi mevcut degil')