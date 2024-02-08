from django.shortcuts import redirect, render
from django.shortcuts import render
from django.views.generic import TemplateView

from home.forms import CaptchaTestForm, PotterForm
# Create your views here.

class HomePageView(TemplateView):
    template_name = "index.html"

def inventory_of_pottery_making(request):
    form = PotterForm()
    if request.POST:
        # form = CaptchaTestForm(request.POST)
        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            # print('Form is valid')
            inventory_number = request.POST.get('inventory_number')
            created_at = request.POST.get('date_of_inventory')
            full_name = request.POST.get('full_name')
            gender = request.POST.get('gender')
            dob = request.POST.get('dob')

            print(f"invenory_number: {inventory_number}")
            print(f"full_name: {full_name}")
            print(f"gender: {gender}")
            print(f"dob: {dob}")
            print(f"date_of_inventory: {created_at}")

    else:
        # form = CaptchaTestForm()
        form = PotterForm()

    return render(request, "ceramic-app/index.html", {'form': form})

def kampot_view(request):
    return render(request, "kampot/index.html")
