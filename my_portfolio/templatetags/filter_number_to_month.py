from django import template
from ..auxiliar import dict_number_to_month
import datetime

register = template.Library()
today = datetime.date.today()

@register.filter(name='month_name')
def month_name(number):
    return dict_number_to_month.get(number)

@register.filter(name='short_month_name')
def short_month_name(number):
    return dict_number_to_month.get(number)[:3]

@register.filter(name='equal_current_year')
def current_year(year):
    return year == today.year

@register.filter(name='greater_current_year')
def greater_year(year):
    return year > today.year

@register.filter(name='equal_current_month')
def current_month(month):
    return month == today.month

@register.filter(name='greater_current_month')
def greater_month(month):
    return month > today.month