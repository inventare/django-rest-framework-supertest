from typing import List, Union, Optional
from django.http import HttpResponse
from rest_framework import status

class AssertAPIValidationMixin:
    def assertHasValidationField(self, 
            response: HttpResponse, 
            fieldPath: Union[List[Union[str, int]], str], 
            messages: Optional[Union[List[str], str]]=None):
        if type(fieldPath) == str:
            fieldPath = [fieldPath]

        if type(messages) == str:
            messages = [messages]
            
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = response.json()
        for path in fieldPath:
            data = data[path]

        if not messages:
            self.assertTrue(len(data) > 0)
        else:
            self.assertEquals(data, messages)
