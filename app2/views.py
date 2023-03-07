from django.shortcuts import render
from django.http import HttpResponse
def first_app2(request):
    return HttpResponse('<h1>This is first view function in app2</h2>')

def second_app2(request):
    return HttpResponse('<h2>This is second view function in app2</h2>')

# Create your views here.
