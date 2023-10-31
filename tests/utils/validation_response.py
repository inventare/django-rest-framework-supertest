import json

from django.http import HttpResponse
from rest_framework import status
from rest_framework.serializers import Serializer, ValidationError


def get_validation_response(serializer: Serializer) -> HttpResponse:
    """
    Return a `django.http.HttpResponse` with bad request validation.

    Call `serializer.is_valid(raise_exception=True)`, handle this
    `rest_framework.serializers.ValidationError` exception and
    create an `django.http.HttpResponse` with Bad Request
    status and data from `rest_framework.serializers.ValidationError`.

    Args:
        serializer: The `rest_framework.serializers.Serializer` to
          validate and mount the `django.http.HttpResponse` with
          `rest_framework.serializers.ValidationError`.

    Returns:
        A `django.http.HttpResponse`.
    """
    data = '{}'
    try:
        serializer.is_valid(raise_exception=True)
    except ValidationError as e:
        data = json.dumps(e.detail)

    resp = HttpResponse(
        data,
        status=status.HTTP_400_BAD_REQUEST,
        headers={
            'Content-Type': 'application/json',
        },
    )
    resp.json = lambda: json.loads(resp.content.decode())
    return resp
