#!/usr/bin/python3
""" a Python script that fetches a url from argv[1]
    and an email as argv[2], requests,
    then prints the response """

if __name__ == "__main__":
    """ our main function """
    from urllib import request, parse
    from sys import argv

    url = argv[1]
    email = argv[2]
    data = parse.urlencode({"email": email})
    data = data.encode("ascii")

    with request.urlopen(url, data) as response:
        the_page = response.read().decode("utf-8")
    print(the_page)
