#!/bin/bash
# Displays the size of the body of a response in bytes
curl -s "$1" | wc -c | xargs
