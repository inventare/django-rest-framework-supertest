from typing import List, Union
from django.http import HttpResponse
from rest_framework import status

class AssertAPIValidationMixin:
    def assertHasValidationField(self, 
                              response: HttpResponse, 
                              fieldPath: Union[List[Union[str, int]], str], 
                              messages: Union[List[str], str]):
        if type(fieldPath) == str:
            fieldPath = [fieldPath]

        if type(messages) == str:
            messages = [messages]
            
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = response.json()
        for path in data:
            data = data[path]

        self.assertEquals(data, messages)

