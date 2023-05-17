#!/bin/bash

#Check if python is installed
python3 -m venv log-venv
#Check if venv already exists
source log-venv/bin/activate
pip3 install -r requirements.txt
python3 main.py