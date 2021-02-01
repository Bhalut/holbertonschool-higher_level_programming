#!/usr/bin/python3
""" 6-post_email

    Takes in a URL and an email address,
    sends a POST request to the passed URL with the email as a parameter,
    and finally displays the body of the response.
"""
import requests
from sys import argv


def main():
    """Takes a url and email, sends POST request and display body
    """
    post_url = argv[1]
    payload = {
        'email': argv[2]
    }
    req = requests.post(post_url, data=payload)
    print(req.text)


if __name__ == "__main__":
    main()
