from typing import Optional

from ._utils import unique
from .typing import DateParseType


def credit_card_expire(
    fake: object,
    start: DateParseType = 'now',
    end: DateParseType = '+10y',
    date_format: str = '%m/%y',
) -> str:
    """
    Generate a credit card expiry date.

    To format of the expiry date, strftime() is used and
    date_format is simply passed to that method.

    Args:
        fake: The `Faker` instance.
        start: the start date to generate the expiry date.
        end: the end date to generate the expiry date.
        date_format: the date format of the expiry date.
    """
    return fake.credit_card_expire(start=start, end=end, date_format=date_format)

def unique_credit_card_expire(
    fake: object,
    start: DateParseType = 'now',
    end: DateParseType = '+10y',
    date_format: str = '%m/%y',
) -> str:
    """
    Generate a unique credit card expiry date.

    To format of the expiry date, strftime() is used and
    date_format is simply passed to that method.

    Args:
        fake: The `Faker` instance.
        start: the start date to generate the expiry date.
        end: the end date to generate the expiry date.
        date_format: the date format of the expiry date.
    """
    return unique(
        fake,
        credit_card_expire,
        start=start,
        end=end,
        date_format=date_format,
    )

def credit_card_number(fake: object, card_type: Optional[str] = None) -> str:
    """
    Generate a valid credit card number.

    Args:
        fake: The `Faker` instance.
        card_type: if value is None, a random type is used. The
          list of valid card types includes 'amex', 'diners',
          'discover', 'jcb', 'jcb15', 'jcb16', 'maestro',
          'mastercard', 'visa', 'visa13', 'visa16', and 'visa19'.
    """
    return fake.credit_card_number(card_type=card_type)

def unique_credit_card_number(fake: object, card_type: Optional[str] = None) -> str:
    """
    Generate a valid unique credit card number.

    Args:
        fake: The `Faker` instance.
        card_type: if value is None, a random type is used. The
          list of valid card types includes 'amex', 'diners',
          'discover', 'jcb', 'jcb15', 'jcb16', 'maestro',
          'mastercard', 'visa', 'visa13', 'visa16', and 'visa19'.
    """
    return unique(fake, credit_card_number, card_type=card_type)

def credit_card_provider(fake: object, card_type: Optional[str] = None) -> str:
    """
    Generate a credit card provider name.

    Args:
        fake: The `Faker` instance.
        card_type: if value is None, a random type is used. The
          list of valid card types includes 'amex', 'diners',
          'discover', 'jcb', 'jcb15', 'jcb16', 'maestro',
          'mastercard', 'visa', 'visa13', 'visa16', and 'visa19'.
    """
    return fake.credit_card_provider(card_type=card_type)

def unique_credit_card_provider(fake: object, card_type: Optional[str] = None) -> str:
    """
    Generate a unique credit card provider name.

    Args:
        fake: The `Faker` instance.
        card_type: if value is None, a random type is used. The
          list of valid card types includes 'amex', 'diners',
          'discover', 'jcb', 'jcb15', 'jcb16', 'maestro',
          'mastercard', 'visa', 'visa13', 'visa16', and 'visa19'.
    """
    return unique(fake, credit_card_provider, card_type=card_type)

def credit_card_security_code(fake: object, card_type: Optional[str] = None) -> str:
    """
    Generate a credit card security code.

    Args:
        fake: The `Faker` instance.
        card_type: if value is None, a random type is used. The
          list of valid card types includes 'amex', 'diners',
          'discover', 'jcb', 'jcb15', 'jcb16', 'maestro',
          'mastercard', 'visa', 'visa13', 'visa16', and 'visa19'.
    """
    return fake.credit_card_security_code(card_type=card_type)

def unique_credit_card_security_code(
    fake: object,
    card_type: Optional[str] = None,
) -> str:
    """
    Generate a unique credit card security code.

    Args:
        fake: The `Faker` instance.
        card_type: if value is None, a random type is used. The
          list of valid card types includes 'amex', 'diners',
          'discover', 'jcb', 'jcb15', 'jcb16', 'maestro',
          'mastercard', 'visa', 'visa13', 'visa16', and 'visa19'.
    """
    return unique(fake, credit_card_security_code, card_type=card_type)
