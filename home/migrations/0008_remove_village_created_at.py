# Generated by Django 5.0.1 on 2024-02-12 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_techniquemakingpottery_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='village',
            name='created_at',
        ),
    ]