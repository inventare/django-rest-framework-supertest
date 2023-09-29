from typing import List
import json
from django.http import HttpResponse
from rest_framework_supertest.utils.exceptions import APIExceptionsUtils


class AssertAPIExceptionMixin:
    def assertAPIException(self, response: HttpResponse, exception):
        if not hasattr(self, 'assertResponseJson'):
            raise AttributeError(
                "To use assertAPIException method, assertResponseJson must be present in the TestCase. "
                "Extends AssertAPIResponseMixin on your TestCase"
            )
        if not hasattr(self, 'assertResponseHeaders'):
            raise AttributeError(
                "To use assertAPIException method, assertResponseHeaders must be present in the TestCase. "
                "Extends AssertAPIResponseMixin on your TestCase"
            )

        handler = APIExceptionsUtils(response, exception)
        data, status, headers = handler.exception_handler()

        self.assertEquals(response.status_code, status)
        self.assertResponseJson(response, data)
        self.assertResponseHeaders(response, headers)

    def assertOneOfAPIExceptions(self, response: HttpResponse, exceptions: List[any]):
        found_one = False
        for exception in exceptions:
            handler = APIExceptionsUtils(response, exception)
            data, status, headers = handler.exception_handler()

            if response.status_code != status:
                continue
            if json.dumps(data) != json.dumps(response.json()):
                continue

            found_one = True
            for header in headers.keys():
                value = headers.get(header)

                if response.headers.get(header) != value:
                    found_one = False

            if found_one:
                break

        if not found_one:
            self.fail('None of the APIException\'s is raised to the response.')
