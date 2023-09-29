import json
from django.http import HttpResponse

class AssertAPIResponseMixin:
    def assertResponseHeaders(self, response: HttpResponse, headers):
        for header in headers.keys():
            value = headers.get(header)
            self.assertEquals(response.headers.get(header), value)
    
    def assertResponseJson(self, response: HttpResponse, data: dict):
        return self.assertEquals(json.dumps(data), json.dumps(response.json()))
