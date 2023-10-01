from django.urls import path

from main.views import contacts, ProductCreateView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView, BlogListView, BlogCreateView, BlogUpdateView, BlogDetailView, BlogDeleteView, \
    product_version_list, VersionCreateView


app_name = 'main'


urlpatterns = [
    path('', product_version_list, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
    path('product/<int:pk>/version/', VersionCreateView.as_view(), name='version_create'),
]
