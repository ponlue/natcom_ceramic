import uuid
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from home.forms import PotterForm, RecaptchaForm, ImageForm
from home.models import ImageGallery, Potter, Image, TechniqueMakingPottery
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from home.forms import PotterForm, PotterForm, ImageForm, RecaptchaForm
from home.models import *
from slideshow.models import Image as SlideImage



def HomePageView(request):
    province_list = Province.objects.all()
    potter_list = Potter.objects.all()
    img_list = PotterPost.objects.all()
    internal_list = PotterPost.objects.all().filter(category=1).order_by('-id')
    external_list = PotterPost.objects.all().filter(category=2).order_by('-id')
    upcoming_event = PotterPost.objects.filter(category=3).order_by('-id').first
    slider = SlideImage.objects.all().filter(slideshow=6)[:5]
    event_slider = SlideImage.objects.all().filter(slideshow=7)
    print(slider)
    return render(request, "index.html", {
        'province_list':province_list,
        'img_list':img_list,
        'potter_list':potter_list,
        'internal_list':internal_list,
        'external_list':external_list,
        'slider':slider,
        'upcoming_event':upcoming_event,
        'event_slider':event_slider,
        })

def PotterdetailView(request, id):
    province_list = Province.objects.all()
    potterbody = get_object_or_404(Potter, id=id)
    return render(request,"potter/potterdetail.html", {
        'potterbody':potterbody,
        'province_list':province_list,
        })
    

def all_province(request):
    province_list = Province.objects.all()
    potter_list = Potter.objects.all()
    img_list = Image.objects.all()
    return render(request, "menu/navbar.html", {
        'province_list':province_list,
        'img_list':img_list,
        'potter_list':potter_list,
        })

def all_Potter(request, id ):
    province_list = Province.objects.all()
    province = Province.objects.all().filter(id=id)
    potter_list = Potter.objects.all().filter(province_of_address=id)
    img_list = ProvinceImage.objects.all().filter(province=id).all().order_by('-id')[:3]
    imgpotter = Image.objects.filter(potter=id).order_by('-id')[:3]
    imgpotter_list = Image.objects.all()
    potter_b =Potter.objects.all().filter(id=id)
    slider = ProvinceImage.objects.all().filter(province=id).order_by('-id')[:5]
    image_gallery = ProvinceImageGallery.objects.filter(province=id).all()
    print(image_gallery)
    return render(request, "potter/potter.html",{
        'province_list':province_list,
        'img_list':img_list,
        'potter_list':potter_list,
        'imgpotter':imgpotter,
        'potter_b':potter_b,
        'province':province,
        'image_gallery':image_gallery,
        'imgpotter_list':imgpotter_list,
        'slider':slider,
        })

def all_post(request, id):
    province_list = Province.objects.all()
    potter_list = Potter.objects.all()
    img_list = Image.objects.all()
    internal_list = PotterPost.objects.all().filter(category=1).order_by('-id')
    external_list = PotterPost.objects.all().filter(category=2).order_by('-id')
    post_list = get_object_or_404(PotterPost, id=id)
    return render(request, "post/postbody.html", {
        'province_list':province_list,
        'img_list':img_list,
        'potter_list':potter_list,
        'internal_list':internal_list,
        'external_list':external_list,
        'post_list':post_list,
        })

def home(request):
    return render(request, 'index.html')


@require_http_methods(['GET', 'POST']) # Allow only http request GET & POST 
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
        recaptcha_form = RecaptchaForm(request.POST)

        """
            Getting technique of making pottery as list

        """
        titles = request.POST.getlist('title[]')
        descriptions = request.POST.getlist('description[]')
        images = request.FILES.getlist('image[]')



        """
            - check if recaptcha_form, potter_form and formset is input correctly from
                user and save potter form to database.
            - if not return error otherwise.
        """
        if recaptcha_form.is_valid() and potter_form.is_valid() and formset.is_valid() :
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
                    messages.error(
                        request, 
                        'An errors occured while submit the potter application'
                    )
        else:
            messages.error(
                request, 
                'បញ្ចូលទិន្នន័យមិនបានត្រឹមត្រូវ'
            )

    else:
        potter_form = PotterForm()
        formset = image_formset(instance=Potter())
        recaptcha_form = RecaptchaForm()

    context = {
        'potter_form': potter_form,
        'formset': formset,
        'recaptcha_form': recaptcha_form
    }

    return render(request, "ceramic/index.html", context)


def technique_making_potter_list(req):
    # data = list(TechniqueMakingPottery.objects.all().values())
    # print(data)

    context = {
        'json_data': serialized_data,
    }
    return render(req, 'ceramic/technique.html', context)

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

def image_collection(request):
    img_object = ImageGallery.objects.filter(province_image_gallery=1).values()
    print(img_object)

    return render(request, 'img-collection.html')
