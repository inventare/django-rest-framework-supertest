from rest_framework_supertest.shortcuts import images

from . import ShortcutTestCase


class ImagesShortcutsTests(ShortcutTestCase):
    def test_image(self) -> None:
        width = 512
        height = 512
        image_format = "jpeg"
        image_name = "any_file.jpg"

        fake, mock = self.get_faker_mock(["image"])
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


__all__ = []
