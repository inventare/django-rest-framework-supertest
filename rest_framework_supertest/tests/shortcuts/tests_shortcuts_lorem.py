from django.test import TestCase
from rest_framework_supertest.shortcuts import lorem
from .base import FakerMockMixin

class LoremShortcutsTests(FakerMockMixin, TestCase):
    def test_paragraph(self):
        nb_sentences = 10
        variable_nb_sentences = True
        ext_word_list = None
        self.exec_test(
            ['paragraph'],
            lorem,
            'paragraph',
            nb_sentences=nb_sentences,
            variable_nb_sentences=variable_nb_sentences,
            ext_word_list=ext_word_list
        )

    def test_unique_paragraph(self):
        nb_sentences = 10
        variable_nb_sentences = True
        ext_word_list = None
        self.exec_test(
            ['unique', 'paragraph'],
            lorem,
            'unique_paragraph',
            nb_sentences=nb_sentences,
            variable_nb_sentences=variable_nb_sentences,
            ext_word_list=ext_word_list
        )

    def test_sentence(self):
        nb_words = 20
        variable_nb_words = False
        ext_word_list = None
        self.exec_test(
            ['sentence'],
            lorem,
            'sentence',
            nb_words=nb_words,
            variable_nb_words=variable_nb_words,
            ext_word_list=ext_word_list
        )

    def test_unique_sentence(self):
        nb_words = 20
        variable_nb_words = False
        ext_word_list = None
        self.exec_test(
            ['unique', 'sentence'],
            lorem,
            'unique_sentence',
            nb_words=nb_words,
            variable_nb_words=variable_nb_words,
            ext_word_list=ext_word_list
        )

    def test_text(self):
        max_nb_chars = 400
        ext_word_list = None
        self.exec_test(['text'], lorem, 'text', max_nb_chars=max_nb_chars, ext_word_list=ext_word_list)

    def test_unique_text(self):
        max_nb_chars = 400
        ext_word_list = None
        self.exec_test(['unique', 'text'], lorem, 'unique_text', max_nb_chars=max_nb_chars, ext_word_list=ext_word_list)
        
    def test_word(self):
        part_of_speech = 'subject'
        ext_word_list = []
        self.exec_test(['word'], lorem, 'word', part_of_speech=part_of_speech, ext_word_list=ext_word_list)

    def test_unique_word(self):
        part_of_speech = 'subject'
        ext_word_list = []
        self.exec_test(['unique', 'word'], lorem, 'unique_word', part_of_speech=part_of_speech, ext_word_list=ext_word_list)
        