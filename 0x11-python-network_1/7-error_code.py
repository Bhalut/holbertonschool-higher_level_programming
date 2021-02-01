#!/usr/bin/python3
""" 7-error_code

    Takes in a URL, sends a request to the URL
    and displays the body of the response.
"""
import requests
from sys import argv


def main():
    """Takes a url, sendsrequest and display body
    """
    url_req = argv[1]
    req = requests.get(url_req)
    if req.status_code >= 400:
        print("Error code: {:}".format(req.status_code))
    else:
        print(req.text)


if __name__ == "__main__":
    main()
