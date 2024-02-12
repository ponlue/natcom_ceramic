from django.db import models
from datetime import datetime

class Province(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    code = models.CharField(max_length=50, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now)

class District(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    code = models.CharField(max_length=50, unique=True, null=False, blank=False)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

class Commune(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    code = models.CharField(max_length=50, unique=True, null=False, blank=False)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

class Village(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    code = models.CharField(max_length=50, unique=True, null=False, blank=False)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

class Image(models.Model):
    image_url = models.ImageField(upload_to = 'uploads/')

class TypePottery(models.Model):
    title = models.CharField(max_length=25, unique=True, null=False, blank=False)
    images = models.ManyToManyField(Image)
    diameter = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    thickness = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.title



class TechniqueMakingPottery(models.Model):
    title = models.CharField(max_length=25, unique=True, null=False, blank=False)
    images = models.ManyToManyField(Image)
    description = models.TextField(blank=True)

class ToolPottery(models.Model):
    title = models.CharField(max_length=25, unique=True, null=False, blank=False)
    images = models.ManyToManyField(Image)
    description = models.TextField(blank=True)


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
    duration = models.PositiveIntegerField()
    amount_of_pottery = models.PositiveIntegerField()  # Use PositiveIntegerField for non-negative values
    inheritance = models.CharField(max_length=255, blank=True)

    type_of_pottery = models.ForeignKey(TypePottery, on_delete=models.CASCADE)

    village_of_address = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='village_of_address')
    commune_of_address = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='commune_of_address')
    district_of_address = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district_of_address')
    province_of_address = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='province_of_address')
    
    village_of_pob = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='village_of_pob')
    commune_of_pob = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='commune_of_pob')
    district_of_pob = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district_of_pob')
    province_of_pob = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='province_of_pob')

    url_google_map = models.URLField(max_length=200)

    
    # Images of potter
    images = models.ManyToManyField(Image)
