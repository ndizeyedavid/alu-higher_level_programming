#!/bin/bash
# Sends a GET request and displays the body of a 200 status code response
code=$(curl -sL -o /tmp/body -w "%{http_code}" "$1")
if [ "$code" -eq 200 ]; then
    cat /tmp/body
fi

