from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.


class EmbedLive(models.Model):
    STATUS_CHOICES = [
        ('0', 'Active'),
        ('1', 'Inactive'),
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    event_image = models.ImageField(upload_to='live-events', blank=True, null=True)
    embed_code = models.TextField()
    description = CKEditor5Field('Live Description', config_name='default', default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Live Event'
        verbose_name_plural = 'Live Event'