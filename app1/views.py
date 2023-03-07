from django.shortcuts import render
from django.http import HttpResponse
def first_app1(request):
    return HttpResponse('<h1>This is first view function in app1</h1>')
def second_app1(request):
    return HttpResponse('<h2>This is second view function in app1</h1>')

# Create your views here.
