# Generated by Django 4.2 on 2024-02-07 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='post_body',
        ),
    ]
