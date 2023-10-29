from rest_framework_supertest.shortcuts import colors

from . import ShortcutTestCase


class ColorsShortcutsTests(ShortcutTestCase):
    def test_color(self) -> None:
        hue = 180
        luminosity = 'dark'
        color_format = 'rgb'
        self.exec_test(
            ['color'],
            colors,
            'color',
            hue=hue,
            luminosity=luminosity,
            color_format=color_format,
        )

    def test_unique_color(self) -> None:
        hue = 180
        luminosity = 'dark'
        color_format = 'rgb'
        self.exec_test(
            ['unique', 'color'],
            colors,
            'unique_color',
            hue=hue,
            luminosity=luminosity,
            color_format=color_format,
        )

    def test_color_name(self) -> None:
        self.exec_test(['color_name'], colors, 'color_name')

    def test_unique_color_name(self) -> None:
        self.exec_test(['unique', 'color_name'], colors, 'unique_color_name')

    def test_hex_color(self) -> None:
        self.exec_test(['hex_color'], colors, 'hex_color')

    def test_unique_hex_color(self) -> None:
        self.exec_test(['unique', 'hex_color'], colors, 'unique_hex_color')

    def test_rgb_color(self) -> None:
        self.exec_test(['rgb_color'], colors, 'rgb_color')

    def test_unique_rgb_color(self) -> None:
        self.exec_test(['unique', 'rgb_color'], colors, 'unique_rgb_color')

    def test_rgb_css_color(self) -> None:
        self.exec_test(['rgb_css_color'], colors, 'rgb_css_color')

    def test_unique_rgb_css_color(self) -> None:
        self.exec_test(['unique', 'rgb_css_color'], colors, 'unique_rgb_css_color')

    def test_safe_color_name(self) -> None:
        self.exec_test(['safe_color_name'], colors, 'safe_color_name')

    def test_unique_safe_color_name(self) -> None:
        self.exec_test(['unique', 'safe_color_name'], colors, 'unique_safe_color_name')

    def test_safe_hex_color(self) -> None:
        self.exec_test(['safe_hex_color'], colors, 'safe_hex_color')

    def test_unique_safe_hex_color(self) -> None:
        self.exec_test(['unique', 'safe_hex_color'], colors, 'unique_safe_hex_color')

__all__ = []
