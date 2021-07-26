# Generated by Django 3.2.5 on 2021-07-26 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_auto_20210726_1325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['-time_update'], 'verbose_name': 'Известные женщины', 'verbose_name_plural': 'Женщины'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='women',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='women.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='women',
            name='content',
            field=models.TextField(blank=True, verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='women',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='women',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='women',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='women',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]
