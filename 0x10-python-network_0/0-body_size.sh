#!/bin/bash
# This script receives a URL and returns the size of the body in the response
curl -sI "$1" | grep "Length" | cut -d" " -f2
