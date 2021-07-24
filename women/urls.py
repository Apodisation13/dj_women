from django.urls import path

from women.views import *

urlpatterns = [
    path('', home, name='home'),
    path('categories/<int:category_id>/', categories, name='categories')
]
