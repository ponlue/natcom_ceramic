import json
from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

admin.site.site_header = 'Ceramic Administration'
admin.site.index_title = 'Ceramic Features'

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
        'description'
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
        'id',
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
    search_fields = ("inventory_number", "full_name")
    list_display_links = ('id', 'inventory_number', 'full_name')


class TechniqueMakingPotteryAdmin(admin.ModelAdmin):
    list_display = ('potter_name', 'json_data')
    list_display_links = ('potter_name', 'json_data')

    def potter_name(self, potter_object):
        return potter_object.potter.full_name
    potter_name.short_description = 'Potter fullname'


admin.site.register(TechniqueMakingPottery, TechniqueMakingPotteryAdmin)
admin.site.register(Province, ProvinceAdmin)
class showCategoryAdmin(admin.ModelAdmin):
    fields = ['title','create_at','description']
    list_display=('title', 'create_at', 'description')

class showPostAdmin(admin.ModelAdmin):
    fields = ('category','title','description','body','image','post_photo','create_at')
    list_display=('category_name','title', 'image','post_photo', 'create_at')
    readonly_fields = ['post_photo']
    def category_name(self, instance):
        return instance.category.title

admin.site.register(Categories, showCategoryAdmin)
admin.site.register(PotterPost, showPostAdmin)
admin.site.register(Potter, PotterAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(TypePottery)
admin.site.register(ProvinceImage, ProvinceImageAdmin)
admin.site.register(District)
admin.site.register(Commune)
admin.site.register(Village)
admin.site.register(ToolPottery)
