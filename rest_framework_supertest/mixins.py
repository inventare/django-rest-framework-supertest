import json
from django.http import HttpResponse
from rest_framework_supertest.utils.exceptions import APIExceptionsUtils

class AssertAPIExceptionMixin:
    def assertAPIException(self, response: HttpResponse, exception):
        handler = APIExceptionsUtils(response, exception)
        data, status, headers = handler.exception_handler()

        self.assertEquals(response.status_code, status)
        self.assertEquals(json.dumps(data), json.dumps(response.json()))
        
        for header in headers.keys():
            value = headers.get(header)
            self.assertEquals(response.headers.get(header), value)

__all__ = [
    'AssertAPIExceptionMixin'
]
