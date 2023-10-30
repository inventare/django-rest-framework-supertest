import json
from typing import List

from django.http import HttpResponse
from rest_framework.exceptions import APIException

from rest_framework_supertest.utils.exceptions import APIExceptionsUtils


class AssertAPIExceptionMixin:
    """Implements a Mixin to assert API exceptions in APITestCase."""

    def assert_api_exception(
        self,
        response: HttpResponse,
        exception: APIException,
    ) -> None:
        """
        Assert if the response is generated from an APIException.

        Args:
            response: The `HttpResponse` to check if is generated from APIException.
            exception: The `APIException` to verify.
        """
        if not hasattr(self, 'assert_response_json'):
            msg = (
                "To use assertAPIException method, assert_response_json must be "
                "present in the TestCase. Extends AssertAPIResponseMixin on your "
                "TestCase"
            )
            raise AttributeError(msg)
        if not hasattr(self, 'assert_response_headers'):
            msg = (
                "To use assertAPIException method, assert_response_headers must be "
                "present in the TestCase. Extends AssertAPIResponseMixin on your"
                " TestCase"
            )
            raise AttributeError(msg)

        handler = APIExceptionsUtils(response, exception)
        data, status, headers = handler.exception_handler()

        self.assertEqual(response.status_code, status)
        self.assert_response_json(response, data)
        self.assert_response_headers(response, headers)

    def assert_one_of_api_exceptions(
        self,
        response: HttpResponse,
        exceptions: List[APIException],
    ) -> None:
        """
        Assert if the response is generated from one of the APIException's.

        Args:
            response: The `HttpResponse` to check if is generated from one of
              the APIException's from the `exceptions` argument.
            exceptions: An list of `APIException` to verify if the response
              is generated from one of it.
        """
        found_one = False
        for exception in exceptions:
            handler = APIExceptionsUtils(response, exception)
            data, status, headers = handler.exception_handler()

            if response.status_code != status:
                continue
            if json.dumps(data) != json.dumps(response.json()):
                continue

            found_one = True
            for header in headers:
                value = headers.get(header)

                if response.headers.get(header) != value:
                    found_one = False

            if found_one:
                break

        if not found_one:
            self.fail('None of the APIException\'s is raised to the response.')
