from django.db import models
from django.utils.safestring import mark_safe
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    STATUS_CHOICES = [
        ('0', 'Active'),
        ('1', 'Inactive'),
    ]
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return self.name


class SlideShow(models.Model):
    """
        For create, update, delete, and display slideshow 
        in ceramic homepage.-
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=255, null=False, blank=False, default='No title')
    description = CKEditor5Field('Slideshow description', blank=True, null=True, config_name='extends')


    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    slideshow = models.ForeignKey(SlideShow, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='home_slideshow', blank=True, null=True)

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="200" height="" alt="Image Slideshow" />')
        else:
            return "No image uploaded."
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True