from unittest.mock import MagicMock

from django.test import TestCase

from rest_framework_supertest.mixins import AssertAPIResponseMixin


class _AssertTestCase(AssertAPIResponseMixin, TestCase):
    pass

class AssertResponseTestCase(TestCase):
    def test_response_json_equals(self) -> None:
        data = {
            'any': 'any-json-field',
            'data': 1000,
            'nested': {
                'dum': 'aloah',
                'array': [
                    {'name': 'name'},
                ],
            },
        }
        response = MagicMock()
        response.json = MagicMock(return_value=data)

        mixin = _AssertTestCase()
        self.assertIsNone(mixin.assert_response_json(response, data))

    def test_response_json_raised(self) -> None:
        data = {
            'any': 'any-json-field',
            'data': 1000,
        }
        response_data = {
            **data,
            'nested': {
                'dum': 'aloah',
                'array': [
                    {'name': 'name'},
                ],
            },
        }
        response = MagicMock()
        response.json = MagicMock(return_value=response_data)

        mixin = _AssertTestCase()
        with self.assertRaises(AssertionError):
            mixin.assert_response_json(response, data)

    def test_response_json_without_assert_equals(self) -> None:
        data = {}
        response = MagicMock()
        response.json = MagicMock(return_value=data)

        mixin = AssertAPIResponseMixin()
        with self.assertRaises(AttributeError):
            mixin.assert_response_json(response, data)

    def test_response_headers_failing_with_item(self) -> None:
        response = MagicMock()
        response.headers = {
            'Authentication': 'any',
        }

        mixin = _AssertTestCase()
        with self.assertRaises(AssertionError):
            mixin.assert_response_headers(response, {'Authentication': 'new'})

    def test_response_headers_failing_without_item(self) -> None:
        response = MagicMock()
        response.headers = {
            'Authentication': 'any',
        }

        mixin = _AssertTestCase()
        with self.assertRaises(AssertionError):
            mixin.assert_response_headers(response, {'X-Auth': 'new'})

    def test_response_headers_success_without_headers(self) -> None:
        response = MagicMock()
        response.headers = {
            'Authentication': 'any',
        }

        mixin = _AssertTestCase()
        mixin.assert_response_headers(response, {})

    def test_response_headers_success_with_item(self) -> None:
        response = MagicMock()
        response.headers = {
            'Authentication': 'any',
            'X-Auth': 'test',
        }

        mixin = _AssertTestCase()
        mixin.assert_response_headers(response, {'X-Auth': 'test'})

__all__ = []
