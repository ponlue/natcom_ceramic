from django.db import models
from datetime import datetime

from django.db.models import CharField
from django_ckeditor_5.fields import CKEditor5Field


class TypePottery(models.Model):
    title = models.CharField(max_length=25, unique=True)
    # images = models.ManyToManyField(Image)
    diameter = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    thickness = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=20)

    def __str__(self) -> CharField:
        return self.title


class Province(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, unique=True)
    google_map_url = models.URLField(default=None, blank=False, null=True)
    youtube_url = models.URLField(default=None, blank=False, null=True)

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
    

# Store images of Province
class ProvinceImage(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, default=None, blank=True, null=True)
    image = models.ImageField(upload_to = 'province_images/', null=True, blank=True)
    

class Potter(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    inventory_number = models.IntegerField(unique=True)
    created_at = models.DateTimeField(default=datetime.now)
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    dob = models.DateField()
    duration = models.CharField(max_length=255, blank=False, null=True)
    amount_of_pottery = models.PositiveIntegerField()
    inheritance = models.CharField(max_length=255, blank=False, null=True)

    type_of_pottery = models.ForeignKey(TypePottery, on_delete=models.CASCADE, default=1)

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

    describe = CKEditor5Field('Potter Description', config_name='extends', default=None)


class TechniqueMakingPottery(models.Model):
    objects = None
    json_data = models.JSONField(default=None, null=True, blank=True)
    potter = models.ForeignKey(Potter, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name="potter")

    def __str__(self):
        return str('របៀបផលិតរបស់: ' + self.potter.full_name)


class Image(models.Model):
    potter = models.ForeignKey(Potter, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='uploads/')


class ToolPottery(models.Model):
    title = models.CharField(max_length=25, unique=True, null=False, blank=False)
    images = models.ManyToManyField(Image)
    description = models.TextField(blank=True)