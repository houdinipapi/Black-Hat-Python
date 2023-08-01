#!/bin/bash

# This script is designed to find hosts with MySQL installed

echo "IP address: "
read ip

nmap -sT $ip/24 -p 3306 > devnull -oG MySQLscan
cat MySQLscan | grep open > MySQLscan2
cat MySQLscan2
