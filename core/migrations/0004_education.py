# Generated by Django 5.0 on 2023-12-20 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_experience_job_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=150)),
                ('degree', models.CharField(max_length=150)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('field_of_study', models.CharField(max_length=150)),
                ('jobseeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.jobseeker')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
                'db_table': 'Education',
            },
        ),
    ]
