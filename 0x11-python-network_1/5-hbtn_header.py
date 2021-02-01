#!/usr/bin/python3
""" 5-hbtn_header

    Sends a request to the URL
    and displays the value of the variable X-Request-Id in the response header
"""
import requests
from sys import argv


def main():
    """Takes a url, send request and display value
    """
    url_req = argv[1]
    req = requests.get(url_req)
    req.text
    print(req.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
