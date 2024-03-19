from django.contrib import admin
from django import forms
from facebook_live.models import EmbedLive

class EmbedLiveAdminForm(forms.ModelForm):
    """Modify form in djagno admin."""
    STATUS_CHOICES = [
        ('0', 'Active'),
        ('1', 'Inactive'),
    ]

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.RadioSelect(),
        label='Status'
        
    )

    class Meta:
        model = EmbedLive
        fields = '__all__'



class EmbedLiveAdmin(admin.ModelAdmin):
    """ Display such as field to admin site. """


    form = EmbedLiveAdminForm
    list_display = ('id', 'status', 'event_image', 'embed_code', 'description', 'created_at')
    list_display_links = ('id', 'status', 'event_image', 'embed_code', 'description', 'created_at')
    list_per_page = 5


# Register your models here.
admin.site.register(EmbedLive, EmbedLiveAdmin)