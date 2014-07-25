from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from pytube import YouTube

def home(request):

    return render(request, 'home/home.html')


