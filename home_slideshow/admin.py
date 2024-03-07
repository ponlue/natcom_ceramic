from django.contrib import admin
from .models import HomeSlideShow


class SlideshowAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag')
    list_per_page = 5

admin.site.register(HomeSlideShow, SlideshowAdmin)
