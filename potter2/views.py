from django.http import HttpResponse
from django.shortcuts import redirect, render
from home.models import Potter
from .forms import PotterForm2, ImageFormSet, TechniqueMakingPotteryFormSet, RecaptchaForm
from django.views.decorators.http import require_http_methods
from django.contrib import messages

@require_http_methods(['GET', 'POST'])
def potter2(request):

    if request.method == 'POST':
        print(request.POST)
        potter2_form = PotterForm2(request.POST)
        # image_formset = ImageFormSet(request.POST, request.FILES, instance=Potter())
        # technique_making_pottery_form = TechniqueMakingPotteryFormSet(request.POST, request.FILES, instance=Potter())
        recaptcha_form = RecaptchaForm(request.POST)

        if potter2_form.is_valid() and recaptcha_form.is_valid():
            print(potter2_form)
            potter2_form.save()
            if HttpResponse.status_code == 200:
                    return redirect('/success-submitted')
            else:
                messages.error(
                        request, 
                        'An errors occured while submit the potter application'
                )

    else:
        potter2_form = PotterForm2()
        # image_formset = ImageFormSet(instance=Potter())
        # technique_making_pottery_formset = TechniqueMakingPotteryFormSet(instance=Potter())
        recaptcha_form = RecaptchaForm()

    context = {
        'potter2_form': potter2_form,
        # 'image_formset': image_formset,
        # 'technique_making_pottery_formset': technique_making_pottery_formset,
        'recaptcha_form': recaptcha_form

    }

    return render(request, 'ceramic/potter2.html', context)
   