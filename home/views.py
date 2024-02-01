from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = "index.html"

def ceramic_app(request):
    return render(request, "ceramic-app/index.html")

def memoryapp(request):
    pass