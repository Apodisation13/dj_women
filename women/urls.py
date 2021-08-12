from django.urls import path
from django.views.decorators.cache import cache_page

from women.views import *
from women.views_CBV import *


# FUNC_BASED_VIEW
# urlpatterns = [
#     path('', home, name='home'),
#     path('about/', about, name='about'),
#     path('addpage/', add_page, name='add_page'),
#     path('contact/', contact, name='contact'),
#     path('login/', login, name='login'),
#     path('post/<slug:post_slug>/', show_post, name='post'),
#     path('category/<slug:category_slug>/', show_category, name='category'),
# ]


# CLASS_BASED_VIEW
urlpatterns = [
    path('', cache_page(60)(WomenHome.as_view()), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:category_slug>/', cache_page(60)(WomenCategory.as_view()), name='category'),
]
