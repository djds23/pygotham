from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from pytube import YouTube

def index(request):
    return render(request, 'transcoder/index.html', {
        'error': None,
    })

def yt_url_handler(request):
    try:
        url = request.POST['url']
        search_term = request.POST['search_term']
    except KeyError:
        return render(request, 'transcoder/index.html', {
            'error':'Missing or Invalid Parameters',
        })
    return render(request, 'transcoder/processing.html')
