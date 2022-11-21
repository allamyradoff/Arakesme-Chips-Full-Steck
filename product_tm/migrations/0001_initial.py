# Generated by Django 4.1.1 on 2022-11-19 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='benefits/', verbose_name='Üstünlikleriň suraty')),
                ('title', models.CharField(max_length=50, verbose_name='Üstünlikleriň ady')),
                ('desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='Üstünlikleriň beýany')),
            ],
            options={
                'verbose_name': 'Üstünlik',
                'verbose_name_plural': 'Üstünlikler',
            },
        ),
        migrations.CreateModel(
            name='MainPageBanners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='main_page_banners/', verbose_name='Üstunlikleriň suraty')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='main_page_banners/', verbose_name='Üstunlikleriň suraty_2')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='main_page_banners/', verbose_name='Üstunlikleriň suraty_3')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news/')),
                ('desc', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Täzelik',
                'verbose_name_plural': 'Täzelikler',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('desc', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Haryt',
                'verbose_name_plural': 'harytlar',
            },
        ),
        migrations.CreateModel(
            name='TopThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_tm.product')),
            ],
            options={
                'verbose_name': 'Meşhur haryt',
                'verbose_name_plural': 'Iň meşhur harytlar',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ady')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Beýany')),
                ('big_image', models.ImageField(blank=True, null=True, upload_to='banner/', verbose_name='Arkadaky surat')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='banner/', verbose_name='Esasy surat')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_tm.product', verbose_name='Haýsy haryda degişli')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Bannerlar',
            },
        ),
    ]
