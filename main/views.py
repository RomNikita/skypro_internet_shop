from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from main.models import Product, Blog


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}({phone}): {message}')
    return render(request, 'main/contacts.html')


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'preview', 'price', 'date', 'modified_at',)
    success_url = reverse_lazy('home')


class ProductListView(ListView):
    model = Product
    template_name = 'main/home.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_id.html'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'preview', 'price', 'date', 'modified_at',)  # Поля для редактирования
    success_url = reverse_lazy('home')
    template_name = 'main/product_edit.html'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('home')


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'preview', 'date', 'sign_of_blog', 'number_of_views',)
    success_url = reverse_lazy('blog_list')


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'main/blog_id.html'


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'preview', 'date', 'sign_of_blog', 'number_of_views',)
    success_url = reverse_lazy('blog_list')
    template_name = 'main/blog_edit.html'


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')

