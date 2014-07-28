from django.shortcuts import render_to_response, render
from django.http import HttpResponse

from utils import pull_url
from videogrep import videogrep

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
    filenames = pull_url(url)
    videogrep.videogrep(filenames['filename'], 'output.mp4', search_term, 'pos' )
    return render(request, 'transcoder/success.html')
