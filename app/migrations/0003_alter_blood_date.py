# Generated by Django 4.1.2 on 2023-03-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_blood_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood',
            name='Date',
            field=models.DateField(null=True),
        ),
    ]
