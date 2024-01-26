#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request


if __name__ == "__main__":
    url = "https: //alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as r:
        response = r.read()
        print('Body response:')
        print('\t- type: {}'.format(type(response)))
        print('\t- content: {}'.format(response))
        print('\t- utf8 content: {}'.format(response.decode("utf-8")))
