#!/usr/bin/python3
""" 100-github_commits

    Takes 2 arguments in order to solve this challenge
"""
import requests
from sys import argv


def main():
    """Takes a url, sendsrequest and display body
    """
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/' + \
        owner + '/' + repo + '/commits?per_page=10'
    response = requests.get(url)
    response_data = response.json()
    for i in range(len(response_data)):
        print("{:}: {:}". format(response_data[i]['sha'], response_data[i]
                                 ['commit']['author']['name']))


if __name__ == "__main__":
    main()
