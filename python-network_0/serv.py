#!/bin/bash
kill -9 `cat web.pid` > /dev/null 2>&1;
sleep 2;

python3 "$1" > /dev/null 2>&1 &
echo $! > web.pid

sleep 5;
