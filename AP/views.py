from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ap(request):
    return HttpResponse('<b> AMARAVATI IS THE CAPITAL OF ANDHR PRADHES <B/>')
