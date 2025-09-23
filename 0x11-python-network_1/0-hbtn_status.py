#!/usr/bin/python3
"""A module to fetch and display the status from a URL using urllib."""

import urllib.request


def fetch_status():
    """Fetches the status from https://alx-intranet.hbtn.io/status.

    Displays the response body type, content, and UTF-8 decoded content
    using urllib and a with statement.

    Returns:
        None
    """
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")


if __name__ == "__main__":
    fetch_status()
