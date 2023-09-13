from typing import Optional
from faker import Faker

def create_faker(model_class, data: Optional[dict] = None, save = True):
    fake = Faker('pt_BR')

    faker_fields = model_class.faker_fields
    fields = faker_fields.keys()
    create_dict = {}
    for field in fields:
        create_dict[field] = faker_fields[field](fake)

    if not data:
        data = {}
        
    create_dict = {
        **create_dict,
        **data,
    }

    if save:
        return model_class.objects.create(**create_dict)
    return model_class(**create_dict)
