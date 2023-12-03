import json

from django.http import HttpResponse


class AssertAPIResponseMixin:
    """Implements a Mixin to assert API responses in APITestCase."""

    def assert_response_headers(self, response: HttpResponse, headers: dict) -> None:
        """
        Assert if the response headers has some headers.

        The `HttpResponse` may contain another headers that no described in
        the `headers` argument. Only the `headers` is checked.

        Args:
            response: The `HttpResponse` to check response headers.
            headers: The headers to check if is present inside the response headers.
        """
        for header in headers:
            value = headers.get(header)
            self.assertEqual(response.headers.get(header), value)

    def assert_response_json(self, response: HttpResponse, data: dict) -> None:
        """
        Assert if the response json data is equals to other data.

        Args:
            response: The `HttpResponse` to check response json body.
            data: The data to assert if is equals.
        """
        return self.assertEqual(json.dumps(data), json.dumps(response.json()))
