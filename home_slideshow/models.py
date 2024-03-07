from django.db import models
from django.utils.safestring import mark_safe

class HomeSlideShow(models.Model):
    """
        For create, update, delete, and display slideshow 
        in ceramic homepage.
    """
    image = models.ImageField(upload_to='home_slideshow', blank=True, null=True)

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="200" height="" alt="Image Slideshow" />')
        else:
            return "No image uploaded."

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True