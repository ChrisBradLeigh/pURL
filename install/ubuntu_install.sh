#!/bin/bash
#This is a quick script that create a service out of the python script.

mv /var/www/pURL/install/purl.service /lib/systemd/system/purl.service
systemctl daemon-reload
systemctl start purl.service
