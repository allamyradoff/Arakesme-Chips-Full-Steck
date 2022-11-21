from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('all_products/', all_products, name="all_products"),
    path('category/<int:id>/', category, name="category"),
]
