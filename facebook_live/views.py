from django.shortcuts import render

def fb_live(request):
    return render(request, 'facebooklive/embed.html')