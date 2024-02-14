from typing import Any
from django import forms
from captcha.fields import CaptchaField
from .models import Commune, District, Image, Potter, Province, TypePottery, Village

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
        label="ភេទ / Gender",
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


    # Current address form field customization

    province_of_address = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='ជ្រើសរើសខេត្ត / Choose Province '
    )
    district_of_address = forms.ModelChoiceField(
        queryset=District.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='ជ្រើសរើសស្រុក / Choose District '
    )
    commune_of_address = forms.ModelChoiceField(
        queryset=Commune.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='ជ្រើសរើសឃុំ / Choose Commune '
    )
    village_of_address = forms.ModelChoiceField(
        queryset=Village.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='ជ្រើសរើសភូមិ / Choose Village '
    )

    # End current address form field customization


    # POB form field customization

    province_of_pob = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='ជ្រើសរើសខេត្ត / Choose Province POB'
    )
    district_of_pob = forms.ModelChoiceField(
        queryset=District.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='ជ្រើសរើសស្រុក / Choose District POB'
    )
    commune_of_pob = forms.ModelChoiceField(
        queryset=Commune.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='ជ្រើសរើសឃុំ / Choose Commune POB'
    )
    village_of_pob = forms.ModelChoiceField(
        queryset=Village.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='ជ្រើសរើសភូមិ / Choose Village POB'
    )

    # POB form field customization


    # images = forms.ModelChoiceField(
    #     queryset=Image.objects.all(),
    #     widget=forms.Select(attrs={'class': 'form-control'}),
    #     label='រូបភាព / Photo'
    # )

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
            'url_google_map': 'តំណភ្ជាប់ / Links'
        }

        error_messages = {
            'inventory_number': {
                'required': 'សូមបញ្ចូលលេខបញ្ជី / Pleas input inventory number',
                'invalid': 'សូមបញ្ចូលលេខបញ្ជីឲ្យបានត្រឹមត្រូវ',
                'unique': 'លេខបញ្ជីមានរួចហើយ / Inventory number already exist!',
            },

            'full_name': {
                # 'required': 'សូមបញ្ចូលលេខបញ្ជី / Pleas input inventory number',
                # 'invalid': 'Invalid input for Field 1. Please enter a valid value.',
                'max_length': 'សូមបញ្ចូលឈ្មោះឲ្យតិចជាង ២៥៥ តួអក្សរ / Max length 255',
            },

            'url_google_map': {
                'required': 'សូមបញ្ចូលលេខបញ្ជី / Pleas input inventory number',
                # 'invalid': 'Invalid input for Field 1. Please enter a valid value.',
                # 'max_length': 'Field 1 must be at most 50 characters long.',
                'unique': 'សូមបញ្ចូលតំណភ្ជាប់ឲ្យបានត្រឹមត្រូវ / Please input correct link or url',
            },
        }




    def __init__(self, *args, **kwargs):
        super(PotterForm, self).__init__(*args, **kwargs)
        # self.error_class = jQueryUiErrors

        # Customize the inventory_number field
        self.fields['inventory_number'].widget.attrs.update({
            'placeholder': 'លេខបញ្ជី / Inventory number',
            'class': 'form-control',
        })

        # self.fields['inventory_number'].required = False

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
        
        self.fields['url_google_map'].widget.attrs.update({
            'placeholder': '​សូមវាយបញ្ចូល or Copy & Paste',
            'class': 'form-control',
        })


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }