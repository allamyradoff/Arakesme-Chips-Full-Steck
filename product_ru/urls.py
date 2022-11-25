from django.urls import path
from .views import *

urlpatterns = [
    path('', index_ru, name="index_ru"),
    path('about/', about_ru, name="about_ru"),
    path('all_products/', all_products_ru, name="all_products_ru"),
    path('product_detail/<int:id>/', product_detail_ru, name="product_detail_ru"),
    path('category/<int:id>/', category_ru, name="category_ru"),
    path('contact/', contact_ru, name='contact_ru'),

]
