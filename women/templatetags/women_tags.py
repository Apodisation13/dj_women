from django import template
from women.models import *


MENU = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти    ', 'url_name': 'login'}
        ]

register = template.Library()


# в скобках можно указать name= имя для тэг-функции
@register.simple_tag()
def get_categories():
    return Category.objects.all()


# целый кусок хтмл страницы!!! да ещё и с аргументом,который должен указываться в шаблоне
@register.inclusion_tag('women/show_categories.html')
def show_categories(category_selected):
    categories = Category.objects.all()
    return {'categories': categories, "category_selected": category_selected}


@register.inclusion_tag('women/show_menu.html')
def show_menu():
    return {'menu': MENU}
