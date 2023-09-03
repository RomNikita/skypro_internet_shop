from django.core.management import BaseCommand

from main.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'id': 1, 'name': 'Яблоки'},
            {'id': 2, 'name': 'Хлеб',},
            {'id': 3, 'name': 'Вода'},
            {'id': 4, 'name': 'Хлопья'}
        ]

        Category.objects.all().delete()

        category_to_add = []

        for item in category_list:
            category_to_add.append(Category(**item))

        Category.objects.bulk_create(category_to_add)

