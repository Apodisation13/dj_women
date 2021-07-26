from django.apps import AppConfig


class WomenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'women'

    # влияет на админку - заголовок приложения на синем фоне, включено только если мы зарегили приложение хитро
    verbose_name = 'Женщины мира'
