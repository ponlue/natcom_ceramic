from django.contrib import admin
from .models import HomeSlideShow


class SlideshowAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag')

admin.site.register(HomeSlideShow, SlideshowAdmin)
