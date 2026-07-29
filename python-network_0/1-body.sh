#!/bin/bash
# Sends a GET request and displays the body of a 200 status code response
code=$(curl -sL -o /dev/null -w "%{http_code}" "$1"); [ "$code" -eq 200 ] && curl -sL "$1"
