from django.http import HttpResponse
from django.shortcuts import redirect, render
from home.models import Potter
from .forms import PotterForm2, ImageFormSet, TechniqueMakingPotteryFormSet, RecaptchaForm
from django.views.decorators.http import require_http_methods
from django.contrib import messages

@require_http_methods(['GET', 'POST'])
def potter2(request):

    if request.method == 'POST':
        potter2_form = PotterForm2(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES, instance=Potter())
        technique_making_pottery_formset = TechniqueMakingPotteryFormSet(request.POST, request.FILES, instance=Potter())
        recaptcha_form = RecaptchaForm(request.POST)

        if potter2_form.is_valid() and image_formset.is_valid() and technique_making_pottery_formset.is_valid() and recaptcha_form.is_valid():
            p_instance = potter2_form.save()
            image_formset.instance = p_instance 
            technique_making_pottery_formset.instance = p_instance
            image_formset.save()
            technique_making_pottery_formset.save()
       
            if HttpResponse.status_code == 200:
                messages.success(
                    request,
                    'ព័ត៍មានបានរក្សាទុកបានជោគជ័យ / Data have been saved successfully!'
                )
                return redirect('/potter2/')

        else:
            potter2_form = PotterForm2()
            image_formset = ImageFormSet(instance=Potter())
            technique_making_pottery_formset = TechniqueMakingPotteryFormSet(instance=Potter())
            recaptcha_form = RecaptchaForm()
    else:
        potter2_form = PotterForm2()
        image_formset = ImageFormSet(instance=Potter())
        technique_making_pottery_formset = TechniqueMakingPotteryFormSet(instance=Potter())
        recaptcha_form = RecaptchaForm()
    context = {
        'potter2_form': potter2_form,
        'image_formset': image_formset,
        'technique_making_pottery_formset': technique_making_pottery_formset,
        'recaptcha_form': recaptcha_form

    }

    return render(request, 'ceramic/potter2.html', context)
   