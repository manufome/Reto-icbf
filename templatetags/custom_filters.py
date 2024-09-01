from django import template

register = template.Library()


@register.filter(name='add_class')
def add_class(value, arg):
    existing_classes = value.field.widget.attrs.get('class', '')
    new_classes = f"{existing_classes} {arg}".strip()
    return value.as_widget(attrs={'class': new_classes})


@register.filter(name='get_attr')
def get_attr(obj, attr_name):
    return obj.get(attr_name, '')
