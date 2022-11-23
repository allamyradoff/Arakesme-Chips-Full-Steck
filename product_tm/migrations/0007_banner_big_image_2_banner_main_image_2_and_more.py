# Generated by Django 4.1.1 on 2022-11-23 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_tm', '0006_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='big_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='banner/', verbose_name='Arkadaky surat'),
        ),
        migrations.AddField(
            model_name='banner',
            name='main_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='banner/', verbose_name='Esasy surat'),
        ),
        migrations.AddField(
            model_name='banner',
            name='main_image_3',
            field=models.ImageField(blank=True, null=True, upload_to='banner/', verbose_name='Esasy surat'),
        ),
        migrations.AddField(
            model_name='banner',
            name='name_2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ady'),
        ),
        migrations.AddField(
            model_name='banner',
            name='name_3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ady'),
        ),
        migrations.AddField(
            model_name='banner',
            name='title_2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Beýany'),
        ),
        migrations.AddField(
            model_name='banner',
            name='title_3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Beýany'),
        ),
    ]