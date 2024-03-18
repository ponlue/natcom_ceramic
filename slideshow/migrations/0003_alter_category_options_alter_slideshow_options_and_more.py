# Generated by Django 4.2 on 2024-03-18 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slideshow', '0002_alter_slideshow_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'SlideShow Category', 'verbose_name_plural': 'SlideShow Category'},
        ),
        migrations.AlterModelOptions(
            name='slideshow',
            options={'verbose_name': 'SlideShow', 'verbose_name_plural': 'SlideShow'},
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('0', 'Active'), ('1', 'Inactive')], default=1, max_length=2),
        ),
    ]
