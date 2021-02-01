#!/usr/bin/python3
""" 2-post_email

    Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""
from urllib import request
from urllib import parse
from sys import argv


def main():
    """Takes a url and email, sends POST request and display body
    """
    post_url = argv[1]
    params = {
        'email': argv[2]
    }
    query_string = parse.urlencode(params)
    post_data = query_string.encode("ascii")
    with request.urlopen(post_url, post_data) as post_response:
        response_text = post_response.read()
        print(response_text.decode("UTF-8"))


if __name__ == "__main__":
    main()
