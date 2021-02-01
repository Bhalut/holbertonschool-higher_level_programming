#!/usr/bin/python3
""" 3-error_code

    Sends a request to the URL
    and displays the body of the response (decoded in utf-8).
"""
from urllib import request
from urllib.error import HTTPError
from sys import argv


def main():
    """Takes a url, sendsrequest and display body
    """
    url_request = argv[1]
    req = request.Request(url_request)
    try:
        with request.urlopen(req) as resp:
            html = resp.read()
            print(html.decode("UTF-8"))
    except HTTPError as e:
        print("Error code: {:}".format(e.code))


if __name__ == "__main__":
    main()
