from django.contrib import admin

from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_update', 'photo', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published','time_update')
    prepopulated_fields = {'slug': ('title',)}  # для ввода слага автоматически по имени


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Category._meta.fields]  # показать все поля
    list_display_links = ('name',)
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}  # для ввода слага автоматически по имени


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
