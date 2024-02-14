from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.views.generic import TemplateView

from home.forms import PotterForm, SimpleCaptchaForm, ImageForm
from home.models import Potter, Image

class HomePageView(TemplateView):
    template_name = "index.html"

def inventory_of_pottery_making(request):

    # Allows user to upload multitple
    ImageFormSet = inlineformset_factory(
        Potter, 
        Image, 
        form=ImageForm, 
        extra=2, # Specific 2 or 3 of input fields
        can_delete=False,
    )

    if request.method == 'POST':
        forms = PotterForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, instance=Potter())
        captcha_form = SimpleCaptchaForm(request.POST)

        print(f'data list {request.POST}')


        if forms.is_valid() and formset.is_valid() and captcha_form.is_valid():
            # person = forms.save()
            # formset.instance = person
            # formset.save()
            data_list = request.POST
            print(f'data list {data_list}')
        else:
            # Form is not valid, re-render the form with errors
            return render(request, "ceramic-app/index.html", {'forms': forms, 'formset': formset, 'captcha_form': captcha_form})

        # if forms.is_valid() and formset.is_valid():
            # print('Both form are valid.')
      
            # print(f'inventory: {forms.cleaned_data['inventory_number']}')
            # print(f'full_name: {forms.cleaned_data['full_name']}')
            # print(f'gender: {forms.cleaned_data['gender']}')
            # print(f'dob: {forms.cleaned_data['dob']}')
            # print(f'duration: {forms.cleaned_data['duration']}')
            # print(f'amount_of_pottery: {forms.cleaned_data['amount_of_pottery']}')
            # print(f'inheritance: {forms.cleaned_data['inheritance']}')
            # print(f'type_of_pottery: {forms.cleaned_data['type_of_pottery']}')

            # print('--Current address--')
            # print(f'village_of_address: {forms.cleaned_data['village_of_address']}')
            # print(f'commune_of_address: {forms.cleaned_data['commune_of_address']}')
            # print(f'district_of_address: {forms.cleaned_data['district_of_address']}')
            # print(f'province_of_address: {forms.cleaned_data['province_of_address']}')


            # print('--POB--')
            # print(f'village_of_pob: {forms.cleaned_data['village_of_pob']}')
            # print(f'commune_of_pob: {forms.cleaned_data['commune_of_pob']}')
            # print(f'district_of_pob: {forms.cleaned_data['district_of_address']}')
            # print(f'province_of_pob: {forms.cleaned_data['province_of_pob']}')
            # print(f'url_google_map: {forms.cleaned_data['url_google_map']}')


            # print(f'images: {forms.cleaned_data['images']}')
            # forms.save()
    else:
        forms = PotterForm()
        formset = ImageFormSet(instance=Potter())
        captcha_form = SimpleCaptchaForm()

    return render(request, "ceramic-app/index.html", {'forms': forms, 'formset': formset, 'captcha_form': captcha_form})




def kampot_view(request):
    return render(request, "kampot/index.html")
