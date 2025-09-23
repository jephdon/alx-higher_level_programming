#!/usr/bin/python3
"""A module to fetch and display the X-Request-Id header
from a URL response.
"""

import urllib.request
import sys


def fetch_header(url):
    """Fetches the X-Request-Id header from a given URL.

    Sends a request to the provided URL using urllib, follows redirects,
    and prints the value of the X-Request-Id header in the response.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    # Create an opener to handle redirects
    opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler)
    request = urllib.request.Request(url)
    with opener.open(request) as response:
        header_value = response.getheader('X-Request-Id')
        print(header_value)


if __name__ == "__main__":
    fetch_header(sys.argv[1])
