import json
from django.http import HttpResponse
from rest_framework import status
from rest_framework.serializers import ValidationError

def get_validation_response(serializer):
    data = '{}'
    try:
        serializer.is_valid(raise_exception=True)
    except ValidationError as e:
        data = json.dumps(e.detail)
    
    resp = HttpResponse(
        data,
        status=status.HTTP_400_BAD_REQUEST,
        headers={
            'Content-Type': 'application/json'
        }
    )
    resp.json = lambda: json.loads(resp.content.decode())
    return resp
