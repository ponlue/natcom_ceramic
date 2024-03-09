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


class ImageGalleryInline(admin.TabularInline):
    model = ImageGallery



class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'province_image_gallery', 'image')

class ProvinceImageGalleryAdmin(admin.ModelAdmin):
    inlines = [ImageGalleryInline]
    list_display = ('id', 'province', 'title')
    list_display_links = ('id', 'province', 'title', )

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


class PotterImageInline(admin.TabularInline):
    model = Image

class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('រូបភាព / Photos', {
            'fields': (
                'image',
            ),
        }),
    ]

class PotterAdmin(admin.ModelAdmin):
    inlines = [PotterImageInline]

    fieldsets = [
        ('បញ្ជីសារពើភណ្ឌអ្នកផលិតកុលាលភាជន៍ក្នុងប្រទេសកម្ពុជា', {
            'fields': ('inventory_number', 'created_at')
        }),
        ('I.ព័ត៍មានទូទៅរបស់ស្មូន / General information', {
            'fields': (
                'full_name', 
                'gender', 
                'dob', 
                'duration', 
                'amount_of_pottery', 
                'inheritance',
                'type_of_pottery',
            )
        }),
        ('ទីកន្លែងកំណើត / Place of Birth', {
            'fields': (
                'province_of_pob',
                'district_of_pob',
                'commune_of_pob',
                'village_of_pob',
            ),
        }),
        ('លំនៅឋានបច្ចុបន្ន / Current Address', {
            'fields': (
                'province_of_address',
                'district_of_address',
                'commune_of_address',
                'village_of_address',
            ),
        }),
        ('និយាមការផ្ទះ / Coordinate', {
            'fields': (
                'x_coordinate',
                'y_coordinate',
                'url_google_map',
                'youtube_url',
                'describe'
            ),
        }),
    ]

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
        'created_at',
    )
    search_fields = ("inventory_number", "full_name")
    list_display_links = ('id', 'inventory_number', 'full_name')
    list_per_page = 10

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
admin.site.register(ImageGallery, ImageGalleryAdmin)
admin.site.register(ProvinceImageGallery, ProvinceImageGalleryAdmin)
admin.site.register(District)
admin.site.register(Commune)
admin.site.register(Village)
admin.site.register(ToolPottery)
