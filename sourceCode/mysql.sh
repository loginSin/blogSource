#!/bin/bash

#帮助管理本地的mysql数据库，提供开启、停止、重启、查看当前状态的功能
#需要输入对应的参数start/stop/restart/status

function mStart(){
	echo "mysql is starting"
	sudo /usr/local/mysql/support-files/mysql.server start
}

function mStop(){
	echo "mysql is stopping"
        sudo /usr/local/mysql/support-files/mysql.server stop
}

function mRestart(){
	echo "mysql is restarting"
	sudo /usr/local/mysql/support-files/mysql.server restart
}

function mStatus(){
	echo "looking mysql's status"
	sudo /usr/local/mysql/support-files/mysql.server status
}

if [ $1 == "start" ]
	then 
	mStart
	elif [ $1 == "stop" ]
	then
	mStop
	elif [ $1 == "restart" ]
	then
	mRestart
	elif [ $1 == "status" ]
	then
	mStatus
	else
	echo "please input start/stop/restart/status"
    echo "eg:./mysql.sh start"
fi
