from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect

from women.forms import AddPostForm
from women.models import *


def about(request):
    template_name = 'women/about.html'
    # для функции пагинатор выглядел бы так:
    # чтобы перейти на вторую страницу надо напечатать
    contact_list = Women.objects.all().select_related('category')
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'title': 'О сайте'}
    return render(request, template_name, context)


def home(request):
    template_name = 'women/index.html'

    women = Women.objects.all().select_related('category')
    # ВОТ ЭТО ДОБАВЛЕНИЕ SELECT_RELATED ПОЗВОЛИЛО ВМЕСТО КУЧИ ЗАПРОСОВ СДЕЛАТЬ ВСЕГО 2

    context = {
        'posts': women,
        'title': 'Главная страница',
        'category_selected': 0
    }

    return render(request, template_name, context)


@login_required  # для функции нужен декоратор
def add_page(request):
    template_name = 'women/addpage.html'

    # проверка - если форма уже отправлена с ошибкой, чтобы данные остались
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    context = {'title': 'Добавление статьи', 'form': form}
    return render(request, template_name, context)


def contact(request):
    return HttpResponse('Контакты')


def login(request):
    return HttpResponse('Войти')


def show_post(request, post_slug):

    template_name = 'women/post.html'

    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'category_selected': post.category_id
    }

    return render(request, template_name, context)


def show_category(request, category_slug):
    template_name = 'women/index.html'

    # category_id = Category.objects.filter(slug=category_slug)

    women = Women.objects.filter(category__slug=category_slug).select_related('category')

    if not women:
        raise Http404()

    context = {
        'posts': women,
        'title': 'Отображение по рубрикам',
        'category_selected': category_slug
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

def logout_user(request):
    logout(request)
    return redirect('login')
