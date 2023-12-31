# Generated by Django 4.2.4 on 2023-09-22 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_blog_sign_of_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='название продукта'),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_version', models.IntegerField(default=0, verbose_name='номер версии')),
                ('name_of_version', models.CharField(max_length=100, verbose_name='название версии')),
                ('to_active', models.BooleanField(default=True, verbose_name='признак версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
