#!/usr/bin/python3
"""
uses GitHub credentials (username and password) to display your id
"""

from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    response = requests.get('https://api.github.com/user',
                            auth=HTTPBasicAuth(username, password))
    print(response.json().get('id'))
