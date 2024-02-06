from typing import List, Union

from django.http import HttpResponse
from rest_framework.serializers import Serializer


class AssertSerializersMixin:
    """Implements a Mixin to assert serializer data in APITestCase."""

    def assert_serializer_data(
        self,
        data: Union[dict, List],
        serializer: Serializer,
    ) -> None:
        """
        Assert if the data is equals the serializer output data.

        Args:
            data: the data extracted from response or from pagination.
            serializer: the serializer to get data and extract.
        """
        output_data = serializer.data
        if isinstance(data, dict):
            return self.assertDictEqual(output_data, data)
        if isinstance(data, list):
            return self.assertListEqual(output_data, data)

        return self.fail("Only dict or list is acceptable.")

    def assert_serializer_response_data(
        self,
        response: HttpResponse,
        serializer: Serializer,
    ) -> None:
        """
        Assert if the response json body is equals the serializer output data.

        Args:
            response: The `HttpResponse` to check response json body.
            serializer: the serializer to get data and extract.
        """
        self.assert_serializer_data(response.json(), serializer)
