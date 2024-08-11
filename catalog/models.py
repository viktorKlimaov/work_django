from django.db import models


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

    class Meta:
        verbose_name = 'плагин'
        verbose_name_plural = 'плагины'

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
