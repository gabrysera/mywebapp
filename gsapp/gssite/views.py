from django.shortcuts import render
from django.http import HttpResponse


def root(request):
    return HttpResponse("<h1>G.S. web site (root)</h1>")
    
def home(request):
    return HttpResponse("<h1>G.S. web site</h1>")

