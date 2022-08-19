#!/usr/bin/python3
""" a Python cript that takes in a URL and an email address,
    sends a POST request to the passed URL with the email as a parameter,
    and finally displays the body of the response. """

if __name__ == "__main__":
    """ our main function """
    import requests
    from sys import argv

    url = argv[1]
    email = {"email": argv[2]}

    the_page = requests.post(url, data=email)
    print(the_page.text)
