
class FakerModelMixin:
    @staticmethod
    def create_faker(self):
        print(self.__class.faker_fields)
