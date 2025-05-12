#!/bin/bash

sudo systemctl stop cloudflared-imani-main-tunnel
sudo systemctl stop run-flask-server
sudo systemctl stop run-go-server