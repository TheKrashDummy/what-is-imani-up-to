#!/bin/bash

sudo systemctl start cloudflared-imani-main-tunnel
sudo systemctl start run-flask-server
sudo systemctl start run-go-server