# Generated by Django 5.0 on 2023-12-20 15:27

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.cover_photo_upload_path),
        ),
    ]