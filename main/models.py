from django.db import models
from django.utils import timezone

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='название категории')
    description = models.TextField(verbose_name='описание категории')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название продукта', unique=True)
    description = models.TextField(verbose_name='описание продукта')
    preview = models.ImageField(upload_to='product',verbose_name='превью', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    date = models.DateField(default=timezone.now, verbose_name='дата создания', null=True)
    modified_at = models.DateField(verbose_name='дата последнего изменения', null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',) # порядок с какого поля начнется


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='слаг', null=True, blank=True)
    content = models.TextField(verbose_name='содержание')
    preview = models.ImageField(upload_to='blog', verbose_name='превью блога', null=True, blank=True)
    date = models.DateField(default=timezone.now, verbose_name='дата создания', null=True)
    sign_of_blog = models.BooleanField(default=True, verbose_name='признак публикации')
    number_of_views = models.IntegerField(default=0, verbose_name='количество просмотров')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('title',)


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт')
    number_of_version = models.IntegerField(default=0, verbose_name='номер версии')
    name_of_version = models.CharField(max_length=100, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='признак версии')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name_of_version} ({self.number_of_version})'


    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'