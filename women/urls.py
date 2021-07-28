from django.urls import path

from women.views import *

urlpatterns = [
    path('', home, name='home'),
    # path('categories/<int:category_id>/', categories, name='categories'),
    path('about/', about, name='about'),
    path('addpage/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:category_id>/', show_category, name='category'),
]
