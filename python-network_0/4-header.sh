#!/bin/bash
# Sends a GET request with a header and displays the body
curl -s -H "X-HolbertonSchool-User-Id: 98" -H "X-School-User-Id: 98" "$1"
