from django import forms
from captcha.fields import CaptchaField
from .models import Potter

class CaptchaTestForm(forms.Form):
    captcha = CaptchaField()

class PotterForm(forms.ModelForm):
    inventory_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '', 
        'class': 'form-control'
    }))
    class Meta:
        model = Potter
        fields = ['inventory_number']