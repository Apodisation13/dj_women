from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from women.models import *


MENU = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def home(request):
    template_name = 'women/home.html'
    women = Women.objects.all()
    context = {'women': women}
    return render(request, template_name, context)


def categories(request, category_id):
    # print(request.GET)
    # if int(category_id) > 10:
    #     raise Http404()

    template_name = 'women/categories.html'
    context = {
        'category_id': category_id,
        'menu': MENU
    }
    return render(request, template_name, context)


def page_not_found(request, exception):
    msg = '<h1><font color="red">СТРАНИЦА НЕ НАЙДЕНА</font></h1>'
    return HttpResponseNotFound(msg)
