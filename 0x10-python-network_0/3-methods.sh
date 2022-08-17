#!/bin/bash
# script that takes in an URL and displays the accepted methods

curl -sIX OPTIONS "$1" | grep "Allow:" | cut -c8-
