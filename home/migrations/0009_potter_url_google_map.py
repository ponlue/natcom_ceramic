# Generated by Django 5.0.1 on 2024-02-12 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_village_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='potter',
            name='url_google_map',
            field=models.URLField(default=None),
        ),
    ]
