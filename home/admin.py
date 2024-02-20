from django.contrib import admin
from .models import *
# Register your models here.

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

class showCategoryAdmin(admin.ModelAdmin):
    fields = ['title','create_at','description']
    list_display=('title', 'create_at', 'description')

class showPostAdmin(admin.ModelAdmin):
    fields = ('category','title','description','body','image','post_photo','create_at')
    list_display=('category_name','title', 'image','post_photo', 'create_at')
    readonly_fields = ['post_photo']
    def category_name(self, instance):
        return instance.category.title

admin.site.register(Category, showCategoryAdmin)
admin.site.register(Post, showPostAdmin)
admin.site.register(Potter, PotterAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(TypePottery)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Commune)
admin.site.register(Village)
admin.site.register(TechniqueMakingPottery)
admin.site.register(ToolPottery)
