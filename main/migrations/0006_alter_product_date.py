# Generated by Django 4.2.4 on 2023-09-18 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 9, 18, 18, 7, 40, 973846, tzinfo=datetime.timezone.utc), null=True, verbose_name='дата создания'),
        ),
    ]
