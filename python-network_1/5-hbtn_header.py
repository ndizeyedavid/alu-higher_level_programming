#!/usr/bin/python3
"""Displays the X-Request-Id header from a URL response using requests."""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
