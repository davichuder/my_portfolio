def model_to_dict(model):
    new_dict = model.__dict__
    new_dict.pop("id")
    new_dict.pop("_state")
    return new_dict

def all_row_model_to_dict(model_class, order_by=None):
    if order_by:
        return [model_to_dict(model) for model in model_class.objects.all().order_by(order_by)]    
    return [model_to_dict(model) for model in model_class.objects.all()]