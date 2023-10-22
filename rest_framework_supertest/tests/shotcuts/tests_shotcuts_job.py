from django.test import TestCase
from rest_framework_supertest.shotcuts import job
from .base import FakerMockMixin

class JobShotcuts(FakerMockMixin, TestCase):
    def test_job(self):
        self.exec_test(['job'], job, 'job_name')

    def test_unique_job(self):
        self.exec_test(['unique', 'job'], job, 'unique_job_name')
