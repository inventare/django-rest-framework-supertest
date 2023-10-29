import json

from django.http import HttpResponse


class AssertAPIResponseMixin:
    def assertResponseHeaders(self, response: HttpResponse, headers):
        for header in headers.keys():
            value = headers.get(header)
            self.assertEqual(response.headers.get(header), value)

    def assertResponseJson(self, response: HttpResponse, data: dict):
        return self.assertEqual(json.dumps(data), json.dumps(response.json()))
