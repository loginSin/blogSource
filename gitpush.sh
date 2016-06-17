#!/bin/bash

if [ ! -n "$1" ]
	then
	echo "you have to input something"
else
	git add .
	git commit -m "$1"
	git push
fi
