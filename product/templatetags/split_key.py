from django import template
register = template.Library()


def split_key(value,arg):
    data = value.split("##@@")
    if arg == "left":
        return data[0]
    elif arg == "right":
        return data[1]
    else:
        return ""

register.filter('split_key', split_key)