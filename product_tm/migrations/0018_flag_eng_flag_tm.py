# Generated by Django 4.1.1 on 2022-11-24 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_tm', '0017_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='eng',
            field=models.ImageField(blank=True, null=True, upload_to='ru_flag/'),
        ),
        migrations.AddField(
            model_name='flag',
            name='tm',
            field=models.ImageField(blank=True, null=True, upload_to='ru_flag/'),
        ),
    ]
