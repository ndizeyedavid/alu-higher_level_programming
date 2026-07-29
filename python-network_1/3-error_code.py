#!/usr/bin/python3
"""Sends a request and handles HTTP errors using urllib."""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
