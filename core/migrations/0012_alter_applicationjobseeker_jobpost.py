# Generated by Django 5.0 on 2023-12-21 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_rename_user_applicationjobseeker_jobseeker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationjobseeker',
            name='jobpost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.jobpost'),
        ),
    ]
