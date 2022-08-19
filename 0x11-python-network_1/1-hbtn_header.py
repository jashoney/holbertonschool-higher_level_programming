#!/usr/bin/python3
""" a Python script that fetches a url from argv[1] """
""" then gets the value of the header_key and prints it """

if __name__ == "__main__":
    """ our main function """
    from urllib import request
    from sys import argv

    url = argv[1]
    header_key = "X-Request-Id"

    with request.urlopen(url) as response:
        info = response.info().get(header_key)
    print(info)
