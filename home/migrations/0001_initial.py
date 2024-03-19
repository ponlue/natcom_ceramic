import ckeditor.fields
import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('create_at', models.DateTimeField(default=datetime.datetime.now)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Potter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_number', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('full_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=2)),
                ('dob', models.DateField()),
                ('duration', models.CharField(max_length=255, null=True)),
                ('started_date', models.DateField(default=datetime.datetime.now)),
                ('ended_date', models.DateField(default=datetime.datetime.now)),
                ('amount_of_pottery', models.PositiveIntegerField()),
                ('inheritance', models.CharField(max_length=255, null=True)),
                ('x_coordinate', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('y_coordinate', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('url_google_map', models.URLField(default=None, null=True)),
                ('youtube_url', models.URLField(default=None, null=True)),
                ('describe', ckeditor_uploader.fields.RichTextUploadingField(default=None, verbose_name='Potter Description')),
                ('commune_of_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commune_of_address', to='home.commune')),
                ('commune_of_pob', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commune_of_pob', to='home.commune')),
                ('district_of_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district_of_address', to='home.district')),
                ('district_of_pob', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district_of_pob', to='home.district')),
            ],

            options={
                'verbose_name': 'ស្មូន / Potter',
                'verbose_name_plural': 'ស្មូន / Potter',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('google_map_url', models.URLField(default=None, null=True)),
                ('youtube_url', models.URLField(default=None, null=True)),
                ('description', django_ckeditor_5.fields.CKEditor5Field(default=None, verbose_name='Province Description')),
            ],
        ),
        migrations.CreateModel(
            name='TypePottery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, unique=True)),
                ('diameter', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('thickness', models.DecimalField(decimal_places=2, max_digits=5)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.commune')),
            ],
        ),
        migrations.CreateModel(
            name='ToolPottery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, unique=True)),
                ('description', models.TextField(blank=True)),
                ('images', models.ManyToManyField(to='home.image')),
            ],
        ),
        migrations.CreateModel(
            name='TechniqueMakingPottery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json_data', models.JSONField(blank=True, default=None, null=True)),
                ('title', models.CharField(default='untitle', max_length=200)),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, default='', verbose_name='Description')),
                ('image', models.ImageField(blank=True, default='', upload_to='technique_image/')),
                ('potter', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='potter', to='home.potter')),
            ],
            options={
                'verbose_name': 'របៀបនៃការផលិត / Technique',
                'verbose_name_plural': 'របៀបនៃការផលិត / Technique',
            },
        ),
        migrations.CreateModel(
            name='ProvinceImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitle', max_length=255)),
                ('province', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.province')),
            ],
            options={
                'verbose_name': 'Province-Image-Gallery',
                'verbose_name_plural': 'Province-Image-Galleries',
            },
        ),
        migrations.CreateModel(
            name='ProvinceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='province_images/')),
                ('province', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.province')),
            ],
        ),
        migrations.AddField(
            model_name='potter',
            name='province_of_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='province_of_address', to='home.province'),
        ),
        migrations.AddField(
            model_name='potter',
            name='province_of_pob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='province_of_pob', to='home.province'),
        ),
        migrations.AddField(
            model_name='potter',
            name='type_of_pottery',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.typepottery'),
        ),
        migrations.AddField(
            model_name='potter',
            name='village_of_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='village_of_address', to='home.village'),
        ),
        migrations.AddField(
            model_name='potter',
            name='village_of_pob',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='village_of_pob', to='home.village'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('create_at', models.DateTimeField(default=datetime.datetime.now)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='potter',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.potter'),
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.province'),
        ),
        migrations.AddField(
            model_name='commune',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.district'),
        ),
    ]
