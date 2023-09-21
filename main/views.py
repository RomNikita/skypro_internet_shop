from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

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

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sign_of_blog=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
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


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'preview', 'date', 'sign_of_blog', 'number_of_views',)
    #success_url = reverse_lazy('blog_list')
    template_name = 'main/blog_edit.html'

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')

