# Generated by Django 5.0.1 on 2024-02-16 04:22

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_province_images_provinceimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potter',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Description'),
        ),
    ]