from django.test import TestCase
from rest_framework import serializers
from rest_framework_supertest.test import APITestCase
from rest_framework_supertest.mixins import AssertAPIValidationMixin
from rest_framework_supertest.tests.utils import get_validation_response

class ATestCase(TestCase):
    def test_basic_validation_field(self):
        class Serializer(serializers.Serializer):
            email = serializers.EmailField()
            name = serializers.CharField()
        
        serializer = Serializer(data={})
        response = get_validation_response(serializer)
        
        case = APITestCase()
        case.assertHasValidationField(response, 'email', 'This field is required.')
        case.assertHasValidationField(response, 'name', 'This field is required.')

    def test_basic_validation_field_without_message(self):
        class Serializer(serializers.Serializer):
            email = serializers.EmailField()
            name = serializers.CharField()
        
        serializer = Serializer(data={})
        response = get_validation_response(serializer)
        
        case = APITestCase()
        case.assertHasValidationField(response, 'email')
        case.assertHasValidationField(response, 'name')

    def test_validation_field_inside_array(self):
        class Child(serializers.Serializer):
            name = serializers.CharField()

        class Serializer(serializers.Serializer):
            childs = Child(many=True)
        
        serializer = Serializer(data={
            'childs': [
                { 'name': 'aaa' },
                {}
            ]
        })
        response = get_validation_response(serializer)
        
        case = APITestCase()
        case.assertHasValidationField(response, ['childs', 1, 'name'], 'This field is required.')

    def test_validation_field_inside_array_without_message(self):
        class Child(serializers.Serializer):
            name = serializers.CharField()

        class Serializer(serializers.Serializer):
            childs = Child(many=True)
        
        serializer = Serializer(data={
            'childs': [
                { 'name': 'aaa' },
                {}
            ]
        })
        response = get_validation_response(serializer)
        
        case = APITestCase()
        case.assertHasValidationField(response, ['childs', 1, 'name'])

    def test_validation_response_with_array(self):
        class Child(serializers.Serializer):
            name = serializers.CharField()

        class Serializer(serializers.Serializer):
            childs = Child(many=True)
        
        serializer = Serializer(data={
            'childs': [
                { 'name': 'aaa' },
                {}
            ]
        })
        response = get_validation_response(serializer)
        
        case = APITestCase()
        case.assertValidationResponse(
            response,
            {
                'childs': [
                    {},
                    { 'name': ['This field is required.'] }
                ]
            }
        )
    
    def test_validation_response_with_one_field(self):
        class Serializer(serializers.Serializer):
            email = serializers.EmailField()
            name = serializers.CharField()
        
        serializer = Serializer(data={})
        response = get_validation_response(serializer)
        
        case = APITestCase()
        case.assertValidationResponse(
            response,
            {
                'email': ['This field is required.'],
                'name': ['This field is required.']
            }
        )

    def test_validation_response_without_assertAPIException(self):
        class Serializer(serializers.Serializer):
            email = serializers.EmailField()
            name = serializers.CharField()
        
        serializer = Serializer(data={})
        response = get_validation_response(serializer)
        
        case = AssertAPIValidationMixin()
        with self.assertRaises(AttributeError):
            case.assertValidationResponse(response, {})
