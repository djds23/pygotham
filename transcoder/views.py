from django.shortcuts import render

from transcoder.static.videos.utils import make_element

def index(request):
    return render(request, 'transcoder/index.html', {
        'error': None,
    })

def twitter_handler(request):
    try:
        twitter_handle = request.POST['twitter_handle']
    except KeyError:
        return render(request, 'transcoder/index.html', {
            'error':'Missing or Invalid Parameters',
        })
    make_element(twitter_handle)
    return render(request, 'transcoder/success.html')
