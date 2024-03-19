# Generated by Django 4.2 on 2024-03-19 07:01

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmbedLive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', 'Active'), ('1', 'Inactive')], max_length=2)),
                ('event_image', models.ImageField(blank=True, null=True, upload_to='live-events')),
                ('embed_code', models.TextField()),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, default='', null=True, verbose_name='Live Description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Live Event',
                'verbose_name_plural': 'Live Event',
            },
        ),
    ]
