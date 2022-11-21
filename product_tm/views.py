from django.shortcuts import render
from django.http import HttpResponse
from .models import *

banner = Banner.objects.all()


def index(request):
    benefit = Benefits.objects.all()[0:3]
    main_page_banners = MainPageBanners.objects.all()[0:1]
    top_three_product = TopThree.objects.all()[0:4]
    last_product = Product.objects.all().order_by('-id')
    last_product = last_product[0:4]
    news = News.objects.all()[0:3]

    context = {
        'banner': banner,
        'benefit': benefit,
        'top_three_product': top_three_product,
        'main_page_banners': main_page_banners,
        'last_product': last_product,
        'news': news,
    }
    return render(request, 'home.html', context)


def about(request):
    about = AboutBanner.objects.all()[0:1]
    benefit = Benefits.objects.all()[0:4]
    about_page_banners = AboutPageBanners.objects.all()[0:1]
    about_us = AboutUs.objects.all()[0:1]

    context = {
        'about': about,
        'benefit': benefit,
        'about_page_banners': about_page_banners,
        'about_us': about_us,
    }
    return render(request, 'about.html', context)


def all_products(request):
    product = Product.objects.all()
    category = Category.objects.all()

    context = {
        'product': product,
        'category': category,
    }
    return render(request, 'all_products.html', context)


def category(request, id):
    product = Product.objects.filter(category__id=id)
    category = Category.objects.all()

    context = {
        'product': product,
        'category': category,
    }
    return render(request, 'product.html', context)
