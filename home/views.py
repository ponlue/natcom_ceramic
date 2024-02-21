import json
from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize
from django.forms import inlineformset_factory
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
from home.forms import PotterForm, SimpleCaptchaForm, ImageForm
from home.models import Potter, Image, TechniqueMakingPottery


def home(request):
    return render(request, 'index.html')


def potter(request):
    image_formset = inlineformset_factory(
        Potter,
        Image,
        form=ImageForm,
        extra=3,
        can_delete=False,
    )
    if request.method == 'POST':
        forms = PotterForm(request.POST)
        formset = image_formset(request.POST, request.FILES, instance=Potter())
        captcha_form = SimpleCaptchaForm(request.POST)
        if forms.is_valid() and formset.is_valid():
            # Getting technique of making pottery as list
            titles = request.POST.getlist('title[]')
            descriptions = request.POST.getlist('description[]')
            images = request.FILES.getlist('image[]')

            # Create a folder to store the uploaded images
            fs = FileSystemStorage(location='media/')

            data_dict = {}
            for title, description, image in zip(titles, descriptions, images):
                # Create a unique filename for each image
                filename = fs.save(title + ".png", image)

                # Get the URL of the saved file
                file_url = fs.url(filename)

                # Create a dictionary with the data including the file path
                data_dict = {
                    'title': title,
                    'description': description,
                    'image_url': file_url
                }

            """
                Getting potter id what TechniqueMakingPottery is belong to potter.
            """
            formset.instance = forms.save()
            formset.save()
            technique_instance = TechniqueMakingPottery(json_data=data_dict, potter=forms.instance)
            technique_instance.save()

            if HttpResponse.status_code == 200:
                return HttpResponse('Data received, images saved, and converted to JSON successfully!')
            else:
                return HttpResponse('An errors occurred while upload!')
        # else:
        #     return HttpResponse('Form invalid!')
    else:
        forms = PotterForm()
        formset = image_formset(instance=Potter())
        captcha_form = SimpleCaptchaForm()

    context = {
        'forms': forms,
        'formset': formset,
        'captcha_form': captcha_form
    }

    return render(request, "ceramic/index.html", context)


def technique_making_potter_list(req):
    queryset = TechniqueMakingPottery.objects.all()
    serialized_data = json.loads(serialize('json', queryset))

    context = {
        'json_data': serialized_data,
    }
    return render(req, 'ceramic/technique.html', context)
