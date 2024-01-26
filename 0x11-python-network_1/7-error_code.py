#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions and print: Error code:
 followed by the HTTP status code
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    code = response.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(response.text)
