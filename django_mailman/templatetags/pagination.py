from django import template
from django.utils.html import conditional_escape


register = template.Library()


@register.simple_tag(takes_context=True)
def add_to_query_string(context, *args, **kwargs):
    """Adds or replaces parameters in the query string"""
    qs = context["request"].GET.copy()
    # create a dict from every args couple
    new_qs_elements = dict(zip(args[::2], args[1::2]))
    new_qs_elements.update(kwargs)
    # don't use the .update() method, it appends instead of overwriting.
    for key, value in new_qs_elements.iteritems():
        qs[key] = value
    return conditional_escape(qs.urlencode())

