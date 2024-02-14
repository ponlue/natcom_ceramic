from django.contrib import admin
from .models import *
# Register your models here.

class showCategory(admin.ModelAdmin):
    fields = ('title', 'description', 'create_at')
    list_display = ('title', 'description', 'create_at')

class showPost(admin.ModelAdmin):
    fields = ('title', 'post_body', 'images', 'create_at')
    list_display = ('title', 'images', 'create_at')

admin.site.register(Category, showCategory)
admin.site.register(Post, showPost)
admin.site.site_header = 'Adminstration'


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
        'amount_of_pottery',
        'inheritance',
        'type_of_pottery',
        'province_of_address',
        'province_of_pob',
        'url_google_map',
        'created_at',
    )

admin.site.register(Potter, PotterAdmin)
admin.site.register(Image, ImageAdmin)

admin.site.register(TypePottery)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Commune)
admin.site.register(Village)
admin.site.register(TechniqueMakingPottery)
admin.site.register(ToolPottery)
