from django.contrib import admin
from .models import *

class SlideShowImageInline(admin.TabularInline):
    """Allows upload multiple image in Slideshow admin"""
    model = Image


class SlideShowAdmin(admin.ModelAdmin):
    inlines = [SlideShowImageInline]
    list_display = ('id', 'title', 'description', 'category')
    list_per_page = 5
    list_display_links = ('id', 'title', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'status')
    list_per_page = 5


class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = ('id', 'image_tag', 'slideshow')

admin.site.register(SlideShow, SlideShowAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Category, CategoryAdmin)