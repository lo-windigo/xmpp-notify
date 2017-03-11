#!/usr/bin/env bash

#########################
# Check for permissions
#########################
if [ "$USER" != "root" ]; then
	echo "This script installs system dependencies, and requires root"
	exit 9
fi


#########################
# Requirements 
#########################

# Debian (Stretch)
read -r -d '' DEBIAN_PACKAGES <<-'PACKAGES'
	python3-dev libssl-dev libffi-dev
PACKAGES

echo "Installing requested dependencies..."
# Display command
set -x

# Try installing the debian requirements
apt install $PACKAGES
