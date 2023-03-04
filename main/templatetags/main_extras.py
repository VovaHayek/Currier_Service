from django import template

from main.models import Restaurant

register = template.Library()

@register.inclusion_tag('includes/slider.html')
def last_three_elements():
    slider_restaurants = Restaurant.objects.all()[2:]
    return {'slides': slider_restaurants}