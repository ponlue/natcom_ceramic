from django import forms
from home.models import Potter, Image, TypePottery, TechniqueMakingPottery
from django.forms.models import inlineformset_factory
from django_recaptcha.fields import ReCaptchaField
from django_ckeditor_5.widgets import CKEditor5Widget



class PotterForm2(forms.ModelForm):
    """ test new form of potter inventory """


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

    started_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': '', 'type': 'date'}),
        label='ថ្ងៃចាប់ផ្ដើម / Started date'
    )

    ended_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': '', 'type': 'date'}),
        label='ថ្ងៃបញ្ចប់/ Ended date'
    )

    type_of_pottery = forms.ModelMultipleChoiceField(
        queryset=TypePottery.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label='ប្រភេទកុលាភាជន៍ / Type of pottery'
    )



    def __init__(self, *args, **kwargs):
        super(PotterForm2, self).__init__(*args, **kwargs)

        # Update form attribute
        self.fields['inventory_number'].widget.attrs.update({
            'class': '',
            # 'placeholder': 'បញ្ចូលលេខបញ្ជី | Inventory number is required',
            'autocomplete': 'off'
        })
        self.fields['full_name'].widget.attrs.update({
            'class': '',
            # 'placeholder': 'បញ្ចូលឈ្មោះ | Name is required',
            'autocomplete': 'off'
        })

        self.fields['type_of_pottery'].widget.attrs.update({
            'multiple': True
        })


    class Meta:
        model = Potter
        fields = '__all__'
        labels = {
            'inventory_number': 'លេខបញ្ជី / Inventory number',
            'created_at': ' កាលបរិច្ឆេទនៃការចុះបញ្ជី / Date of Inventory ',
            'full_name': 'ឈ្មោះ / Name',
            'started_date': '',
            'ended_date': '',
            'amount_of_pottery': 'ចំនួនស្មូនក្នុងគ្រួសារ / Amount of pottery',
            'inheritance': 'ការបន្តចំណេះ / Inheritance',
            'url_google_map': 'តំណភ្ជាប់ / Google Map',
            'youtube_url': 'តំណភ្ជាប់ / YouTube Link',
            'gender': 'ភេទ  / Gender',
        }

class ImageForm(forms.ModelForm):
    """Potter image form for using in ImageFormSet."""

    class Meta:
        model = Image
        fields = ['image']
        labels = {
            'image': 'រូបភាពស្មូន / Potter Image',
        }

"""Make image inline when save potter data."""
ImageFormSet = inlineformset_factory(
    Potter, 
    Image, 
    form=ImageForm,
    fields='__all__', 
    extra=1, 
    can_delete=False,
)


class TechniqueMakingPotteryForm(forms.ModelForm):
    """
        -   This Technique class is form represented 
            of how potter making the pottery. 

        -   And for using in techniqe inline formset.
    """
    
    class Meta:
        model = TechniqueMakingPottery
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'ចំណងជើង / Title',
            'description': 'ពិពណ៌នា / Description',
            'image': 'រូបនៃការផលិត / Photo'
            
        }
    

    def __init__(self, *args, **kwargs):
        super(TechniqueMakingPotteryForm, self).__init__(*args, **kwargs)

        self.fields['description'].widget.attrs.update({
            'resize': 'vertical',
            'rows': 8
        })

TechniqueMakingPotteryFormSet = inlineformset_factory(
    Potter,
    TechniqueMakingPottery,
    form=TechniqueMakingPotteryForm,
    fields='__all__',
    extra=1,
    can_delete=False
)


class RecaptchaForm(forms.Form):
    """ For verify I'm not a robot."""
    captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['captcha'].label = "Check to verify me!"
