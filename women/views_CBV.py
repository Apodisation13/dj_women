from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView

from .forms import *
from .models import *
from .utils import *


class WomenHome(BaseMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    queryset = Women.objects.filter(is_published=True)

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
