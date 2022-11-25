from django.urls import path
from .views import *

urlpatterns = [
    path('', index_eng, name="index_eng"),
    path('about/', about_eng, name="about_eng"),
    path('all_products/', all_products_eng, name="all_products_eng"),
    path('product_detail/<int:id>/', product_detail_eng, name="product_detail_eng"),
    path('category/<int:id>/', category_eng, name="category_eng"),
    path('contact/', contact_eng, name='contact_eng'),

]
