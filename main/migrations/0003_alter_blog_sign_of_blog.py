# Generated by Django 4.2.4 on 2023-09-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blog_alter_product_date_alter_product_modified_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='sign_of_blog',
            field=models.BooleanField(default=True),
        ),
    ]