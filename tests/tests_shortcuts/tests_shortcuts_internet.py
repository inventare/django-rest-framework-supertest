from rest_framework_supertest.shortcuts import internet

from . import ShortcutTestCase


class InternetShortcutsTests(ShortcutTestCase):
    def test_email(self) -> None:
        safe = False
        domain = 'any.com'
        self.exec_test(['email'], internet, 'email', safe=safe, domain=domain)

    def test_unique_email(self) -> None:
        safe = False
        domain = 'any.com'
        self.exec_test(
            ['unique', 'email'],
            internet,
            'unique_email',
            safe=safe,
            domain=domain,
        )

    def test_domain_name(self) -> None:
        levels = 2
        self.exec_test(['domain_name'], internet, 'domain_name', levels=levels)

    def test_unique_domain_name(self) -> None:
        levels = 2
        self.exec_test(
            ['unique', 'domain_name'],
            internet,
            'unique_domain_name',
            levels=levels,
        )

    def test_domain_word(self) -> None:
        self.exec_test(['domain_word'], internet, 'domain_word')

    def test_unique_domain_word(self) -> None:
        self.exec_test(['unique', 'domain_word'], internet, 'unique_domain_word')

    def test_hostname(self) -> None:
        levels = 2
        self.exec_test(['hostname'], internet, 'hostname', levels=levels)

    def test_unique_hostname(self) -> None:
        levels = 2
        self.exec_test(
            ['unique', 'hostname'],
            internet,
            'unique_hostname',
            levels=levels,
        )

    def test_http_method(self) -> None:
        self.exec_test(['http_method'], internet, 'http_method')

    def test_image_url(self) -> None:
        width = 400
        height = 4000
        placeholder_url = 'a.com'
        self.exec_test(
            ['image_url'],
            internet,
            'image_url',
            width=width,
            height=height,
            placeholder_url=placeholder_url,
        )

    def test_ipv4(self) -> None:
        network = False
        address_class = 'c'
        private = True
        self.exec_test(
            ['ipv4'],
            internet,
            'ipv4',
            network=network,
            address_class=address_class,
            private=private,
        )

    def test_unique_ipv4(self) -> None:
        network = False
        address_class = 'c'
        private = True
        self.exec_test(
            ['unique', 'ipv4'],
            internet,
            'unique_ipv4',
            network=network,
            address_class=address_class,
            private=private,
        )

    def test_ipv4_network_class(self) -> None:
        self.exec_test(['ipv4_network_class'], internet, 'ipv4_network_class')

    def test_ipv4_private(self) -> None:
        network = False
        address_class = 'a'
        self.exec_test(
            ['ipv4_private'],
            internet,
            'ipv4_private',
            network=network,
            address_class=address_class,
        )

    def test_unique_ipv4_private(self) -> None:
        network = False
        address_class = 'a'
        self.exec_test(
            ['unique', 'ipv4_private'],
            internet,
            'unique_ipv4_private',
            network=network,
            address_class=address_class,
        )

    def test_ipv4_public(self) -> None:
        network = False
        address_class = 'a'
        self.exec_test(
            ['ipv4_public'],
            internet,
            'ipv4_public',
            network=network,
            address_class=address_class,
        )

    def test_unique_ipv4_public(self) -> None:
        network = False
        address_class = 'a'
        self.exec_test(
            ['unique', 'ipv4_public'],
            internet,
            'unique_ipv4_public',
            network=network,
            address_class=address_class,
        )

    def test_ipv6(self) -> None:
        network = False
        self.exec_test(['ipv6'], internet, 'ipv6', network=network)

    def test_unique_ipv6(self) -> None:
        network = False
        self.exec_test(['unique', 'ipv6'], internet, 'unique_ipv6', network=network)

    def test_mac_address(self) -> None:
        self.exec_test(['mac_address'], internet, 'mac_address')

    def test_unique_mac_address(self) -> None:
        self.exec_test(['unique', 'mac_address'], internet, 'unique_mac_address')

    def test_slud(self) -> None:
        value = 'any value here'
        self.exec_test(['slug'], internet, 'slug', value=value)

    def test_tld(self) -> None:
        self.exec_test(['tld'], internet, 'tld')

    def test_uri(self) -> None:
        self.exec_test(['uri'], internet, 'uri')

    def test_uri_extension(self) -> None:
        self.exec_test(['uri_extension'], internet, 'uri_extension')

    def test_uri_page(self) -> None:
        self.exec_test(['uri_page'], internet, 'uri_page')

    def test_uri_path(self) -> None:
        deep = 3
        self.exec_test(['uri_path'], internet, 'uri_path', deep=deep)

    def test_url(self) -> None:
        schemes = {}
        self.exec_test(['url'], internet, 'url', schemes=schemes)

    def test_user_name(self) -> None:
        self.exec_test(['user_name'], internet, 'user_name')

__all__ = []
