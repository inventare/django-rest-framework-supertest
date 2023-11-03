from unittest.mock import MagicMock, patch

from faker import Faker

from rest_framework_supertest.shortcuts import files
from tests.models import FileModel, ImageModel

from . import ShortcutTestCase


class FilesShortcutsTests(ShortcutTestCase):
    def test_file_extension(self) -> None:
        category = "image"
        self.exec_test(['file_extension'], files, 'file_extension', category=category)

    def test_unique_file_extension(self) -> None:
        category = "image"
        self.exec_test(
            ['unique', 'file_extension'],
            files,
            'unique_file_extension',
            category=category,
        )

    def test_file_name(self) -> None:
        category = "image"
        extension = "jpg"
        self.exec_test(
            ['file_name'],
            files,
            'file_name',
            category=category,
            extension=extension,
        )

    def test_unique_file_name(self) -> None:
        category = "image"
        extension = "jpg"
        self.exec_test(
            ['unique', 'file_name'],
            files,
            'unique_file_name',
            category=category,
            extension=extension,
        )

    def test_mime_type(self) -> None:
        category = "image"
        self.exec_test(['mime_type'], files, 'mime_type', category=category)

    def test_unique_mime_type(self) -> None:
        category = "image"
        self.exec_test(
            ['unique', 'mime_type'],
            files,
            'unique_mime_type',
            category=category,
        )

class ImagesShortcutsTests(ShortcutTestCase):
    def test_image(self) -> None:
        width = 512
        height = 512
        image_format = "jpeg"
        image_name = "any_file.jpg"

        fake, mock = self.get_faker_mock(["image"])
        mock.return_value = b''
        output = files.image(
            fake,
            width=width,
            height=height,
            image_format=image_format,
            file_name=image_name,
        )

        mock.assert_called_once_with(size=(width, height), image_format=image_format)
        self.assertIsNotNone(output)
        self.assertEqual(output.name, image_name)

    @patch('rest_framework_supertest.shortcuts.files.uuid')
    def test_image_without_name(self, mock: MagicMock) -> None:
        file_name = "file_name"
        width = 512
        height = 512
        image_format = "tiff"
        mock.uuid4 = MagicMock()
        mock.uuid4.return_value = file_name
        fake = Faker()
        output = files.image(
            fake,
            width=width,
            height=height,
            image_format=image_format,
        )
        expected_name = f"{file_name}.{image_format}"

        mock.uuid4.assert_called_once()
        self.assertIsNotNone(output)
        self.assertEqual(output.name, expected_name)

    def test_image_store_to_field(self) -> None:
        width = 512
        height = 512
        image_format = "png"
        image_name = "any_file.png"
        fake = Faker()
        image = files.image(
            fake,
            width=width,
            height=height,
            image_format=image_format,
            file_name=image_name,
        )

        model = ImageModel.objects.create(field=image)
        instance = ImageModel.objects.get(pk=model.pk)

        self.assertTrue(bool(instance.field))


class PdfShortcutsTests(ShortcutTestCase):
    def test_pdf(self) -> None:
        file_name = "any_file.pdf"

        fake, mock = self.get_faker_mock(["image"])
        mock.return_value = b''
        output = files.pdf(fake, file_name=file_name)

        mock.assert_called_once_with(
            size=(files.PDF_WIDTH, files.PDF_HEIGHT),
            image_format='pdf',
        )
        self.assertIsNotNone(output)
        self.assertEqual(output.name, file_name)

    @patch('rest_framework_supertest.shortcuts.files.uuid')
    def test_pdf_without_name(self, mock: MagicMock) -> None:
        file_name = "file_name"
        mock.uuid4 = MagicMock()
        mock.uuid4.return_value = file_name
        fake = Faker()
        output = files.pdf(fake)
        expected_name = f"{file_name}.pdf"

        mock.uuid4.assert_called_once()
        self.assertIsNotNone(output)
        self.assertEqual(output.name, expected_name)

    def test_pdf_store_to_field(self) -> None:
        image_name = "any_file.pdf"
        fake = Faker()
        image = files.pdf(fake, file_name=image_name)

        model = FileModel.objects.create(field=image)
        instance = FileModel.objects.get(pk=model.pk)

        self.assertTrue(bool(instance.field))


__all__ = []
