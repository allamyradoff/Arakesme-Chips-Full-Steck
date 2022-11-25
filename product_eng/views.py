from django.shortcuts import render
from django.http import HttpResponse
from .models import *

banner = Banner.objects.all()


def index_eng(request):
    benefit = Benefits.objects.all()[0:3]
    main_page_banners = MainPageBanners.objects.all()[0:1]
    top_three_product = TopThree.objects.all()[0:4]
    last_product = Product.objects.all().order_by('-id')
    last_product = last_product[0:4]
    news = News.objects.all()[0:3]
    about_us = AboutUs.objects.all()[0:1]
    location = Locations.objects.all()[0:1]
    flag = Flag.objects.all()

    context = {
        'banner': banner,
        'benefit': benefit,
        'top_three_product': top_three_product,
        'main_page_banners': main_page_banners,
        'last_product': last_product,
        'news': news,
        'about_us': about_us,
        'location':location,
        'flag':flag

    }
    return render(request, 'eng/home_eng.html', context)


def about_eng(request):
    about = AboutBanner.objects.all()[0:1]
    benefit = Benefits.objects.all()[0:4]
    about_page_banners = AboutPageBanners.objects.all()[0:1]
    about_us = AboutUs.objects.all()[0:1]
    flag = Flag.objects.all()


    context = {
        'about': about,
        'benefit': benefit,
        'about_page_banners': about_page_banners,
        'about_us': about_us,
        'flag':flag

    }
    return render(request, 'eng/about_eng.html', context)


def all_products_eng(request):
    product = Product.objects.all()
    category = Category.objects.all()
    about_us = AboutUs.objects.all()[0:1]
    product_banner = ProductsBanner.objects.all()[0:1]
    flag = Flag.objects.all()



    context = {
        'product': product,
        'category': category,
        'about_us': about_us,
        'product_banner':product_banner,
        'flag':flag


    }
    return render(request, 'eng/all_products_eng.html', context)


def category_eng(request, id):
    product = Product.objects.filter(category__id=id)
    category = Category.objects.all()
    about_us = AboutUs.objects.all()[0:1]
    product_banner = ProductsBanner.objects.all()[0:1]
    flag = Flag.objects.all()



    context = {
        'product': product,
        'category': category,
        'about_us': about_us,
        'product_banner':product_banner,
        'flag':flag



    }
    return render(request, 'eng/product_eng.html', context)


def contact_eng(request):
    about_us = AboutUs.objects.all()[0:1]
    location = Locations.objects.all()[0:1]
    flag = Flag.objects.all()


    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        contact = ContactUs.objects.create(
            name=name,
            email=email,
            phone=phone_number,
            message=message,
        )
        print(contact)

        contact.save()
    context = {
        'about_us': about_us,
        'location':location,
        'flag':flag


    }
    return render(request, 'eng/contacts_eng.html', context)


def product_detail_eng(request, id):
    about_us = AboutUs.objects.all()[0:1]
    flag = Flag.objects.all()

    product = Product.objects.get(id=id)

    context = {
        'product':product,
        'about_us': about_us,
        'flag':flag

    }

    return render(request, 'eng/product_detail_eng.html', context)
