#!/bin/bash

# This script is designed to find hosts with MySQL installed

echo "Starting IP address: "
read FirstIp

echo "Enter the last octet of the last IP address: "
read LastOctetIp

echo "Port number: "
read port

nmap -sT $FirstIp-$LastOctetIp -p $port > /dev/null -oG MySQLscan
cat MySQLscan | grep open > MySQLscan2
cat MySQLscan2
