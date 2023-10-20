from ._utils import unique

def email(fake, safe=True, domain=None):
    """Generates a e-mail"""
    return fake.email(safe=safe, domain=domain)

def unique_email(fake, safe=True, domain=None):
    """Generates a unique e-mail"""
    return unique(fake, email, safe=safe, domain=domain)

def domain_name(fake, levels=1):
    """Generates a domain name"""
    return fake.domain_name(levels=levels)

def unique_domain_name(fake):
    """Generates a unique domain name"""
    return unique(fake, domain_name)

def domain_word(fake):
    """Generates a domain word"""
    return fake.domain_word()

def unique_domain_word(fake):
    """Generates a unique domain word"""
    return unique(fake, domain_word)

def hostname(fake, levels=1):
    """Generates a hostname"""
    return fake.hostname(levels=levels)

def unique_hostname(fake, levels=1):
    """Generates a unique hostname"""
    return unique(fake, hostname, levels=levels)

def http_method(fake):
    """Generates a random http method"""
    return fake.http_method()

def image_url(fake, width=None, height=None, placeholder_url=None):
    """Generates a image url"""
    return fake.image_url(width=width, height=height, placeholder_url=placeholder_url)

def ipv4(fake, network=False, address_class=None, private=None):
    """
    Generates a random IPv4 address or network with a valid CIDR.

    Args:
        network: Network address
        address_class: IPv4 address class (a, b, or c)
        private: Public or private
    
    Returns:
        IPv4
    """
    return fake.ipv4(network=network, address_class=address_class, private=private)

def unique_ipv4(fake, network=False, address_class=None, private=None):
    """
    Generates a unique random IPv4 address or network with a valid CIDR.

    Args:
        network: Network address
        address_class: IPv4 address class (a, b, or c)
        private: Public or private
    
    Returns:
        IPv4
    """
    return unique(fake, ipv4, network=network, address_class=address_class, private=private)

def ipv4_network_class(fake):
    """
    Generates a IPv4 network class "a", "b" or "c".

    Returns:
        IPv4 network class
    """
    return fake.ipv4_network_class()

def ipv4_private(fake, network=False, address_class=None):
    """
    Generates a private IPv4.

    Args:
        network: Network address
        address_class: IPv4 address class (a, b, or c)

    Returns:
        Private IPv4
    """
    return fake.ipv4_private(network=network, address_class=address_class)

def unique_ipv4_private(fake, network=False, address_class=None):
    """
    Generates a unique private IPv4.

    Args:
        network: Network address
        address_class: IPv4 address class (a, b, or c)

    Returns:
        private IPv4
    """
    return unique(fake, ipv4_private, network=network, address_class=address_class)

def ipv4_public(fake, network=False, address_class=None):
    """
    Generates a public IPv4 excluding private blocks.

    Args:
        network: Network address
        address_class: IPv4 address class (a, b, or c)

    Returns:
        public IPv4
    """
    return fake.ipv4_public(network=network, address_class=address_class)

def unique_ipv4_public(fake, network=False, address_class=None):
    """
    Generates a unique public IPv4 excluding private blocks.

    Args:
        network: Network address
        address_class: IPv4 address class (a, b, or c)

    Returns:
        public IPv4
    """
    return unique(fake, ipv4_public, network=network, address_class=address_class)

def ipv6(fake, network=False):
    """
    Generates a random IPv6 address or network with a valid CIDR

    Args:
        network: Network address

    Returns:
        IPv6
    """
    return fake.ipv6(network=network)

def unique_ipv6(fake, network=False):
    """
    Generates a unique IPv6 address or network with a valid CIDR

    Args:
        network: Network address

    Returns:
        IPv6
    """
    return unique(fake, ipv6, network=network)

def mac_address(fake):
    """
    Generates a MAC Address

    Returns:
        a MAC Address
    """
    return fake.mac_address()

def unique_mac_address(fake):
    """
    Generates a unique MAC Address

    Returns:
        a MAC Address
    """
    return unique(fake, mac_address)

def slug(fake, value=None):
    """Generates a slug"""
    return fake.slug(value=value)

def tld(fake):
    """Generates a top level domain"""
    return fake.tld()

def uri(fake):
    """Generates a URI"""
    return fake.uri()

def uri_extension(fake):
    """Generates a URI extension"""
    return fake.uri_extension()

def uri_page(fake):
    """Generates a URI page"""
    return fake.uri_page()

def uri_path(fake, deep=None):
    """Generates a URI path"""
    return fake.uri_path(deep=deep)

def url(fake, schemes = None):
    """Generates a url"""
    return fake.url(schemes=schemes)

def user_name(fake):
    """Generates a user name"""
    return fake.user_name()
