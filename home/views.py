import json
from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize
from django.forms import inlineformset_factory
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
from home.forms import PotterForm, SimpleCaptchaForm, ImageForm
from home.models import Potter, Image, TechniqueMakingPottery

from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

from home.forms import PotterForm, SimpleCaptchaForm, ImageForm
from home.models import Potter, Image, Province, Post, ProvinceImage



def HomePageView(request):
    province_list = Province.objects.all()
    potter_list = Potter.objects.all()
    img_list = Post.objects.all()
    internal_list = Post.objects.all().filter(category=1)
    external_list = Post.objects.filter(category=2).all()
    return render(request, "index.html", {
        'province_list':province_list,
        'img_list':img_list,
        'potter_list':potter_list,
        'internal_list':internal_list,
        'external_list':external_list,
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
    province_image = ProvinceImage.objects.all().filter(province=id)
    return render(request, "potter/potter.html",{
        'province_list':province_list,
        'img_list':img_list,
        'potter_list':potter_list,
        'imgpotter':imgpotter,
        'potter_b':potter_b,
        'province':province,
        'province_image':province_image,
        'imgpotter_list':imgpotter_list,
        })

def all_post(request, id):
    province_list = Province.objects.all()
    potter_list = Potter.objects.all()
    img_list = Image.objects.all().order_by('-id')[:3]
    internal_list = Post.objects.all().filter(category=1)
    external_list = Post.objects.all().filter(category=2)
    post_list = get_object_or_404(Post, id=id)
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