from django.db import models

from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='название плагина',
                            help_text='Введите наименование плагина')

    description = models.TextField(max_length=150, verbose_name='описание плагина',
                                   help_text='Введите описание плагина')

    image = models.ImageField(upload_to='photo/product', blank=True, null=True,
                              verbose_name='Фото', help_text='Загрузите фото')

    category_id = models.ForeignKey(to='Category', on_delete=models.SET_NULL,
                                    verbose_name='категория', blank=True, null=True)

    price = models.IntegerField(verbose_name='стоимость плагина')
    created_at = models.DateField(blank=True, null=True, verbose_name='дата создания')
    updated_at = models.DateField(blank=True, null=True, verbose_name='дата последнего изменения')

    user = models.ForeignKey(User, blank=True, null=True, verbose_name='Пользователь', on_delete=models.SET_NULL)

    is_publication = models.BooleanField(default=False, verbose_name='Признак публикации')

    class Meta:
        verbose_name = 'плагин'
        verbose_name_plural = 'плагины'
        permissions = [
            ('can_cancel_publication', 'Может отменять публикацию продукта'),
            ('can_change_description_product', 'может менять описание любого продукта'),
            ('can_change_category_product', 'может менять категорию любого продукта'),
        ]

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='название катигории',
                            help_text='Введите наименование категории')

    description = models.TextField(max_length=150, verbose_name='описание катигории',
                                   help_text='Введите описание катигории')

    class Meta:
        verbose_name = 'катигория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'катигории'  # Настройка для наименования набора объектов

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'


class Version(models.Model):
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE,
                                verbose_name='Продукт', blank=True, null=True)
    number_version = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=150, verbose_name='Название версии')
    is_version = models.BooleanField(default=True, verbose_name='Признак версии')


    def __str__(self):
        return f"{self.version_name}"

    class Meta:
        verbose_name = "версия продукта"
        verbose_name_plural = "версии продуктов"



