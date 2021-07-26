from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    photo = models.ImageField(upload_to='photos/%Y/%m/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    # ПРОТЕКТ - запретить уделение категорий на которые есть ссылки, будет ошибка
    # налл=тру - чтобы смочь добавить вообще такую запись иначе ошибка пустого поля

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """функция для отобржажения кнопку на запись в админке и доставания pk по ключу для шаблонов"""
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        """для отображения в админке"""
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Женщины'
        ordering = ['-time_update']  # эта сортировка влияет везде


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """функция для отобржажения кнопку на запись в админке и доставания pk по ключу для шаблонов"""
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        """для отображения в админке"""
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']  # эта сортировка влияет везде
