#!/usr/bin/python3
"""A module to fetch and display the X-Request-Id header
from a URL response.
"""

import urllib.request
import sys


def fetch_header(url):
    """Fetches the X-Request-Id header from a given URL.

    Sends a GET request to the URL using urllib, follows
    redirects, and prints
    the value of the X-Request-Id header if present.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    with urllib.request.urlopen(url) as response:
        header_value = response.getheader('X-Request-Id')
        if header_value is not None:
            print(header_value)


if __name__ == "__main__":
    fetch_header(sys.argv[1])
