from unittest.mock import MagicMock

from django.test import TestCase
from rest_framework.exceptions import APIException

from rest_framework_supertest.mixins import (
    AssertAPIExceptionMixin,
    AssertAPIResponseMixin,
)


class _AssertTestCase(AssertAPIExceptionMixin, AssertAPIResponseMixin, TestCase):
    pass

class AssertExceptionTestCase(TestCase):
    def test_without_assert_response_json(self) -> None:
        class _TestCase(AssertAPIExceptionMixin):
            pass

        msg_regex = '^(.*?)+assertAPIException method, assert_response_json(.*?)+$'
        with self.assertRaisesRegex(AttributeError, msg_regex):
            _TestCase().assert_api_exception(MagicMock(), MagicMock())

    def test_without_assert_response_headers(self) -> None:
        class _TestCase(AssertAPIExceptionMixin):
            def assert_response_json(self, *args: dict, **kwargs: dict) -> None:
                pass

        msg_regex = '^(.*?)+assertAPIException method, assert_response_headers(.*?)+$'
        with self.assertRaisesRegex(AttributeError, msg_regex):
            _TestCase().assert_api_exception(MagicMock(), MagicMock())

    def test_with_basic_exception(self) -> None:
        data = {
            'detail': 'test detail here',
        }
        status = 422
        headers = {}

        response = MagicMock()
        response.status_code = status
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _Exception(APIException):
            status_code = status
            default_detail = 'test detail here'

        _AssertTestCase().assert_api_exception(response, _Exception())

    def test_with_basic_exception_failing_data(self) -> None:
        data = {
            'error': 'test detail here',
        }
        status = 422
        headers = {}

        response = MagicMock()
        response.status_code = status
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _Exception(APIException):
            status_code = status
            default_detail = 'test detail here'

        with self.assertRaises(AssertionError):
            _AssertTestCase().assert_api_exception(response, _Exception())

    def test_with_basic_exception_failing_status(self) -> None:
        data = {
            'detail': 'test detail here',
        }
        status = 422
        headers = {}

        response = MagicMock()
        response.status_code = 500
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _Exception(APIException):
            status_code = status
            default_detail = 'test detail here'

        with self.assertRaises(AssertionError):
            _AssertTestCase().assert_api_exception(response, _Exception())

    def test_with_auth_header_exception(self) -> None:
        data = {
            'detail': 'test detail here',
        }
        status = 401
        auth_header_value = 'Bearer'
        headers = {
            'WWW-Authenticate': auth_header_value,
        }

        response = MagicMock()
        response.status_code = status
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _Exception(APIException):
            status_code = status
            default_detail = 'test detail here'
            auth_header = auth_header_value

        _AssertTestCase().assert_api_exception(response, _Exception())

    def test_with_auth_header_exception_failing_data(self) -> None:
        data = {
            'data': 'test detail here',
        }
        status = 401
        auth_header_value = 'Bearer'
        headers = {
            'WWW-Authenticate': auth_header_value,
        }

        response = MagicMock()
        response.status_code = status
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _Exception(APIException):
            status_code = status
            default_detail = 'test detail here'
            auth_header = auth_header_value

        with self.assertRaises(AssertionError):
            _AssertTestCase().assert_api_exception(response, _Exception())

    def test_with_auth_header_exception_failing_status(self) -> None:
        data = {
            'detail': 'test detail here',
        }
        status = 401
        auth_header_value = 'Bearer'
        headers = {
            'WWW-Authenticate': auth_header_value,
        }

        response = MagicMock()
        response.status_code = 422
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _Exception(APIException):
            status_code = status
            default_detail = 'test detail here'
            auth_header = auth_header_value

        with self.assertRaises(AssertionError):
            _AssertTestCase().assert_api_exception(response, _Exception())

    def test_with_auth_header_exception_failing_header(self) -> None:
        data = {
            'detail': 'test detail here',
        }
        status = 401
        auth_header_value = 'Bearer'
        headers = {
            '-Authenticate': auth_header_value,
        }

        response = MagicMock()
        response.status_code = status
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _Exception(APIException):
            status_code = status
            default_detail = 'test detail here'
            auth_header = auth_header_value

        with self.assertRaises(AssertionError):
            _AssertTestCase().assert_api_exception(response, _Exception())

    def test_with_retry_header_exception(self) -> None:
        data = {
            'detail': 'test detail here',
        }
        status = 422
        wait_value = 500
        headers = {
            'Retry-After': '%d' % wait_value,
        }

        response = MagicMock()
        response.status_code = status
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _Exception(APIException):
            status_code = status
            default_detail = 'test detail here'
            wait = wait_value

        _AssertTestCase().assert_api_exception(response, _Exception())

    def test_with_retry_header_exception_failing_data(self) -> None:
        data = {
            'data': 'test detail here',
        }
        status = 422
        wait_value = 500
        headers = {
            'Retry-After': '%d' % wait_value,
        }

        response = MagicMock()
        response.status_code = status
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _Exception(APIException):
            status_code = status
            default_detail = 'test detail here'
            wait = wait_value

        with self.assertRaises(AssertionError):
            _AssertTestCase().assert_api_exception(response, _Exception())

    def test_with_retry_header_exception_failing_status(self) -> None:
        data = {
            'detail': 'test detail here',
        }
        status = 422
        wait_value = 500
        headers = {
            'Retry-After': '%d' % wait_value,
        }

        response = MagicMock()
        response.status_code = 500
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _Exception(APIException):
            status_code = status
            default_detail = 'test detail here'
            wait = wait_value

        with self.assertRaises(AssertionError):
            _AssertTestCase().assert_api_exception(response, _Exception())

    def test_with_retry_header_exception_failing_header(self) -> None:
        data = {
            'detail': 'test detail here',
        }
        status = 422
        wait_value = 500
        headers = {
            'RetryAfter': '%d' % wait_value,
        }

        response = MagicMock()
        response.status_code = status
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _Exception(APIException):
            status_code = status
            default_detail = 'test detail here'
            wait = wait_value

        with self.assertRaises(AssertionError):
            _AssertTestCase().assert_api_exception(response, _Exception())

__all__ = []
