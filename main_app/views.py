from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Sanity</h1>')

def about(request):
  return HttpResponse('<h1>About Page</h1>')

