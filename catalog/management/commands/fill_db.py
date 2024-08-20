import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        # Здесь мы получаем данные из фикстурв с категориями
        with open('data/catalog/category.json', 'r', encoding='utf-8') as file:
            categories = json.load(file)
        return categories

    @staticmethod
    def json_read_products():
        # Здесь мы получаем данные из фикстурв с продуктами
        with open('data/catalog/product.json', 'r', encoding='utf-8') as file:
            products = json.load(file)
        return products

    def handle(self, *args, **options):
        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    name=category['fields']['name'],
                    description=category['fields']['description'],
                    pk=category['pk'],
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    pk=product["pk"],
                    name=product['fields']['name'],
                    description=product['fields']['description'],
                    image=product['fields']['image'],
                    category_id=Category.objects.get(pk=category['pk']),
                    price=product['fields']['price'],
                    created_at=product['fields']['created_at'],
                    updated_at=product['fields']['updated_at'],

                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
