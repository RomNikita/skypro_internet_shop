from django.urls import path

from main.views import home, contacts, products

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('products/', products)
]