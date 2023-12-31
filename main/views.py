from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from main.forms import ProductForm, VersionForm
from main.models import Product, Blog, Version


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}({phone}): {message}')
    return render(request, 'main/contacts.html')


@method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:home')

    def form_valid(self, form):
        new_product = form.save(commit=False)
        new_product.owner = self.request.user
        new_product.save()
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    template_name = 'main/home.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_id.html'


@method_decorator(login_required, name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'preview', 'price', 'date', 'modified_at',)
    success_url = reverse_lazy('main:home')
    template_name = 'main/product_edit.html'


@method_decorator(login_required, name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main:home')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sign_of_blog=True)
        return queryset


@method_decorator(login_required, name='dispatch')
class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('main:blog_list')

    def form_valid(self, form):
        new_blog = form.save(commit=False)
        new_blog.owner = self.request.user
        new_blog.slug = slugify(new_blog.title)
        new_blog.save()
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'main/blog_id.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


@method_decorator(login_required, name='dispatch')
class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'preview', 'date', 'sign_of_blog', 'number_of_views',)
    # success_url = reverse_lazy('blog_list')
    template_name = 'main/blog_edit.html'

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main:blog_detail', args=[self.kwargs.get('pk')])


@method_decorator(login_required, name='dispatch')
class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('main:blog_list')


def product_version_list(request):
    products = Product.objects.all()
    active_versions = Version.objects.filter(is_active=True)

    return render(request, 'main/home.html', {'products': products, 'active_versions': active_versions})


@method_decorator(login_required, name='dispatch')
class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('main:product_detail')

    def form_valid(self, form):
        new_version = form.save(commit=False)
        new_version.owner = self.request.user
        new_version.save()
        return super().form_valid(form)
