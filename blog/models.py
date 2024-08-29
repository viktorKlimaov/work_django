from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='название заголовка')

    slug = models.CharField( max_length=100, verbose_name='slug', blank=True, null=True,)

    content = models.TextField(max_length=200, verbose_name='содержимое',)

    image = models.ImageField(upload_to='photo/blog', blank=True, null=True,
                              verbose_name='Изображение')

    created_at = models.DateField(blank=True, null=True, verbose_name='дата создания')

    is_publication = models.BooleanField(default=True, verbose_name='Признак публикации')

    count_views = models.IntegerField(default=0, verbose_name='Количество просмотров')


    class Meta:
        verbose_name = 'Статья'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Статьи'  # Настройка для наименования набора объектов

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'
