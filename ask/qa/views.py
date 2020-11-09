from django.shortcuts import render
# Create your views here.
# TEST
from django.http import HttpResponse 
def test(request, *args, **kwargs):
    return HttpResponse('OK')
