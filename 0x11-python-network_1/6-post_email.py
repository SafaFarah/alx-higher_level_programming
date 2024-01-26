#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request to
    the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
import requests
import sys

if __name__ == "__main__":
    value = {"email": argv[2]}
    response = requests.post(sys.argv[1], data=value)
    print(response.text)
