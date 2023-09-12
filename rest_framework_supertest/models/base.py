from typing import Optional
from faker import Faker

class FakerModelMixin:
    @classmethod
    def create_faker(cls, data: Optional[dict] = None, save = True):
        fake = Faker('pt_BR')

        faker_fields = cls.faker_fields
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
            return cls.objects.create(**create_dict)
        return cls(**create_dict)
