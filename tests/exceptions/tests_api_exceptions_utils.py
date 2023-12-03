from typing import Optional
from unittest.mock import MagicMock, patch

from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.test import TestCase
from rest_framework.exceptions import NotFound
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

__all__ = []
