#!/usr/bin/python3
""" a Python script that fetches a url status"""

if __name__ == "__main__":
    """ our main function """
    import requests
    from sys import argv

    url = argv[1]

    the_page = requests.get(url)
    page_header = the_page.headers
    xheader = page_header.get('X-Request-Id')
    print(xheader)
