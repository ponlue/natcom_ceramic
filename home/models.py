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

class TypePottery(models.Model):
    title = models.CharField(max_length=25, unique=True, null=False, blank=False)
    images = models.JSONField()
    diameter = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    thickness = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=20)

class TechniqueMakingPottery(models.Model):
    title = models.CharField(max_length=25, unique=True, null=False, blank=False)
    images = models.JSONField()
    description = models.TextField(blank=True)

class ToolPottery(models.Model):
    title = models.CharField(max_length=25, unique=True, null=False, blank=False)
    images = models.JSONField()
    description = models.TextField(blank=True)

class Potter(models.Model):
    inventory_number = models.IntegerField(unique=True)
    created_at = models.DateTimeField(default=datetime.now)
    full_name = models.CharField(max_length=255)  
    gender = models.CharField(max_length=2)
    dob = models.DateField()
    duration = models.PositiveIntegerField()
    amount_of_pottery = models.PositiveIntegerField()  # Use PositiveIntegerField for non-negative values

    village_of_address = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='village_of_address')
    commune_of_address = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='commune_of_address')
    district_of_address = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district_of_address')
    province_of_address = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='province_of_address')
    
    village_of_pob = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='village_of_pob')
    commune_of_pob = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='commune_of_pob')
    district_of_pob = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district_of_pob')
    province_of_pob = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='province_of_pob')
    
    # Images of potter
    images = models.JSONField()

class Image(models.Model):
    potter = models.ForeignKey(Potter, on_delete=models.CASCADE) # Image FK to Potter
    type_of_pottery = models.ForeignKey(TypePottery, on_delete=models.CASCADE) # FK to TypeOfPottery table
    tool_of_pottery = models.ForeignKey(ToolPottery, on_delete=models.CASCADE) # FK to ToolPottery table
    image_url = models.URLField()
