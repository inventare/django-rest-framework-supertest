from .automotives import license_plate, unique_license_plate, vin, unique_vin
from .persons import (
    first_name, unique_first_name,
    first_name_female, unique_first_name_female,
    first_name_male, unique_first_name_male,
    first_name_nonbinary, unique_first_name_nonbinary,
    language_name,
    last_name, unique_last_name,
    last_name_female, unique_last_name_female,
    last_name_male, unique_last_name_male,
    last_name_nonbinary, unique_last_name_nonbinary,
    name, unique_name,
    name_female, unique_name_female,
    name_male, unique_name_male,
    name_nonbinary, unique_name_nonbinary,
    prefix, prefix_female, prefix_male, prefix_nonbinary,
    suffix, suffix_female, suffix_male, suffix_nonbinary,
)
from .internet import (
    domain_name, unique_domain_name, domain_word, unique_domain_word, tld,
    ipv4, unique_ipv4, ipv4_network_class, ipv4_private, unique_ipv4_private, ipv4_public,
    unique_ipv4_public, ipv6, unique_ipv6, mac_address, unique_mac_address,
    http_method, hostname, unique_hostname, email, unique_email, image_url, slug,
    uri, uri_extension, uri_page, uri_path, url, user_name
)
from .lorem import *
from .isbn import *
from .jobs import *
from .emojis import *
from .credit_cards import *
from .addresses import *
from .phone_numbers import *
from .currencies import *
from .geographicals import *
from .files import *
from .misc import *
from .colors import *
from .dates import *

__all__ = [
    # automotives
    'license_plate', 'unique_license_plate', 'vin', 'unique_vin',
    # persons
    'first_name', 'unique_first_name', 'first_name_female', 'unique_first_name_female',
    'first_name_male', 'unique_first_name_male', 'first_name_nonbinary', 'unique_first_name_nonbinary',
    'language_name', 'last_name', 'unique_last_name', 'last_name_female', 'unique_last_name_female',
    'last_name_male', 'unique_last_name_male', 'last_name_nonbinary', 'unique_last_name_nonbinary',
    'name', 'unique_name', 'name_female', 'unique_name_female', 'name_male', 'unique_name_male',
    'name_nonbinary', 'unique_name_nonbinary', 'prefix', 'prefix_female', 'prefix_male', 'prefix_nonbinary',
    'suffix', 'suffix_female', 'suffix_male', 'suffix_nonbinary',
    # internet
    'domain_name', 'unique_domain_name', 'domain_word', 'unique_domain_word', 'tld',
    'ipv4', 'unique_ipv4', 'ipv4_network_class', 'ipv4_private', 'unique_ipv4_private', 'ipv4_public',
    'unique_ipv4_public', 'ipv6', 'unique_ipv6', 'mac_address', 'unique_mac_address',
    'http_method', 'hostname', 'unique_hostname', 'email', 'unique_email', 'image_url', 'slug',
    'uri', 'uri_extension', 'uri_page', 'uri_path', 'url', 'user_name',
]
