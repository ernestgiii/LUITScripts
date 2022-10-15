#!/bin/bash
#This script is used to Install Apache and Install
sudo yum update -y
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
sudo echo "<h1>LUIT Blue Team For the Win!!! </h1>" > /var/www/html/index.html
