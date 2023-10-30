from rest_framework_supertest.shortcuts import misc

from . import ShortcutTestCase


class MiscShortcutsTests(ShortcutTestCase):
    def test_boolean(self) -> None:
        chance_of_getting_true = 40
        self.exec_test(
            ['boolean'],
            misc,
            'boolean',
            chance_of_getting_true=chance_of_getting_true,
        )

    def test_null_boolean(self) -> None:
        self.exec_test(['null_boolean'], misc, 'null_boolean')

    def test_password(self) -> None:
        length = 50
        special_chars = True
        digits = False
        upper_case = True
        lower_case = False
        self.exec_test(
            ['password'],
            misc,
            'password',
            length=length,
            special_chars=special_chars,
            digits=digits,
            upper_case=upper_case,
            lower_case=lower_case,
        )

    def test_uuid4(self) -> None:
        cast_to = None
        self.exec_test(['uuid4'], misc, 'uuid4', cast_to=cast_to)

__all__ = []
