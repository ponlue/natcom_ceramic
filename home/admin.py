import json
from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

admin.site.site_header = 'Ceramic Web Adminstration'

class ProvinceImageInline(admin.TabularInline):
    model = ProvinceImage

class ProvinceAdmin(admin.ModelAdmin):
    inlines = [ProvinceImageInline]

    def display_images(self, obj):
        first_image = obj.provinceimage_set.first()
        if first_image:
            return mark_safe(f'<img src="{first_image.image.url}" width="80" height="80" />')
        return "No Image"

    display_images.short_description = 'Images'

    list_display = (
        'name',
        'code',
        'display_images',
        'google_map_url',
        'youtube_url',
    )

class ProvinceImageAdmin(admin.ModelAdmin):
    list_display = (
        'province',
        'image',
    )

class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'potter',
        'image'
    )

class PotterAdmin(admin.ModelAdmin):

    list_display = (
        'inventory_number', 
        'full_name',
        'gender', 
        'dob', 
        'duration',
        'amount_of_pottery',
        'inheritance',
        'type_of_pottery',
        'province_of_address',
        'province_of_pob',
        'url_google_map',
        'x_coordinate',
        'y_coordinate',
        'created_at',
        # 'description'
    )

admin.site.register(TechniqueMakingPottery)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(Potter, PotterAdmin)
admin.site.register(Image)
admin.site.register(TypePottery)
admin.site.register(ProvinceImage, ProvinceImageAdmin)
admin.site.register(District)
admin.site.register(Commune)
admin.site.register(Village)
admin.site.register(ToolPottery)
