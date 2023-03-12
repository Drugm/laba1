from django.shortcuts import render
from  django.http import  HttpResponse


def index(request):
    return render(request, 'realtyestateapp/index.html')


def about(request):
    return render (request, 'realtyestateapp/about.html')


def reviews(request):
    return render (request, 'realtyestateapp/reviews.html')


def We(request):
    return render (request, 'realtyestateapp/We.html')
