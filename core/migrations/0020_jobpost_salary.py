# Generated by Django 5.0 on 2024-01-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_skills_jobpost_number_of_vacancies_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]
