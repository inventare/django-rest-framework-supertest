# API Exception's

This text introduces our philosophy about using API Exceptions to handle errors when writing django REST API's.

## Introduction

One of the possibles way to handle errors in django rest framework REST API's is writing manual responses on views, like that:

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class SomeAPIView(APIView):
    def post(self, request):
        if not condition:
            return Response({ 'detail': 'my any error', }, status=422)
```

or, without using early-return:

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class SomeAPIView(APIView):
    def post(self, request):
        if condition:
            # process here
        else:
            return Response({ 'detail': 'my any error', }, status=422)
```

This is not a good way of handle errors with django rest framework, specially for our package, because whe need to assert manually the response body and status. A other side of the problem is the cognitive load of multiple responses returning in one view function. The `APIException` concept solve the both problems.

### Example

The example bellow does the same logic, and return an 422 response with an detail if condition is false, like the above methods:

```python
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CustomAPIException(APIException):
    default_detail = 'my any error'
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY


class SomeAPIView(APIView):
    def post(self, request):
        if not condition:
            raise CustomAPIException()
        # process request

```

## One customizable APIException vs Multiple APIException

One example of using customizable `APIException` is present on the `rest_framework_simplejwt` package:


```python
# ...
class TokenObtainSerializer(serializers.Serializer):
    # ...
    default_error_messages = {
        "no_active_account": _("No active account found with the given credentials")
    }

    def validate(self, attrs: Dict[str, Any]) -> Dict[Any, Any]:
        # ...
        if not api_settings.USER_AUTHENTICATION_RULE(self.user):
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_account"],
                "no_active_account",
            )
        # ...
```

For the purpose of this testing utilities package, using this way is a little bad for some reasons: this moves the detail and codes to the `APIView` or `Serializer` and, then, make the code a little more verbose than writing one APIException for each error and add more cognitive load on this code.

For this testing package, this is a little bad because we need to redeclare this exceptions inside our tests, like this:

```python
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework.exceptions import AuthenticationFailed as BaseAuthenticationFailed

NO_ACTIVE_ACCOUNT = BaseAuthenticationFailed(
    TokenObtainSerializer.default_error_messages["no_active_account"],
    "no_active_account",
)

TWO_AUTORIZATION_PARTS = AuthenticationFailed(
    _("Authorization header must contain two space-delimited values"),
    code="bad_authorization_header",
)

# ...
```
