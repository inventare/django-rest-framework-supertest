from typing import List, Union, Optional
from django.http import HttpResponse
from rest_framework import status
from rest_framework.exceptions import ValidationError

class AssertAPIValidationMixin:
    def assertHasValidationField(self, 
            response: HttpResponse, 
            fieldPath: Union[List[Union[str, int]], str], 
            messages: Optional[Union[List[str], str]]=None):
        if isinstance(fieldPath, str):
            fieldPath = [fieldPath]

        if isinstance(messages, str):
            messages = [messages]
            
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = response.json()
        for path in fieldPath:
            data = data[path]

        if not messages:
            self.assertTrue(len(data) > 0)
        else:
            self.assertEquals(data, messages)

    def assertValidationResponse(self, response: HttpResponse, data):
        if not hasattr(self, 'assertAPIException'):
            msg = (
                "To use assertValidationResponse method, assertAPIException should be disponible on test case. "
                "To turn it disponible, add AssertAPIExceptionMixin to the inherit classes of your TestCase"
            )
            raise AttributeError(msg)
        
        exception = ValidationError(data)
        self.assertAPIException(response, exception)
