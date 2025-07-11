# Generated by Django 5.1.3 on 2025-04-08 08:28

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/', validators=[core.models.validate_image_file]),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='videos/', validators=[core.models.validate_video_file]),
        ),
    ]
