#!/bin/bash

java -jar jenkins-cli.jar -s  http://3.7.254.62:8080/ -auth @creds who-am-i
set -x
for plugin in $(cat plugins.txt); do
    java -jar jenkins-cli.jar \
    -s http://3.7.254.62:8080/ \
    -auth @creds \
    install-plugin "$plugin"
done
# java -jar jenkins-cli.jar \
#     -s http://3.7.254.62:8080/ \
#     -auth @creds \
#     safe-restart

``
# 111eac27585fd3bd393cf083f75fad94c4
