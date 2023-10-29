from django.test import TestCase

from rest_framework_supertest.shortcuts import credit_cards

from .base import FakerMockMixin


class CreditCardsShortcutsTests(FakerMockMixin, TestCase):
    def test_credit_card_expire(self):
        self.exec_test(['credit_card_expire'], credit_cards, 'credit_card_expire')

    def test_unique_credit_card_expire(self):
        self.exec_test(['unique', 'credit_card_expire'], credit_cards, 'unique_credit_card_expire')

    def test_credit_card_number(self):
        card_type = 'jcb15'
        self.exec_test(['credit_card_number'], credit_cards, 'credit_card_number', card_type=card_type)

    def test_unique_credit_card_number(self):
        card_type = 'jcb15'
        self.exec_test(['unique', 'credit_card_number'], credit_cards, 'unique_credit_card_number', card_type=card_type)

    def test_credit_card_provider(self):
        card_type = 'jcb15'
        self.exec_test(['credit_card_provider'], credit_cards, 'credit_card_provider', card_type=card_type)

    def test_unique_credit_card_provider(self):
        card_type = 'jcb15'
        self.exec_test(['unique', 'credit_card_provider'], credit_cards, 'unique_credit_card_provider', card_type=card_type)

    def test_credit_card_security_code(self):
        card_type = 'jcb15'
        self.exec_test(['credit_card_security_code'], credit_cards, 'credit_card_security_code', card_type=card_type)

    def test_unique_credit_card_security_code(self):
        card_type = 'jcb15'
        self.exec_test(['unique', 'credit_card_security_code'], credit_cards, 'unique_credit_card_security_code', card_type=card_type)

