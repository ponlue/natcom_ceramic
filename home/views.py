import json
import uuid
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render
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
        potter_form = PotterForm(request.POST)
        formset = image_formset(request.POST, request.FILES, instance=Potter())
        captcha_form = SimpleCaptchaForm(request.POST)

        """
            Getting technique of making pottery as list

        """
        titles = request.POST.getlist('title[]')
        descriptions = request.POST.getlist('description[]')
        images = request.FILES.getlist('image[]')

        if potter_form.is_valid() and formset.is_valid() and captcha_form.is_valid():
            # Create empty dict for store technique data
            technique_list = []

            for title, description, image in zip(titles, descriptions, images):
                # Generate a unique identifier for technique image 
                unique_id = uuid.uuid4().hex

                # Extract file extension
                file_extension = image.name.split('.')[-1]

                # Create unique filename with the unique identifier
                unique_filename = f"{unique_id}.{file_extension}"

                fs = FileSystemStorage(location='media/')

                # Save the image with the unique filename
                filename = fs.save(unique_filename, image)

                # Get the URL of the saved file
                file_url = fs.url(filename)

                # Create a dictionary with the data including the file path
                technique_list.append({
                    'title': title,
                    'description': description,
                    'image_url': file_url
                })

            """
                Getting potter id what TechniqueMakingPottery is belong to potter.
            """

            # Save Potter form data
            potter_instance = potter_form.save()

            # Save the formset with the Potter instance
            formset.instance = potter_instance
            formset.save()

            technique_instance = TechniqueMakingPottery(json_data=technique_list, potter=potter_instance)
            technique_instance.save()

            if HttpResponse.status_code == 200:
                return redirect('/success-submitted')
            else:
                return HttpResponse('An errors occurred while submit!')
    else:
        potter_form = PotterForm()
        formset = image_formset(instance=Potter())
        captcha_form = SimpleCaptchaForm()

    context = {
        'potter_form': potter_form,
        'formset': formset,
        'captcha_form': captcha_form
    }

    return render(request, "ceramic/index.html", context)


def technique_making_potter_list(req):
    # data = list(TechniqueMakingPottery.objects.all().values())
    # print(data)

    query_set = TechniqueMakingPottery.objects.all()
    qs_json = serializers.serialize('json', query_set)


    # json_data = json.dumps(data_object)
    # print(len(json_data))
    # # serialized_data = json.loads(serialize('json', queryset))

    # context = {
    #     # 'json_data': serialized_data,
    # }
    # return render(req, 'ceramic/technique.html')
    
    # return JsonResponse({'data': data})    

    return HttpResponse(qs_json, content_type='application/json')




def success_submitted_potter_form(request):
    return render(request, 'ceramic/success.html')