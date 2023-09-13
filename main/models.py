from django.db import models


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
    name = models.CharField(max_length=100, verbose_name='название продукта')
    description = models.TextField(verbose_name='описание продукта')
    preview = models.ImageField(verbose_name='превью', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    date = models.DateField(verbose_name='дата создания')
    modified_at = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)
