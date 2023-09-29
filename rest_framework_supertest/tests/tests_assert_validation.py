from django.test import TestCase
from rest_framework import serializers
from rest_framework_supertest.test import APITestCase
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