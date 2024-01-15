from django.test import TestCase
from rest_framework import serializers

from rest_framework_supertest.mixins import AssertAPIValidationMixin
from rest_framework_supertest.test import APITestCase
from tests.utils import get_validation_response


class AssertValidationTestCase(TestCase):
    def test_basic_validation_field(self) -> None:
        class Serializer(serializers.Serializer):
            email = serializers.EmailField()
            name = serializers.CharField()

        serializer = Serializer(data={})
        response = get_validation_response(serializer)

        case = APITestCase()
        case.assert_has_validation_field(response, 'email', 'This field is required.')
        case.assert_has_validation_field(response, 'name', 'This field is required.')

    def test_basic_validation_field_without_message(self) -> None:
        class Serializer(serializers.Serializer):
            email = serializers.EmailField()
            name = serializers.CharField()

        serializer = Serializer(data={})
        response = get_validation_response(serializer)

        case = APITestCase()
        case.assert_has_validation_field(response, 'email')
        case.assert_has_validation_field(response, 'name')

    def test_validation_field_inside_array(self) -> None:
        class Child(serializers.Serializer):
            name = serializers.CharField()

        class Serializer(serializers.Serializer):
            childs = Child(many=True)

        serializer = Serializer(data={
            'childs': [
                {'name': 'aaa'},
                {},
            ],
        })
        response = get_validation_response(serializer)

        case = APITestCase()
        case.assert_has_validation_field(
            response,
            ['childs', 1, 'name'],
            'This field is required.',
        )

    def test_validation_field_inside_array_without_message(self) -> None:
        class Child(serializers.Serializer):
            name = serializers.CharField()

        class Serializer(serializers.Serializer):
            childs = Child(many=True)

        serializer = Serializer(data={
            'childs': [
                {'name': 'aaa'},
                {},
            ],
        })
        response = get_validation_response(serializer)

        case = APITestCase()
        case.assert_has_validation_field(response, ['childs', 1, 'name'])

    def test_validation_response_with_array(self) -> None:
        class Child(serializers.Serializer):
            name = serializers.CharField()

        class Serializer(serializers.Serializer):
            childs = Child(many=True)

        serializer = Serializer(data={
            'childs': [
                {'name': 'aaa'},
                {},
            ],
        })
        response = get_validation_response(serializer)

        case = APITestCase()
        case.assert_validation_response(
            response,
            {
                'childs': [
                    {},
                    {'name': ['This field is required.']},
                ],
            },
        )

    def test_validation_response_with_one_field(self) -> None:
        class Serializer(serializers.Serializer):
            email = serializers.EmailField()
            name = serializers.CharField()

        serializer = Serializer(data={})
        response = get_validation_response(serializer)

        case = APITestCase()
        case.assert_validation_response(
            response,
            {
                'email': ['This field is required.'],
                'name': ['This field is required.'],
            },
        )

    def test_validation_response_without_assert_api_exception(self) -> None:
        class Serializer(serializers.Serializer):
            email = serializers.EmailField()
            name = serializers.CharField()

        serializer = Serializer(data={})
        response = get_validation_response(serializer)

        case = AssertAPIValidationMixin()
        with self.assertRaises(AttributeError):
            case.assert_validation_response(response, {})

__all__ = []
