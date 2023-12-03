from typing import Optional
from unittest.mock import MagicMock, patch

from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.test import TestCase
from rest_framework import status
from rest_framework.exceptions import (
    APIException,
    AuthenticationFailed,
    NotAuthenticated,
    NotFound,
)
from rest_framework.exceptions import PermissionDenied as ApiPermissionDenied

from rest_framework_supertest.utils.exceptions import APIExceptionsUtils


class FakeViewHeader:
    def get_authenticate_header(self, _: object) -> Optional[str]:
        return "HEADER_HERE"

class FakeViewNoHeader:
    def get_authenticate_header(self, _: object) -> Optional[str]:
        return None

class APIExceptionsUtilsTests(TestCase):
    def setUp(self) -> None:
        self.response = MagicMock()
        self.response.wsgi_request = MagicMock()

    def test_transform_exception_http404(self) -> None:
        utils = APIExceptionsUtils(self.response, Http404())
        self.assertEqual(type(utils.exc), NotFound)

    def test_transform_exception_permission_denied(self) -> None:
        utils = APIExceptionsUtils(self.response, PermissionDenied())
        self.assertEqual(type(utils.exc), ApiPermissionDenied)

    def test_get_authenticate_header_without_request(self) -> None:
        self.response = MagicMock()
        self.response.wsgi_request = None
        utils = APIExceptionsUtils(self.response, MagicMock())
        self.assertIsNone(utils.get_authenticate_header())

    def test_get_authenticate_header_view_class(self) -> None:
        path = '/my-path-here'

        self.response = MagicMock()
        self.response.wsgi_request = MagicMock()
        self.response.wsgi_request.path = path
        with patch('rest_framework_supertest.utils.exceptions.resolve') as resolve:
            FakeViewHeader.get_authenticate_header.view_class = FakeViewHeader
            resolve.return_value = FakeViewHeader.get_authenticate_header, '', ''

            utils = APIExceptionsUtils(self.response, MagicMock())
            self.assertEqual(utils.get_authenticate_header(), "HEADER_HERE")
            resolve.assert_called_once_with(path)

    def test_get_authenticate_header_view_class_none_value(self) -> None:
        path = '/q-path-here'

        self.response = MagicMock()
        self.response.wsgi_request = MagicMock()
        self.response.wsgi_request.path = path
        with patch('rest_framework_supertest.utils.exceptions.resolve') as resolve:
            FakeViewNoHeader.get_authenticate_header.view_class = FakeViewNoHeader
            resolve.return_value = FakeViewNoHeader.get_authenticate_header, '', ''

            utils = APIExceptionsUtils(self.response, MagicMock())
            self.assertIsNone(utils.get_authenticate_header())
            resolve.assert_called_once_with(path)

    def test_handle_auth_headers_without_auth_exceptions(self) -> None:
        exc = NotFound()
        utils = APIExceptionsUtils(self.response, exc)
        utils.handle_auth_headers()
        self.assertFalse(hasattr(exc, 'auth_header'))
        self.assertNotEqual(exc.status_code, status.HTTP_403_FORBIDDEN)

    def test_handle_auth_headers_with_auth_exceptions_header(self) -> None:
        header = 'HEADER HERE!'
        exc = AuthenticationFailed()
        utils = APIExceptionsUtils(self.response, exc)
        utils.get_authenticate_header = lambda: header
        utils.handle_auth_headers()
        self.assertEqual(exc.auth_header, header)
        self.assertNotEqual(exc.status_code, status.HTTP_403_FORBIDDEN)

    def test_handle_auth_headers_with_auth_exceptions_header2(self) -> None:
        header = 'HEADER HERE!'
        exc = NotAuthenticated()
        utils = APIExceptionsUtils(self.response, exc)
        utils.get_authenticate_header = lambda: header
        utils.handle_auth_headers()
        self.assertEqual(exc.auth_header, header)
        self.assertNotEqual(exc.status_code, status.HTTP_403_FORBIDDEN)

    def test_handle_auth_headers_without_auth_header(self) -> None:
        exc = NotAuthenticated()
        utils = APIExceptionsUtils(self.response, exc)
        utils.get_authenticate_header = lambda: None
        utils.handle_auth_headers()
        self.assertFalse(hasattr(exc, 'auth_header'))
        self.assertEqual(exc.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_headers_auth_header(self) -> None:
        header = 'NEW HEADER!'
        exc = MagicMock()
        exc.auth_header = header
        exc.wait = None
        utils = APIExceptionsUtils(self.response, exc)
        data = utils.get_headers()
        self.assertDictEqual(data, {
            'WWW-Authenticate': header,
        })

    def test_get_headers_wait(self) -> None:
        exc = MagicMock()
        exc.auth_header = None
        exc.wait = 5
        utils = APIExceptionsUtils(self.response, exc)
        data = utils.get_headers()
        self.assertDictEqual(data, {
            'Retry-After': '5',
        })

    def test_get_headers_auth_header_wait(self) -> None:
        header = 'NEW HEADER!'
        exc = MagicMock()
        exc.auth_header = header
        exc.wait = 5
        utils = APIExceptionsUtils(self.response, exc)
        data = utils.get_headers()
        self.assertDictEqual(data, {
            'WWW-Authenticate': header,
            'Retry-After': '5',
        })

    def test_get_data_list(self) -> None:
        data = ['any data here?']
        exc = MagicMock()
        exc.detail = data
        utils = APIExceptionsUtils(self.response, exc)
        self.assertListEqual(utils.get_data(), data)

    def test_get_data_dict(self) -> None:
        data = {'any': ['any data here?']}
        exc = MagicMock()
        exc.detail = data
        utils = APIExceptionsUtils(self.response, exc)
        self.assertDictEqual(utils.get_data(), data)

    def test_get_data_str(self) -> None:
        data = 'any data here?'
        exc = MagicMock()
        exc.detail = data
        utils = APIExceptionsUtils(self.response, exc)
        self.assertDictEqual(utils.get_data(), {'detail': data})

    def test_exception_handler_without_exception(self) -> None:
        exc = MagicMock()
        utils = APIExceptionsUtils(self.response, exc)
        with self.assertRaises(NotImplementedError):
            utils.exception_handler()

    def test_exception_handler_with_valid_exception(self) -> None:
        exc = APIException()
        exc.auth_header = 'EXAMPLE'
        exc.wait = 10
        exc.status_code = 422
        exc.detail = {'test': 'data', 'error': 'exception'}
        utils = APIExceptionsUtils(self.response, exc)
        data, status, headers = utils.exception_handler()
        self.assertEqual(status, 422)
        self.assertDictEqual(data, {'test': 'data', 'error': 'exception'})
        self.assertDictEqual(headers, {
            'WWW-Authenticate': 'EXAMPLE',
            'Retry-After': '10',
        })

__all__ = []
