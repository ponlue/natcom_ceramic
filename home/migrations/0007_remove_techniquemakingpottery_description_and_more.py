# Generated by Django 5.0.1 on 2024-02-12 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_potter_inheritance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techniquemakingpottery',
            name='description',
        ),
        migrations.RemoveField(
            model_name='techniquemakingpottery',
            name='images',
        ),
        migrations.RemoveField(
            model_name='techniquemakingpottery',
            name='title',
        ),
        migrations.AddField(
            model_name='techniquemakingpottery',
            name='json_data',
            field=models.JSONField(default=None, null=True),
        ),
    ]
