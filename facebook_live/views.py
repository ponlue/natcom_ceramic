from django.shortcuts import render
from django.views.decorators.http import require_GET
from .models import EmbedLive


@require_GET
def fb_live(request):
    content = EmbedLive.objects.filter(status='0').get
    return render(request, 'facebooklive/embed.html' , {'content': content})