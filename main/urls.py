from django.conf.urls.static import static
from django.urls import path

from config import settings
from main.views import home, contacts, products

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('products/', products),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)