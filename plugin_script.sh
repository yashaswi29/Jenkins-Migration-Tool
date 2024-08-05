#!/bin/bash
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


