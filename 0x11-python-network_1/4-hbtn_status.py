#!/usr/bin/python3
""" 4-hbtn_status

    Fetches https://intranet.hbtn.io/status
"""
import requests


def main():
    """Takes a url, sends request and display body
    """
    url_req = "https://intranet.hbtn.io/status"
    req = requests.get(url_req)
    print("Body response:")
    print("\t- type: {:}".format(type(req.text)))
    print("\t- content: {:}".format(req.text))


if __name__ == "__main__":
    main()
