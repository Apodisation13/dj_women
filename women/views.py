from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from women.models import *


MENU = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти    ', 'url_name': 'login'}
        ]


def about(request):
    template_name = 'women/about.html'
    return render(request, template_name)


def home(request):
    template_name = 'women/index.html'

    women = Women.objects.all()
    categories = Category.objects.all()

    context = {
        'posts': women,
        'menu': MENU,
        'title': 'Главная страница',
        'categories': categories,
        'category_selected': 0
    }

    return render(request, template_name, context)


def add_page(request):
    return HttpResponse('Добавить страницу')


def contact(request):
    return HttpResponse('Контакты')


def login(request):
    return HttpResponse('Войти')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id {post_id}')


def show_category(request, category_id):
    template_name = 'women/index.html'

    women = Women.objects.filter(category_id=category_id)
    categories = Category.objects.all()

    if not women:
        raise Http404()

    context = {
        'posts': women,
        'menu': MENU,
        'title': 'Отображение по рубрикам',
        'categories': categories,
        'category_selected': category_id
    }

    return render(request, template_name, context)


def page_not_found(request, exception):
    msg = '<h1><font color="red">СТРАНИЦА НЕ НАЙДЕНА</font></h1>'
    return HttpResponseNotFound(msg)


# def categories(request, category_id):
#     # print(request.GET)
#     # if int(category_id) > 10:
#     #     raise Http404()
#
#     template_name = 'women/categories.html'
#     context = {
#         'category_id': category_id,
#         'menu': MENU
#     }
#     return render(request, template_name, context)
