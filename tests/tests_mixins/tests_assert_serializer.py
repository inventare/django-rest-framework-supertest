from unittest.mock import MagicMock

from django.test import TestCase
from rest_framework import serializers

from rest_framework_supertest.test import APITestCase


class AssertSerializerTestCase(TestCase):
    def test_assert_serializer_data(self) -> None:
        expected = {
            'email': 'example@example.com.br',
            'name': 'example',
        }

        class Serializer(serializers.Serializer):
            email = serializers.EmailField()
            name = serializers.CharField()

        class Instance:
            email = 'example@example.com.br'
            name = 'example'

        serializer = Serializer(instance=Instance())
        case = APITestCase()
        case.assert_serializer_data(expected, serializer)

    def test_assert_serializer_response_data(self) -> None:
        expected = {
            'email': 'example@example.com.br',
            'name': 'example',
        }

        class Serializer(serializers.Serializer):
            email = serializers.EmailField()
            name = serializers.CharField()

        class Instance:
            email = 'example@example.com.br'
            name = 'example'

        response = MagicMock()
        response.status_code = 500
        response.json = MagicMock(return_value=expected)

        serializer = Serializer(instance=Instance())
        case = APITestCase()
        case.assert_serializer_response_data(response, serializer)

__all__ = []
