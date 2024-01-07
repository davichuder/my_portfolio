import re
from .models import Pages

def model_to_dict(model):
    new_dict = model.__dict__
    new_dict.pop("id")
    new_dict.pop("_state")
    return new_dict

def all_row_model_to_dict(model_class, *order_by):
    if order_by:
        return [model_to_dict(model) for model in model_class.objects.all().order_by(*order_by)]    
    return [model_to_dict(model) for model in model_class.objects.all()]

def obtain_url_buttons_from_template(model, template_name):
    url = re.search(r'[^/]+(?=\.html$)', template_name).group()
    buttons = model.objects.filter(url=url).values().first()
    buttons.pop("id")
    return buttons

def get_pages_list(start_url="index"):
    url_list = []
    name_list = []
    next_item = Pages.objects.filter(url=start_url).values().first()
    while next_item['next_url']:
        url_list.append(next_item['next_url'])
        next_item = Pages.objects.filter(url=url_list[-1]).values().first()
        name_list.append(next_item['name'])
    page_list = [{'url':item[0], 'name':item[1]} for item in zip(url_list, name_list)]
    return page_list

dict_month_to_number = {
    "Enero": 1,
    "Febrero": 2,
    "Marzo": 3,
    "Abril": 4,
    "Mayo": 5,
    "Junio": 6,
    "Julio": 7,
    "Agosto": 8,
    "Septiembre": 9,
    "Octubre": 10,
    "Noviembre": 11,
    "Diciembre": 12
}

dict_number_to_month = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}