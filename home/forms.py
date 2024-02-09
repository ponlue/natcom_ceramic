from django import forms
from captcha.fields import CaptchaField
from .models import Potter, TypePottery

class SimpleCaptchaForm(forms.Form):
    captcha = CaptchaField()

class PotterForm(forms.ModelForm):


    GENDER_CHOICES = [
        ('', 'ជ្រើសរើស / Choose'),  # Include an empty option for the default value
        ('M', 'ប្រុស / Male'),
        ('F', 'ស្រី / Female'),
        ('O', 'ផ្សេងៗ / Other'),
    ]


    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control' }),
        label="ភេទ / Gender"
    )
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='ថ្ងៃ ខែ ឆ្នាំ កំណើត / Date of Birth'
    )

    type_of_pottery = forms.ModelChoiceField(
        queryset=TypePottery.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='ជ្រើសរើសប្រភេទកុលាលភាជន៍ / Choose Type of Pottery '
    )

    class Meta:
        model = Potter
        fields = '__all__'
        labels = {
            'inventory_number': 'លេខបញ្ជី / Inventory number',
            'created_at': ' កាលបរិច្ឆេទនៃការចុះបញ្ជី / Date of Inventory ',
            'full_name': 'ឈ្មោះ / Name',
            'duration': 'រយៈពេលនៃការផលិតកុលាលភាជន៍ / Duration',
            'amount_of_pottery': 'ចំនួនស្មូនក្នុងគ្រួសារ / Amount of pottery',
            'inheritance': 'ការបន្តចំណេះ / Inheritance',
        }



    def __init__(self, *args, **kwargs):
        super(PotterForm, self).__init__(*args, **kwargs)

        # Customize the inventory_number field
        self.fields['inventory_number'].widget.attrs.update({
            'placeholder': 'លេខបញ្ជី / Inventory number',
            'class': 'form-control',
        })

        # Customize the created_at field
        self.fields['created_at'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['full_name'].widget.attrs.update({
            'placeholder': '​សូមវាយបញ្ចូល',
            'class': 'form-control',
        })

        self.fields['duration'].widget.attrs.update({
            'placeholder': '​សូមវាយបញ្ចូល',
            'class': 'form-control',
        })

        self.fields['amount_of_pottery'].widget.attrs.update({
            'placeholder': '​សូមវាយបញ្ចូល',
            'class': 'form-control',
        })

        self.fields['inheritance'].widget.attrs.update({
            'placeholder': '​សូមវាយបញ្ចូល',
            'class': 'form-control',
        })
        



