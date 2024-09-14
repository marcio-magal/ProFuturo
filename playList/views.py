from django.shortcuts import render

# Create your views here.
def playList(request):
    return render(request, 'playlist.html')

def videoPlayer(request):
    return render(request, 'videoplayer.html')
