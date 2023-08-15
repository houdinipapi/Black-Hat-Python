#!/bin/bash

# Resolving Port Conflict

sudo fuser -k 8000/tcp
sudo fuser -k 5000/tcp
