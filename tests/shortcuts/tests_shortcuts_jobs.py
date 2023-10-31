from rest_framework_supertest.shortcuts import jobs

from . import ShortcutTestCase


class JobsShortcutsTests(ShortcutTestCase):
    def test_job(self) -> None:
        self.exec_test(['job'], jobs, 'job_name')

    def test_unique_job(self) -> None:
        self.exec_test(['unique', 'job'], jobs, 'unique_job_name')

__all__ = []
