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
    def test_with_none_exceptions(self) -> None:
        with self.assertRaises(AssertionError):
            _AssertTestCase().assert_one_of_api_exceptions(MagicMock(), [])

    def test_with_one_exception(self) -> None:
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

        exceptions = [_Exception()]

        _AssertTestCase().assert_one_of_api_exceptions(response, exceptions)

    def test_with_one_exception_failing_data(self) -> None:
        data = {}
        status = 500
        headers = {}

        response = MagicMock()
        response.status_code = status
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _Exception(APIException):
            status_code = status
            default_detail = 'test detail here'

        exceptions = [_Exception()]

        with self.assertRaises(AssertionError):
            _AssertTestCase().assert_one_of_api_exceptions(response, exceptions)

    def test_with_one_exception_failing_status(self) -> None:
        data = {
            'detail': 'test detail here',
        }
        status = 500
        headers = {}

        response = MagicMock()
        response.status_code = 422
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _Exception(APIException):
            status_code = status
            default_detail = 'test detail here'

        exceptions = [_Exception()]

        with self.assertRaises(AssertionError):
            _AssertTestCase().assert_one_of_api_exceptions(response, exceptions)

    def test_with_multiple_exceptions_passing(self) -> None:
        data = {
            'detail': 'test detail here',
        }
        status = 500
        headers = {}

        response = MagicMock()
        response.status_code = status
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _FailException(APIException):
            status_code = 500
            default_detail = 'test detail here'

        class _Exception(APIException):
            status_code = status
            default_detail = 'test detail here'

        exceptions = [_Exception(), _FailException()]

        _AssertTestCase().assert_one_of_api_exceptions(response, exceptions)

    def test_with_multiple_exceptions_failing(self) -> None:
        data = {
            'detail': 'test detail here',
        }
        status = 500
        headers = {}

        response = MagicMock()
        response.status_code = status
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _FailException(APIException):
            status_code = 401
            default_detail = 'test detail here'

        class _Exception(APIException):
            status_code = 422
            default_detail = 'test detail here'

        exceptions = [_Exception(), _FailException()]

        with self.assertRaises(AssertionError):
            _AssertTestCase().assert_one_of_api_exceptions(response, exceptions)

    def test_with_multiple_exceptions_failing_by_header_wait(self) -> None:
        data = {
            'detail': 'test detail here',
        }
        status = 500
        headers = {}
        wait_value = 200

        response = MagicMock()
        response.status_code = status
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _FailException(APIException):
            status_code = status
            default_detail = 'test detail here'
            wait = wait_value

        class _Exception(APIException):
            status_code = 422
            default_detail = 'test detail here'

        exceptions = [_Exception(), _FailException()]

        with self.assertRaises(AssertionError):
            _AssertTestCase().assert_one_of_api_exceptions(response, exceptions)

    def test_with_multiple_exceptions_failing_by_header_auth(self) -> None:
        data = {
            'detail': 'test detail here',
        }
        status = 500
        headers = {}
        auth_header_value = 'bearer'

        response = MagicMock()
        response.status_code = status
        response.headers = headers
        response.json = MagicMock(return_value=data)

        class _FailException(APIException):
            status_code = status
            default_detail = 'test detail here'
            auth_header = auth_header_value

        class _Exception(APIException):
            status_code = 422
            default_detail = 'test detail here'

        exceptions = [_Exception(), _FailException()]

        with self.assertRaises(AssertionError):
            _AssertTestCase().assert_one_of_api_exceptions(response, exceptions)

__all__ = []
