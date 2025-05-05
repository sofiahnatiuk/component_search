from django import template
from urllib.parse import urlencode

register = template.Library()


@register.simple_tag(takes_context=True)
def querystring_without_page(context):
    request = context['request']
    query = request.GET.copy()
    query.pop('page', None)
    return urlencode(query)