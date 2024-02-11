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