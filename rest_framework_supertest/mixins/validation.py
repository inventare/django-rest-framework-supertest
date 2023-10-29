from typing import List, Optional, Union

from django.http import HttpResponse
from rest_framework import status
from rest_framework.exceptions import ValidationError


class AssertAPIValidationMixin:
    """Implements a Mixin to assert Validation errors in APITestCase."""

    def assert_has_validation_field(
        self,
        response: HttpResponse,
        field_path: Union[List[Union[str, int]], str],
        messages: Optional[Union[List[str], str]] = None,
    ) -> None:
        """
        Assert if the response has an validation error in some field.

        Args:
            response: The `HttpResponse` to check if has an validation error.
            field_path: The field path inside the response json data.
            messages: A message string or a list of messages. This is optional
              and if was not defined, is checked only if has one validation error
              for the field, without validating the validation error messages.
        """
        if isinstance(field_path, str):
            field_path = [field_path]

        if isinstance(messages, str):
            messages = [messages]

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = response.json()
        for path in field_path:
            data = data[path]

        if not messages:
            self.assertTrue(len(data) > 0)
        else:
            self.assertEqual(data, messages)

    def assert_validation_response(
        self,
        response: HttpResponse,
        data: Union[dict, list],
    ) -> None:
        """
        Assert if the response is a an validation error response.

        Args:
            response: the `HttpResponse` to check if is an validation
              error response.
            data: the validation error data.
        """
        if not hasattr(self, 'assert_api_exception'):
            msg = (
                "To use assertValidationResponse method, assert_api_exception should "
                "be disponible on test case. To turn it disponible, add "
                "AssertAPIExceptionMixin to the inherit classes of your TestCase"
            )
            raise AttributeError(msg)

        exception = ValidationError(data)
        self.assert_api_exception(response, exception)
