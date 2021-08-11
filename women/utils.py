from women.models import Category


class BaseMixin:
    """общий класс для представлений"""

    def get_user_context(self, **kwargs):
        context = kwargs
        # categories = Category.objects.all()
        # context['categories'] = categories
        if 'category_selected' not in context:
            context['category_selected'] = 0
        return context
