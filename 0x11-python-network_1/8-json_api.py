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
    q = ""
    if len(argv) > 1:
        q = argv[1]
    request = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json = request.json()
        if j:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')


if __name__ == "__main__":
    main()
