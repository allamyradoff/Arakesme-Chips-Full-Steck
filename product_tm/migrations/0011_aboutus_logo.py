# Generated by Django 4.1.1 on 2022-11-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_tm', '0010_mainpagebanners_image_5'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo'),
        ),
    ]
