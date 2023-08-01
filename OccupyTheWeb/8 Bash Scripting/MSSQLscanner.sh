#!/bin/bash

# Find systems with Microsoft's SQL Server

echo "IP address: "
read ip

nmap -sT $ip -p 1433 > /dev/null -oG MSSQLscan
cat MSSQLscan | grep open > MSSQLscan2
cat MSSQLscan2
