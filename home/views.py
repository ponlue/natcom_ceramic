from django.shortcuts import redirect, render
from django.shortcuts import render
from django.views.generic import TemplateView

from home.forms import PotterForm, SimpleCaptchaForm

class HomePageView(TemplateView):
    template_name = "index.html"

def inventory_of_pottery_making(request):
    form = PotterForm()
    if request.POST:
        captcha_form = SimpleCaptchaForm(request.POST)
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
        captcha_form = SimpleCaptchaForm()
        form = PotterForm()
    return render(request, "ceramic-app/index.html", {'form': form, 'captcha_form': captcha_form})

def kampot_view(request):
    return render(request, "kampot/index.html")
