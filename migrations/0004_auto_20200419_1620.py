# Generated by Django 3.0.5 on 2020-04-19 14:20

from django.db import migrations, models
import recette.models


class Migration(migrations.Migration):

    dependencies = [
        ('recette', '0003_auto_20200419_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='photo',
            field=models.ImageField(upload_to=recette.models.recette_directory_path),
        ),
    ]
