
from django import template

register = template.Library()

@register.filter(is_safe=True)
def textfield_with_floating_label(value):
    """Removes all values of arg from the given string"""
    mdl_textfield = '<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">{}</div>'.format(value)
    mdl_textfield = mdl_textfield.replace('for="id_message"', 'for="mdl-textfield__label"')
    mdl_textfield = mdl_textfield.replace('<p>', '').replace('</p>', '')
    return mdl_textfield
