from typing import List, Optional

from django.http import HttpResponse


class AssertPaginationMixin:
    """Implements a Mixin to assert pagination responses in APITestCase."""

    def get_pagination_query_params(
        self,
        offset: Optional[int],
        page_size: Optional[int],
    ) -> dict:
        """
        Create pagination query parameters for making client requests.

        Args:
            offset: the skip offset.
            page_size: the page items count.
        """
        data = {}

        if offset is not None:
            data['offset'] = offset
        if page_size is not None:
            data['limit'] = page_size

        return data

    def assert_pagination_data(
        self,
        data: dict,
        page_items: List[object],
        serializer_class: object,
        total_itens: int,
    ) -> None:
        """
        Assert if the paginaiton data is equals the expected itens.

        Args:
            data: the data extracted from response.
            page_items: the list of the items of the page.
            serializer_class: the class of the serializer to validate.
            total_itens: the total itens count.
        """
        if not hasattr(self, 'assert_serializer_data'):
            msg = (
                "To use assert_pagination_data method, assert_serializer_data should "
                "be disponible on test case. To turn it disponible, add "
                "AssertSerializersMixin to the inherit classes of your TestCase"
            )
            raise AttributeError(msg)

        results = data.get('results')
        self.assertEqual(len(results), len(page_items))
        serializer = serializer_class(instance=page_items, many=True)
        self.assert_serializer_data(results, serializer)
        self.assertEqual(data.get('count'), total_itens)

    def assert_pagination_response(
        self,
        response: HttpResponse,
        page_items: List[object],
        serializer_class: object,
        total_itens: int,
    ) -> None:
        """
        Assert if the paginaiton response is equals the expected itens.

        Args:
            response: The `HttpResponse` to check response json body.
            page_items: the list of the items of the page.
            serializer_class: the class of the serializer to validate.
            total_itens: the total itens count.
        """
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assert_pagination_data(data, page_items, serializer_class, total_itens)
