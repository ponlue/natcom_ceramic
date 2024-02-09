# Generated by Django 5.0.1 on 2024-02-08 04:38

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='TechniqueMakingPottery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, unique=True)),
                ('images', models.JSONField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ToolPottery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, unique=True)),
                ('images', models.JSONField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypePottery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, unique=True)),
                ('images', models.JSONField()),
                ('diameter', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('thickness', models.DecimalField(decimal_places=2, max_digits=5)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.district')),
            ],
        ),
        migrations.CreateModel(
            name='Potter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_number', models.IntegerField(unique=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('full_name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=2)),
                ('dob', models.DateField()),
                ('duration', models.PositiveIntegerField()),
                ('amount_of_pottery', models.PositiveIntegerField()),
                ('images', models.JSONField()),
                ('commune_of_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commune_of_address', to='home.commune')),
                ('commune_of_pob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commune_of_pob', to='home.commune')),
                ('district_of_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district_of_address', to='home.district')),
                ('district_of_pob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district_of_pob', to='home.district')),
                ('province_of_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='province_of_address', to='home.province')),
                ('province_of_pob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='province_of_pob', to='home.province')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.province'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('potter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.potter')),
                ('tool_of_pottery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.toolpottery')),
                ('type_of_pottery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.typepottery')),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.commune')),
            ],
        ),
        migrations.AddField(
            model_name='potter',
            name='village_of_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='village_of_address', to='home.village'),
        ),
        migrations.AddField(
            model_name='potter',
            name='village_of_pob',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='village_of_pob', to='home.village'),
        ),
    ]