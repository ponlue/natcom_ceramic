from django.shortcuts import render
from home.models import Potter
from .forms import PotterForm2, ImageFormSet, TechniqueMakingPotteryFormSet, RecaptchaForm
from django.db import DatabaseError
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def potter2(request):
    try:
        if request.method == 'POST':
            recaptcha_form = RecaptchaForm(request.POST)
            pass
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
    except DatabaseError as e:
        msg = 'Error: %s\nPlease contact an administrator' %  e
        print(msg)

   