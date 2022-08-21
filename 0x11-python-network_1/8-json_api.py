#!/usr/bin/python3
""" a Python cript that takes in a URL and a letter
    sends a POST request to the given url,
    and finally displays the body of the response. """

if __name__ == "__main__":
    """ our main function """
    from requests import post
    from sys import exit, argv

    url = 'http://0.0.0.0:5000/search_user'
    letter = {"q": ""}

    if len(argv) > 1:
        letter['q'] = argv[1]

    response = post(url, data=letter)
    if not response.ok or len(response.text) <= 0:
        print('No result')
        exit()
    else:
        try:
            jsonresponse = response.json()
            id = jsonresponse.get('id')
            name = jsonresponse.get('name')
        except ValueError:
            print('Not a valid JSON')
            exit()
        if len(jsonresponse) == 0:
            print('No result')
            exit()
        print("[{}] {}".format(id, name))
