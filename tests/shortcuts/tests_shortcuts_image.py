from faker import Faker

from rest_framework_supertest.shortcuts import images
from tests.models import ImageModel

from . import ShortcutTestCase


class ImagesShortcutsTests(ShortcutTestCase):
    def test_image(self) -> None:
        width = 512
        height = 512
        image_format = "jpeg"
        image_name = "any_file.jpg"

        fake, mock = self.get_faker_mock(["image"])
        mock.return_value = b''
        output = images.image(
            fake,
            width=width,
            height=height,
            image_format=image_format,
            file_name=image_name,
        )

        mock.assert_called_once_with(size=(width, height), image_format=image_format)
        self.assertIsNotNone(output)
        self.assertEqual(output.name, image_name)

    def test_image_store_to_field(self) -> None:
        width = 512
        height = 512
        image_format = "png"
        image_name = "any_file.png"
        fake = Faker()
        image = images.image(
            fake,
            width=width,
            height=height,
            image_format=image_format,
            file_name=image_name,
        )

        model = ImageModel.objects.create(field=image)
        instance = ImageModel.objects.get(pk=model.pk)

        self.assertTrue(bool(instance.field))


__all__ = []
