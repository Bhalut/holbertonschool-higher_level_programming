#!/usr/bin/python3
""" 1-hbtn_header

    Sends a request to the URL and displays
    the value of the X-Request-Id variable
    found in the header of the response
"""
from urllib import request
from sys import argv


def main():
    """Takes a url, send request and display value
    """
    url_request = argv[1]
    with request.urlopen(url_request) as response:
        html = response.read()
        print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
