#!/usr/bin/python3
""" a Python script that fetches a url status"""

if __name__ == "__main__":
    """ our main function """
    import requests

    url = "https://intranet.hbtn.io/status"

    the_page = requests.get(url)
    the_page = the_page.text
    print("Body response:")
    print("    type: {}".format(type(the_page)))
    print("    content: {}".format(the_page))
