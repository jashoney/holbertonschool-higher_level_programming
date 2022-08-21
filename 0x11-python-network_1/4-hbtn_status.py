#!/usr/bin/python3
""" a Python script that fetches a url status"""

if __name__ == "__main__":
    """ our main function """
    from requests import get

    url = "https://intranet.hbtn.io/status"

    the_page = get(url)
    the_page = the_page.text
    print("Body response:")
    print("\t- type: {}".format(type(the_page)))
    print("\t- content: {}".format(the_page))
