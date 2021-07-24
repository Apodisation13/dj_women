from django.http import HttpResponse, HttpResponseNotFound, Http404


def home(request):
    msg = '<h1><font color="green">Это главная страница...</font></h1>'
    return HttpResponse(msg)


def categories(request, category_id):
    print(request.GET)
    if int(category_id) > 10:
        raise Http404()

    msg = f'<h2><font color="blue">Страница категорий</font><br>{category_id}</h2>'
    return HttpResponse(msg)


def page_not_found(request, exception):
    msg = '<h1><font color="red">СТРАНИЦА НЕ НАЙДЕНА</font></h1>'
    return HttpResponseNotFound(msg)
