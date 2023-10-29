from ._utils import unique


def credit_card_expire(fake, start='now', end='+10y', date_format='%m/%y'):
    """
    Generate a credit card expiry date.

    This method uses date_time_between() under the hood to generate the
    expiry date, so the start and end arguments work in the same way
    here as it would in that method. For the actual formatting
    of the expiry date, strftime() is used and date_format
    is simply passed to that method.
    """
    return fake.credit_card_expire()

def unique_credit_card_expire(fake):
    """
    Generate a unique credit card expiry date.

    This method uses date_time_between() under the hood to generate the
    expiry date, so the start and end arguments work in the same way
    here as it would in that method. For the actual formatting
    of the expiry date, strftime() is used and date_format
    is simply passed to that method.
    """
    return unique(fake, credit_card_expire)

def credit_card_number(fake, card_type=None):
    """
    Generate a valid credit card number.

    Args:
        card_type: if value is None, a random type is used. The
          list of valid card types includes 'amex', 'diners',
          'discover', 'jcb', 'jcb15', 'jcb16', 'maestro',
          'mastercard', 'visa', 'visa13', 'visa16', and 'visa19'.
    """
    return fake.credit_card_number(card_type=card_type)

def unique_credit_card_number(fake, card_type=None):
    """
    Generate a valid unique credit card number.

    Args:
        card_type: if value is None, a random type is used. The
          list of valid card types includes 'amex', 'diners',
          'discover', 'jcb', 'jcb15', 'jcb16', 'maestro',
          'mastercard', 'visa', 'visa13', 'visa16', and 'visa19'.
    """
    return unique(fake, credit_card_number, card_type=card_type)

def credit_card_provider(fake, card_type=None):
    """
    Generate a credit card provider name.

    Args:
        card_type: if value is None, a random type is used. The
          list of valid card types includes 'amex', 'diners',
          'discover', 'jcb', 'jcb15', 'jcb16', 'maestro',
          'mastercard', 'visa', 'visa13', 'visa16', and 'visa19'.
    """
    return fake.credit_card_provider(card_type=card_type)

def unique_credit_card_provider(fake, card_type=None):
    """
    Generate a unique credit card provider name.

    Args:
        card_type: if value is None, a random type is used. The
          list of valid card types includes 'amex', 'diners',
          'discover', 'jcb', 'jcb15', 'jcb16', 'maestro',
          'mastercard', 'visa', 'visa13', 'visa16', and 'visa19'.
    """
    return unique(fake, credit_card_provider, card_type=card_type)

def credit_card_security_code(fake, card_type=None):
    """
    Generate a credit card security code.

    Args:
        card_type: if value is None, a random type is used. The
          list of valid card types includes 'amex', 'diners',
          'discover', 'jcb', 'jcb15', 'jcb16', 'maestro',
          'mastercard', 'visa', 'visa13', 'visa16', and 'visa19'.
    """
    return fake.credit_card_security_code(card_type=card_type)

def unique_credit_card_security_code(fake, card_type=None):
    """
    Generate a unique credit card security code.

    Args:
        card_type: if value is None, a random type is used. The
          list of valid card types includes 'amex', 'diners',
          'discover', 'jcb', 'jcb15', 'jcb16', 'maestro',
          'mastercard', 'visa', 'visa13', 'visa16', and 'visa19'.
    """
    return unique(fake, credit_card_security_code, card_type=card_type)
