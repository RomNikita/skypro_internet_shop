from django.conf.urls.static import static
from django.urls import path

from config import settings
from main.views import contacts, products, home, product_id

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('products/', products),
    path('products/<int:pk>/', product_id, name='product')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)