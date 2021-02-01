#!/usr/bin/python3
""" 8-json_api

    Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""
import requests
from sys import argv


def main():
    """Takes a url, sendsrequest and display body
    """
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    post_url = "http://0.0.0.0:5000/search_user"
    payload = {
        'q': q
    }
    req = requests.post(post_url, data=payload)
    try:
        json_content = req.json()
        if len(json_content) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json_content['id'], json_content['name']))
    except:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
