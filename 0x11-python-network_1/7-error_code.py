#!/usr/bin/python3
""" a Python script that fetches a url from argv[1]
    then prints the response handling errors"""

if __name__ == "__main__":
    """ our main function """
    import requests
    from sys import argv

    url = argv[1]

    the_page = requests.get(url)
    if the_page.status_code >= 400:
        print('Error code: {}'.format(the_page.status_code))
    else:
        print(the_page.text)
