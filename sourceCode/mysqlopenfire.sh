#!/bin/bash

#主要是为了启动mysql里面的openfire数据库，方便对里面的表进行操作

echo "input the database-openfire password"

/usr/local/mysql/bin/mysql -u root -p openfire
