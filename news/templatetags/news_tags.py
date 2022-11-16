from django import template

from news.models import Category


register = template.Library()

@register.simple_tag(name="get_list_categories")
def get_categories():
    return  Category.objects.order_by('id')


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.order_by('id')
    return {'categories': categories}