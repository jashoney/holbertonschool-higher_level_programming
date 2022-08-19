#!/usr/bin/python3
""" a Python script that fetches a url from argv[1]
    then prints the response handling errors"""

if __name__ == "__main__":
    """ our main function """
    from urllib import request, parse, error
    from sys import argv

    url = argv[1]

    try:
        with request.urlopen(url) as response:
            the_page = response.read().decode("utf-8")
        print(the_page)
    except error.HTTPError as e:
        print('Error code: ', e.code)
