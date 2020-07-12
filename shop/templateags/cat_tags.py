from django import template
from ..models import Category
from django.db.models import Count



register = template.Library()

@register.simple_tag
def product_category():
    return Category.objects.all()

