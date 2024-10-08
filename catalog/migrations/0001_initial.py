# Generated by Django 5.1 on 2024-08-11 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование категории', max_length=150, verbose_name='название катигории')),
                ('description', models.TextField(help_text='Введите описание катигории', max_length=150, verbose_name='описание катигории')),
            ],
            options={
                'verbose_name': 'катигория',
                'verbose_name_plural': 'катигории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование плагина', max_length=150, verbose_name='название плагина')),
                ('description', models.TextField(help_text='Введите описание плагина', max_length=150, verbose_name='описание плагина')),
                ('image', models.ImageField(blank=True, help_text='Загрузите фото', null=True, upload_to='photo/product', verbose_name='Фото')),
                ('price', models.IntegerField(verbose_name='стоимость плагина')),
                ('created_at', models.DateField(blank=True, null=True, verbose_name='дата создания')),
                ('updated_at', models.DateField(blank=True, null=True, verbose_name='дата последнего изменения')),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'плагин',
                'verbose_name_plural': 'плагины',
            },
        ),
    ]
