#!/bin/bash

# Upload project to target host
path_to_pem=$1
username=$2
host=$3

scp -i $path_to_pem dist/eduworld.tar.gz $username@$host:/home/$username/eduworld