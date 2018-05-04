from django.forms.models import model_to_dict

from .models import Category


def json_iter_first(json_data, parent=None):
    if isinstance(json_data, list):
        for item in json_data:
            json_iter_sec_dict(item, parent)
    else:
        json_iter_sec_dict(json_data)


def json_iter_sec_dict(json_data, parent=None):
    for key, value in json_data.items():
        if key == 'name' and isinstance(value, str):
            parent = Category.objects.create(name=value, parent=parent)
        if isinstance(value, list) and len(value) > 0:
            json_iter_first(value, parent)


def serializer(items: list) -> list:
    """
    Functions of serializing instances of the Category model
    :param items: list of instances of the Category model
    :return: list of dictionaries composed of instances of the Category model
    """
    list_return = []
    for item in items:
        list_return.append({key: value for key, value in model_to_dict(item).items() if key != 'parent'})

    return list_return
