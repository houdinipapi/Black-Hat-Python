#!/bin/bash

# Find systems with Microsoft's SQL Server

echo "Starting IP address: "
read StartIP

echo "Last octet: "
read LastIP

echo "Port: "
read port

nmap -sT $StartIP-$LastIP -p $port > /dev/null -oG MSSQLscan
cat MSSQLscan | grep open > MSSQLscan2
cat MSSQLscan2
