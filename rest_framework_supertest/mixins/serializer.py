from django.http import HttpResponse
from rest_framework.serializers import Serializer


class AssertSerializersMixin:
    """Implements a Mixin to assert serializer data in APITestCase."""

    def assert_serializer_data(self, data: dict, serializer: Serializer) -> None:
        """
        Assert if the data is equals the serializer output data.

        Args:
            data: the data extracted from response or from pagination.
            serializer: the serializer to get data and extract.
        """
        output_data = serializer.data
        self.assertDictEqual(output_data, data)

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
