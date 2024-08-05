#!/bin/bash

java -jar jenkins-cli.jar -s http://13.201.4.9:8080/ -auth @creds who-am-i
set -x
for plugin in $(cat plugin.txt); do
    java -jar jenkins-cli.jar \
    -s http://3.111.55.36:8080/ \
    -auth @creds \
    install-plugin "$plugin"
done
java -jar jenkins-cli.jar \
    -s http://3.111.55.36:8080/ \
    -auth @creds \
    safe-restart


