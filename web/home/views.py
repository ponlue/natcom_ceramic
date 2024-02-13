from django.shortcuts import redirect, render
from django.shortcuts import render
from django.views.generic import TemplateView

from home.forms import CaptchaTestForm
# Create your views here.

class HomePageView(TemplateView):
    template_name = "index.html"

def ceramic_app(request):
    if request.POST:
        form = CaptchaTestForm(request.POST)
        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            human = True
    else:
        form = CaptchaTestForm()

    return render(request, "ceramic-app/index.html", {'form': form})

def kampot_view(request):
    return render(request, "kampot/index.html")
