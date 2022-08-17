#!/bin/bash
# script that takes in an argument URL, sends a GET request to the URL header

curl "$1" -sX GET -H "X-HolbertonSchool-User-Id: 98"
