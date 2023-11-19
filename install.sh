#!/bin/bash -e

# superuser:
# bash -e install.sh
# non-superuser:
# sudo bash -e install.sh

# python, curl installed
python3 --version
curl --version

# Download the file
url="https://raw.githubusercontent.com/junaga/v-vcs/main/bin.py"
curl -L $url > /usr/local/bin/v

# make it executable
chmod +x /usr/local/bin/v

# v installed
v --version

# on some systems $PATH is cached
# [close, open, the terminal]
# v --version
