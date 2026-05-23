from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h1> B1 is best </h1>')
def user(request):
    return HttpResponse('<h1> Welcome User </h1>')
def page1(request):
    return render(request,'1.html')
def p1(request):
    return render(request,'p1.html')
