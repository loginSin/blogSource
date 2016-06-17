#!/bin/bash

#使用方式：放入./git所在文件夹，执行脚本比如
#$./gitpush.sh "init"
#参数是必须的，这一点尤其需要注意

if [ ! -n "$1" ]
	then
	echo "you have to input something"
else
	git add .
	git commit -m "$1"
	git push
fi
