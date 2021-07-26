from django import template
from women.models import *


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
