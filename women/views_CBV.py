from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView

from .forms import *
from .models import *
from .utils import *


class WomenHome(BaseMixin, ListView):

    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    queryset = Women.objects.filter(is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        # возващаем объединение словарей... сложная штука
        # return dict(list(context.items()) + list(c_def.items()))
        return context | c_def  # это аналогично предыдущей записи!

    # это аналогично просто параметру queryset =
    # def get_queryset(self):
    #     return Women.objects.filter(is_published=True)


class WomenCategory(ListView):

    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False  # если категории нету - будет 404, а не Exception list_out_of_index

    def get_queryset(self):
        w = Women.objects.filter(
            category__slug=self.kwargs['category_slug'], is_published=True).\
            select_related('category')
        return w

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # для отображения - Категории - название категории
        context['title'] = 'Категория - ' + str(context['posts'][0].category)
        # для того чтобы достать по сути pk категории
        context['category_selected'] = context['posts'][0].category_id
        return context


class ShowPost(DeleteView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'  # или pk_url_kwarg для pk
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['category_selected'] = context['post'].category_id
        return context


class AddPage(BaseMixin, LoginRequiredMixin, CreateView):
    """класс добавляет из коробки возможность создавать только залогененному"""
    form_class = AddPostForm
    template_name = 'women/addpage.html'

    # а вот тут проблема - get_absolute_url иначе нужно бы вот такое:
    # success_url = reverse_lazy('home')

    # тут на самом деле нужно либо одно, либо другое
    # login_url = reverse_lazy('admin:index')  # куда пойти по попытке зайти
    login_url = '/admin/'
    # raise_exception = True  # кинуть 403 запрещено вместо 404

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить статью')
        return context | c_def


class RegisterUser(BaseMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return context | c_def

    def form_valid(self, form):
        """если авторизация прошла успешно, по сути ещё и залогинить юзера, +редирект домой"""
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(BaseMixin, LoginView):

    form_class = LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Аутентификация')
        return context | c_def

    def get_success_url(self):
        """вот здесь почему-то нужно так, через метод именно, а не success_url как выше"""
        # или так, или в settings написать LOGIN_REDIRECT_URL = '/'
        return reverse_lazy('home')
        # для возрата на то место, где был до этого!
        # url = self.get_redirect_url()
        # if url:
        #     return url
        # else:
        #     return reverse_lazy('home')
