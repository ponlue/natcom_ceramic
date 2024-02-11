from datetime import datetime
from django.db import models
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Category(models.Model):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null = True, default=datetime.now)

class Post(models.Model):
    id_cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.TextField(blank=True, null=True)
    post_body = RichTextUploadingField(blank=True, null=True)
    images = models.ImageField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)