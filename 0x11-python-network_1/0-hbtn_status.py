#!/usr/bin/python3
""" a Python script that fetches https://intranet.hbtn.io/status """


if __name__ == "__main__":

    from urllib import request

    url = "https://intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        the_page = response.read()
    print("Body response:")
    print(f"    - type: {type(the_page)}")
    print(f"    - content: {the_page}")
    print(f"    - utf8 content: {the_page.decode('utf-8')}")
