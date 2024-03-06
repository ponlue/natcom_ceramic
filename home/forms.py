from django import forms
from .models import Commune, District, Image, Potter, Province, TypePottery, Village
from django_ckeditor_5.widgets import CKEditor5Widget
from django_recaptcha.fields import ReCaptchaField

class PotterForm(forms.ModelForm):
    
    GENDER_CHOICES = [
        ('', 'ជ្រើសរើស / Choose'),
        ('M', 'ប្រុស / Male'),
        ('F', 'ស្រី / Female'),
        ('O', 'ផ្សេងៗ / Other'),
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, 
        widget=forms.Select(attrs={'class': '' }),
        label="ភេទ / Gender",
    )
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'class': '', 'type': 'date'}),
        label='ថ្ងៃ ខែ ឆ្នាំ កំណើត / Date of Birth'
    )

    type_of_pottery = forms.ModelChoiceField(
        queryset=TypePottery.objects.all(),
        widget=forms.Select(attrs={'class': ''}),
        label='ប្រភេទកុលាលភាជន៍ / Choose Type of Pottery '
    )

    # Current address form field customization
    province_of_address = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        widget=forms.Select(attrs={'class': ''}),
        label='ខេត្ត / Choose Province '
    )
    district_of_address = forms.ModelChoiceField(
        queryset=District.objects.all(),
        widget=forms.Select(attrs={'class': ''}),
        label='ស្រុក / Choose District '
    )
    commune_of_address = forms.ModelChoiceField(
        queryset=Commune.objects.all(),
        widget=forms.Select(attrs={'class': ''}),
        label='ឃុំ / Choose Commune '
    )
    village_of_address = forms.ModelChoiceField(
        queryset=Village.objects.all(),
        widget=forms.Select(attrs={'class': ''}),
        label='ភូមិ / Choose Village '
    )
    # End current address form field customization

    # POB form field customization
    province_of_pob = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        widget=forms.Select(attrs={'class': ''}),
        label='ខេត្ត / Choose Province POB'
    )
    district_of_pob = forms.ModelChoiceField(
        queryset=District.objects.all(),
        widget=forms.Select(attrs={'class': ''}),
        label='ស្រុក / Choose District POB'
    )
    commune_of_pob = forms.ModelChoiceField(
        queryset=Commune.objects.all(),
        widget=forms.Select(attrs={'class': ''}),
        label='ឃុំ / Choose Commune POB'
    )
    village_of_pob = forms.ModelChoiceField(
        queryset=Village.objects.all(),
        widget=forms.Select(attrs={'class': ''}),
        label='ភូមិ / Choose Village POB'
    )
    # POB form field customization

    describe = forms.CharField(
        label='ពិពណ៍នា / Description',
        widget=CKEditor5Widget(
            config_name='extends',
        )
    )

    def __init__(self, *args, **kwargs):
        super(PotterForm, self).__init__(*args, **kwargs)

        # Customize the inventory_number field
        self.fields['inventory_number'].widget.attrs.update({
            'class': '',
            'placeholder': 'សូមបញ្ចូលលេខបញ្ជី | Inventory number is required',
            'autocomplete': 'off'
        })

    #     # Customize the created_at field
    #     self.fields['created_at'].widget.attrs.update({
    #         'class': '',
    #     })

        self.fields['full_name'].widget.attrs.update({
            'class': '',
            'placeholder': 'សូមបញ្ចូលឈ្មោះស្មូន | Name is required',
            'autocomplete': 'off'

        })

        self.fields['duration'].widget.attrs.update({
            'class': '',
            'placeholder': 'សូមបញ្ចូលរយៈពេល',
            'autocomplete': 'off'


        })

        self.fields['amount_of_pottery'].widget.attrs.update({
            'class': '',
            'placeholder': 'សូមបញ្ចូលចំនួនជាលេខ',
            'autocomplete': 'off'

        })

        self.fields['inheritance'].widget.attrs.update({
            'class': '',
            'placeholder': 'សូមបញ្ចូលការបន្តចំណេះ',
            'autocomplete': 'off'

        })
        
        self.fields['url_google_map'].widget.attrs.update({
            'class': '',
            'placeholder': 'សូមបញ្ចូលតំណភ្ជាប់ | URL google map is required',
            'autocomplete': 'off'

        })

        self.fields['youtube_url'].widget.attrs.update({
            'class': '',
            'placeholder': 'សូមបញ្ចូល | Youtube link is required',
            'autocomplete': 'off'

        })

        self.fields['x_coordinate'].widget.attrs.update({
            'class': '',
            'autocomplete': 'off'

        })
        self.fields['y_coordinate'].widget.attrs.update({
            'class': '',
            'autocomplete': 'off'

        })

        self.fields['x_coordinate'].required = False
        self.fields['y_coordinate'].required = False
        self.fields['duration'].required = False
        self.fields['inheritance'].required = False
        self.fields['describe'].required = False
        self.fields['province_of_pob'].required = False
        self.fields['district_of_pob'].required = False
        self.fields['commune_of_pob'].required = False
        self.fields['village_of_pob'].required = False
        self.fields['province_of_address'].required = False
        self.fields['district_of_address'].required = False
        self.fields['commune_of_address'].required = False
        self.fields['village_of_address'].required = False
        self.fields['describe'].required = False
        self.fields['amount_of_pottery'].required = False


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
            'url_google_map': 'តំណភ្ជាប់ / Google Map',
            'youtube_url': 'តំណភ្ជាប់ / YouTube Link',
        }
        

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        labels = {
            'image': 'រូបថតទូទៅរបស់ស្មូន',
        }
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': ''}),
        }


class RecaptchaForm(forms.Form):
    captcha = ReCaptchaField()
