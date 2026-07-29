#!/bin/bash
# Sends a POST request with email and subject parameters and displays the body
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
