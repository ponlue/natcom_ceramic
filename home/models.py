from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from django.db.models import CharField
from django_ckeditor_5.fields import CKEditor5Field
from ckeditor_uploader.fields import RichTextUploadingField



class Categories(models.Model):
    title = models.CharField(max_length=50, unique=True)
    create_at = models.DateTimeField(default=datetime.now)
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title

class PotterPost(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=50, unique=True)
    body = CKEditor5Field('Post Description', default=None, config_name='extends')
    image = models.ImageField(upload_to='uploads/')
    create_at = models.DateTimeField(default=datetime.now)
    youtube_url = models.URLField(default=None, blank=True, null=True)
    
    def post_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))
    post_photo.short_description = 'image'
    post_photo.allow_tags = True
    
class TypePottery(models.Model):
    title = models.CharField(max_length=25, unique=True)
    diameter = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    thickness = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    color = models.CharField(max_length=20, blank=True)
    

    class Meta:
        verbose_name = 'ប្រភេទកុលាភាជន៍ / Type of Pottery'
        verbose_name_plural = 'ប្រភេទកុលាភាជន៍ / Type of Pottery'
    

    def __str__(self) -> CharField:
        return self.title


class Province(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, unique=True)
    google_map_url = models.TextField(blank=True, null=True)
    youtube_url = models.URLField(default=None, blank=False, null=True)
    description = CKEditor5Field('Province Description', config_name='default', default=None)
    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = "Province"
        #description = CKEditor5Field('Province Description', default=None, config_name='extends')
    # description = RichTextUploadingField(default=None, blank=False, null=True)
    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, unique=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Commune(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Village(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, unique=True)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return self.name    
    

""" Province Image Gallery or Collection Model"""
class ProvinceImageGallery(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=255, null=False, blank=False, default='Untitle')


    class Meta:
        verbose_name = 'Province Image Collection'
        verbose_name_plural = "Province Image Collection"


    def __str__(self) -> str:
        return self.province.name
    

class ImageGallery(models.Model):
    province_image_gallery = models.ForeignKey(ProvinceImageGallery, on_delete=models.CASCADE, default=None, blank=True, null=True)
    image = models.ImageField(upload_to = 'image_gallery/', null=True, blank=True)

    def __str__(self) -> str:
        return self.image.url
    

"""Ended Province Image Gallery or Collection Model"""


# Store images of Province
class ProvinceImage(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, default=None, blank=True, null=True)
    image = models.ImageField(upload_to = 'province_images/', null=True, blank=True)

    class Meta:
        verbose_name = 'រូបភាពនៃខេត្ត / Province Image'
        verbose_name_plural = "Province Image"

class Potter(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    inventory_number = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=datetime.now)
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    dob = models.DateField()
    # duration = models.CharField(max_length=255, blank=False, null=True)
    
    # duration
    started_date = models.DateField(default=datetime.now)
    ended_date = models.DateField(default=datetime.now)
    amount_of_pottery = models.PositiveIntegerField()
    inheritance = models.CharField(max_length=255, blank=False, null=True)

    type_of_pottery = models.ManyToManyField(TypePottery, default=1)

    province_of_pob = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='province_of_pob', null=True, blank=True)
    district_of_pob = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district_of_pob', null=True, blank=True)
    commune_of_pob = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='commune_of_pob', null=True, blank=True)
    village_of_pob = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='village_of_pob', null=True, blank=True)

    province_of_address = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='province_of_address', null=True, blank=True)
    district_of_address = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district_of_address', null=True, blank=True)
    commune_of_address = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='commune_of_address', null=True, blank=True)
    village_of_address = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='village_of_address', null=True, blank=True)

    x_coordinate = models.CharField(max_length=255, default=None, blank=True, null=True)
    y_coordinate = models.CharField(max_length=255, default=None, blank=True, null=True) 

    url_google_map = models.URLField(default=None, blank=False, null=True)
    youtube_url = models.URLField(default=None, blank=False, null=True)
    # describe = CKEditor5Field('Province Description', config_name='default', default=None, config_name='extends')
    #short_description = models.CharField(max_length=255, default=None, null=True, blank=True)
    url_google_map = models.URLField(default=None, blank=True, null=True)
    youtube_url = models.URLField(default=None, blank=True, null=True)
    describe = CKEditor5Field('Potter Description', config_name='default', default='', blank=True)

    class Meta:
        verbose_name = 'Potter'


    url_google_map = models.URLField(default=None, blank=True, null=True)
    youtube_url = models.URLField(default=None, blank=True, null=True)
    describe = CKEditor5Field('ពិពណ៌នា / Description:', config_name='default', default='', blank=True)

    class Meta:
        verbose_name = 'ស្មូន / Potter'
        verbose_name_plural = 'ស្មូន / Potter'


# class TechniqueMakingPottery(models.Model):
#     objects = None
#     json_data = models.JSONField(default="No data", blank=True)
#     potter = models.ForeignKey(Potter, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name="potter")

#     def __str__(self):
#         return str('របៀបផលិតរបស់: ' + self.potter.full_name)
        

class TechniqueMakingPottery(models.Model):
    potter = models.ForeignKey(Potter, on_delete=models.CASCADE, default=None, blank=False, null=False, related_name="potter")
    title = models.CharField(max_length=200, null=False, blank=False, default=None)
    description = CKEditor5Field('Description', config_name='default', default='', blank=True) 
    image = models.ImageField(upload_to='technique_image/', default='', blank=True)

    class Meta:
        verbose_name = "របៀបនៃការផលិត / Technique"
        verbose_name_plural = "របៀបនៃការផលិត / Technique"

    def __str__(self) -> str:
        return  self.potter.full_name
    

class Image(models.Model):
    potter = models.ForeignKey(Potter, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='uploads/')
    class Meta: 
        verbose_name = 'រូបភាពស្មូន / Potter Image'
        verbose_name_plural = 'រូបភាពស្មូន / Potter Image'

class ToolPottery(models.Model):
    title = models.CharField(max_length=25, unique=True, null=False, blank=False)
    images = models.ManyToManyField(Image)
    description = models.TextField(blank=True)
