# Generated by Django 4.1.1 on 2022-11-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_tm', '0011_aboutus_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Suraty_2'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Suraty_3'),
        ),
    ]
