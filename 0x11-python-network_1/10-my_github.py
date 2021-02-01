#!/usr/bin/python3
""" 10-my_github

    Takes your Github credentials (username and password)
    and uses the Github API to display your id
"""
import requests
from sys import argv


def main():
    """Takes a url, sendsrequest and display body
    """
    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))
    response_to_json = response.json()
    id_user = response_to_json.get('id')
    if id_user != "None":
        print(id_user)
    else:
        print("None")


if __name__ == "__main__":
    main()
