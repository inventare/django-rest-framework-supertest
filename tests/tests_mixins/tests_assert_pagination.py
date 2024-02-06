from unittest.mock import MagicMock

from django.test import TestCase
from rest_framework import serializers

from rest_framework_supertest.mixins import AssertPaginationMixin
from rest_framework_supertest.test import APITestCase


class AssertPaginationTestCase(TestCase):
    def test_without_serializer_data(self) -> None:
        test_case = AssertPaginationMixin()
        with self.assertRaises(AttributeError):
            test_case.assert_pagination_data({}, [], None, 100)

    def test_pagination_query_params_offset(self) -> None:
        test_case = AssertPaginationMixin()
        expected = {
            'offset': 100,
        }
        current = test_case.get_pagination_query_params(100, None)
        self.assertDictEqual(expected, current)

    def test_pagination_query_params_limit(self) -> None:
        test_case = AssertPaginationMixin()
        expected = {
            'limit': 20,
        }
        current = test_case.get_pagination_query_params(None, 20)
        self.assertDictEqual(expected, current)

    def test_pagination_query_params_none(self) -> None:
        test_case = AssertPaginationMixin()
        expected = {}
        current = test_case.get_pagination_query_params(None, None)
        self.assertDictEqual(expected, current)

    def test_pagination_query_params_full(self) -> None:
        test_case = AssertPaginationMixin()
        expected = {
            'offset': 100,
            'limit': 20,
        }
        current = test_case.get_pagination_query_params(100, 20)
        self.assertDictEqual(expected, current)

    def test_assert_pagination_data(self) -> None:
        class Item1:
            pid = 1
            name = 'Hello'

        class Item2:
            pid = 2
            name = 'Aloah'

        class Serializer(serializers.Serializer):
            pid = serializers.IntegerField()
            name = serializers.CharField()

        items = [Item1(), Item2()]
        expected_data = {
            'results': [
                {
                    'pid': 1,
                    'name': 'Hello',
                },
                {
                    'pid': 2,
                    'name': 'Aloah',
                },
            ],
            'count': 4,
        }
        test_case = APITestCase()
        test_case.assert_pagination_data(expected_data, items, Serializer, 4)

    def test_assert_pagination_response(self) -> None:
        class Item1:
            pid = 1
            name = 'Hello'

        class Item2:
            pid = 2
            name = 'Aloah'

        class Serializer(serializers.Serializer):
            pid = serializers.IntegerField()
            name = serializers.CharField()

        items = [Item1(), Item2()]
        expected_data = {
            'results': [
                {
                    'pid': 1,
                    'name': 'Hello',
                },
                {
                    'pid': 2,
                    'name': 'Aloah',
                },
            ],
            'count': 4,
        }
        response = MagicMock()
        response.status_code = 200
        response.headers = {}
        response.json = MagicMock(return_value=expected_data)
        test_case = APITestCase()
        test_case.assert_pagination_response(response, items, Serializer, 4)

__all__ = []
