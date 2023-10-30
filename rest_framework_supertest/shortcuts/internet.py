from typing import List, Optional

from ._utils import unique


def email(fake: object, *, domain: Optional[str] = None, safe: bool = True) -> str:
    """
    Generate a e-mail.

    Args:
        fake: The `Faker` instance.
        domain: optional domain of the e-mail (e.g: '@gmail.com'). If none
          is determinated, we have two options based on `safe` argument
          (see the `safe` argument bellow).

        safe: if `safe=True`, then an safe domain name is used
          (one of `example.org`, `example.com`, `example.net`). If
          `safe=False`, an random domain name is used.
    """
    return fake.email(safe=safe, domain=domain)

def unique_email(
    fake: object,
    *,
    domain: Optional[str] = None,
    safe: bool = True,
) -> str:
    """
    Generate a unique e-mail.

    Args:
        fake: The `Faker` instance.
        domain: optional domain of the e-mail (e.g: '@gmail.com'). If none
          is determinated, we have two options based on `safe` argument
          (see the `safe` argument bellow).

        safe: if `safe=True`, then an safe domain name is used
          (one of `example.org`, `example.com`, `example.net`). If
          `safe=False`, an random domain name is used.
    """
    return unique(fake, email, safe=safe, domain=domain)

def domain_name(fake: object, levels: int = 1) -> str:
    """Generate a domain name."""
    return fake.domain_name(levels=levels)

def unique_domain_name(fake: object, levels: int = 1) -> str:
    """Generate a unique domain name."""
    return unique(fake, domain_name, levels=levels)

def domain_word(fake: object) -> str:
    """Generate a domain word."""
    return fake.domain_word()

def unique_domain_word(fake: object) -> str:
    """Generate a unique domain word."""
    return unique(fake, domain_word)

def hostname(fake: object, levels: int = 1) -> str:
    """Generate a hostname."""
    return fake.hostname(levels=levels)

def unique_hostname(fake: object, levels: int = 1) -> str:
    """Generate a unique hostname."""
    return unique(fake, hostname, levels=levels)

def http_method(fake: object) -> str:
    """Generate a random http method."""
    return fake.http_method()

def image_url(
    fake: object,
    width: Optional[int] = None,
    height: Optional[int] = None,
    placeholder_url: Optional[str] = None,
) -> str:
    """Generate a image url."""
    return fake.image_url(width=width, height=height, placeholder_url=placeholder_url)

def ipv4(
    fake: object,
    *,
    network: bool = False,
    address_class: Optional[str] = None,
    private: Optional[bool] = None,
) -> str:
    """
    Generate a random IPv4 address or network with a valid CIDR.

    Args:
        fake: The `Faker` instance.
        network: indicate if is a address or network.
        address_class: IPv4 address class (a, b, or c)
        private: indicates if is public or private
    """
    return fake.ipv4(network=network, address_class=address_class, private=private)

def unique_ipv4(
    fake: object,
    *,
    network: bool = False,
    address_class: Optional[str] = None,
    private: Optional[bool] = None,
) -> str:
    """
    Generate a unique IPv4 address or network with a valid CIDR.

    Args:
        fake: The `Faker` instance.
        network: indicate if is a address or network.
        address_class: IPv4 address class (a, b, or c)
        private: indicates if is public or private
    """
    return unique(
        fake,
        ipv4,
        network=network,
        address_class=address_class,
        private=private,
    )

def ipv4_network_class(fake: object) -> str:
    """Generate a IPv4 network class "a", "b" or "c"."""
    return fake.ipv4_network_class()

def ipv4_private(
    fake: object,
    *,
    network: bool = False,
    address_class: Optional[str] = None,
) -> str:
    """
    Generate a private IPv4.

    Args:
        fake: The `Faker` instance.
        network: indicate if is a address or network.
        address_class: IPv4 address class (a, b, or c)
    """
    return fake.ipv4_private(network=network, address_class=address_class)

def unique_ipv4_private(
    fake: object,
    *,
    network: bool = False,
    address_class: Optional[str] = None,
) -> str:
    """
    Generate a unique private IPv4.

    Args:
        fake: The `Faker` instance.
        network: indicate if is a address or network.
        address_class: IPv4 address class (a, b, or c).
    """
    return unique(fake, ipv4_private, network=network, address_class=address_class)

def ipv4_public(
    fake: object,
    *,
    network: bool = False,
    address_class: Optional[str] = None,
) -> str:
    """
    Generate a public IPv4 excluding private blocks.

    Args:
        fake: The `Faker` instance.
        network: indicate if is a andress or network.
        address_class: IPv4 address class (a, b, or c).
    """
    return fake.ipv4_public(network=network, address_class=address_class)

def unique_ipv4_public(
    fake: object,
    *,
    network: bool = False,
    address_class: Optional[str] = None,
) -> str:
    """
    Generate a unique public IPv4 excluding private blocks.

    Args:
        fake: The `Faker` instance.
        network: indicate if is a andress or network.
        address_class: IPv4 address class (a, b, or c).
    """
    return unique(fake, ipv4_public, network=network, address_class=address_class)

def ipv6(fake: object, *, network: bool = False) -> str:
    """Generate a random IPv6 address or network with a valid CIDR."""
    return fake.ipv6(network=network)

def unique_ipv6(fake: object, *, network: bool = False) -> str:
    """Generate a unique IPv6 address or network with a valid CIDR."""
    return unique(fake, ipv6, network=network)

def mac_address(fake: object) -> str:
    """Generate a MAC Address."""
    return fake.mac_address()

def unique_mac_address(fake: object) -> str:
    """Generate a unique MAC Address."""
    return unique(fake, mac_address)

def slug(fake: object, value: Optional[str] = None) -> str:
    """
    Generate a slug using the django algorithm.

    Args:
        fake: The `Faker` instance.
        value: If the value is not None, the slug is generated
          from the value. Otherwise, an random text with length=20 is used.
    """
    return fake.slug(value=value)

def tld(fake: object) -> str:
    """Generate a top level domain."""
    return fake.tld()

def uri(fake: object) -> str:
    """Generate a URI."""
    return fake.uri()

def uri_extension(fake: object) -> str:
    """Generate a URI extension."""
    return fake.uri_extension()

def uri_page(fake: object) -> str:
    """Generate a URI page."""
    return fake.uri_page()

def uri_path(fake: object, deep: Optional[int] = None) -> str:
    """Generate a URI path."""
    return fake.uri_path(deep=deep)

def url(fake: object, schemes: Optional[List[str]] = None) -> str:
    """
    Generate a url.

    Args:
        fake: The `Faker` instance.
        schemes: a list of strings to use as schemes, one will
          chosen randomly. If None, it will set to `['http', 'https']`.
          Passing an empty list will result in schemeless url
          generation like “://domain.com”.
    """
    return fake.url(schemes=schemes)

def user_name(fake: object) -> str:
    """Generate a user name."""
    return fake.user_name()
