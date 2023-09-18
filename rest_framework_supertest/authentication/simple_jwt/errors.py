from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt import exceptions as jwt_exceptions
from rest_framework import exceptions

NO_ACTIVE_ACCOUNT = exceptions.AuthenticationFailed(
    TokenObtainSerializer.default_error_messages["no_active_account"],
    "no_active_account",
)

TWO_AUTORIZATION_PARTS = jwt_exceptions.AuthenticationFailed(
    _("Authorization header must contain two space-delimited values"),
    code="bad_authorization_header",
)

TOKEN_NOT_VALID_FOR_ANY_TOKEN_TYPE = jwt_exceptions.InvalidToken({
    "detail": _("Given token not valid for any token type"),
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid or expired",
        }
    ],
})

TOKEN_NO_RECOGNIZABLE_USER_ID = jwt_exceptions.InvalidToken(
    _("Token contained no recognizable user identification")
)

__all__ = [
    'NO_ACTIVE_ACCOUNT', 'TWO_AUTORIZATION_PARTS', 'TOKEN_NOT_VALID_FOR_ANY_TOKEN_TYPE',
    'TOKEN_NO_RECOGNIZABLE_USER_ID',
]
