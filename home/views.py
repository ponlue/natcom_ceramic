import json
from django.core.files.storage import FileSystemStorage
from django.forms import inlineformset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.views.generic import TemplateView

from home.forms import PotterForm, SimpleCaptchaForm, ImageForm
from home.models import Potter, Image, TechniqueMakingPottery

class HomePageView(TemplateView):
    template_name = "index.html"

def potter_inventory(request):
    # Allows user to upload multitple
    ImageFormSet = inlineformset_factory(
        Potter, 
        Image, 
        form=ImageForm, 
        extra=5, # Specific 2 or 3 of input fields
        can_delete=False,
    )

    if request.method == 'POST':
        forms = PotterForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, instance=Potter())
        captcha_form = SimpleCaptchaForm(request.POST)

        if forms.is_valid() and formset.is_valid() and captcha_form.is_valid():
            titles = request.POST.getlist('title[]')
            descriptions = request.POST.getlist('description[]')
            images = request.FILES.getlist('image[]')

            # Create a folder to store the uploaded images
            fs = FileSystemStorage(location='media/tecniqueofmaking/')

            data_list = []
            for i, title, description, image in zip(titles, descriptions, images):

                # Create a unique filename for each image
                filename = fs.save("tecniqueofmaking_" + i + ".png", image)

                # Get the URL of the saved file
                file_url = fs.url(filename)

                # Create a dictionary with the data including the file path
                data_dict = {'title': title, 'description': description, 'image_url': file_url}
                data_list.append(data_dict)

            technique_list = TechniqueMakingPottery(json_data=data_list)
            potter = forms.save()
            formset.instance = potter
            formset.save()
            data_list = request.POST
            technique_list.save()

            print(f'Status code: {HttpResponse.status_code}')

            # print(data_list)

            # if HttpResponse.status_code == 200:
            #     return HttpResponse('Data received, images saved, and converted to JSON successfully!')


    else:
        forms = PotterForm()
        formset = ImageFormSet(instance=Potter())
        captcha_form = SimpleCaptchaForm()

    return render(request, "ceramic/index.html", {'forms': forms, 'formset': formset, 'captcha_form': captcha_form})
