from django.views.generic import ListView, DeleteView, CreateView

from women.forms import AddPostForm
from women.models import *


class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['category_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


class WomenCategory(ListView):

    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False  # если категории нету - будет 404, а не list_out_of_index

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


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'

    # а вот тут проблема - get_absolute_url иначе нужно бы вот такое:
    # success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить статью'
        return context
