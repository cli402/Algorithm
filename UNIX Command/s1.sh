#!/bin/bash
clear
echo "The start of the script"
echo "Hi, $USER"

# if [ ! $# == 1 ] ;then
# 	echo "The number of the argument should be one"
# 	exit 
# fi

# if [ "$1" == fish ] ;then
# 	echo "Fish "
# else
# 	echo "Please insert fish"
# fi

filename="$1"

if [ -f filename ]; then
	echo "Size of the file is $(ls -lh $filename | awk '{print $5}')"
else
	echo "The file did not exist"
fi



