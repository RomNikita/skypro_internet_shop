# Generated by Django 4.2.4 on 2023-09-22 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_product_name_version'),
    ]

    operations = [
        migrations.RenameField(
            model_name='version',
            old_name='to_active',
            new_name='is_active',
        ),
    ]
