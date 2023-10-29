from django.test import TestCase

from rest_framework_supertest.shortcuts import jobs

from .base import FakerMockMixin


class JobsShortcutsTests(FakerMockMixin, TestCase):
    def test_job(self):
        self.exec_test(['job'], jobs, 'job_name')

    def test_unique_job(self):
        self.exec_test(['unique', 'job'], jobs, 'unique_job_name')
