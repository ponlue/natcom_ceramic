from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = "index.html"

def ceramic_app(request):
    return render(request, "ceramic-app/index.html")

def BlogPageView(request):
    return render(request, "blog-single.html")

def KompotPageView(request):
    return render(request, "post/kompot.html")


def memoryapp(request):
    pass