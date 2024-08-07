#!/bin/bash
java -jar jenkins-cli.jar \
    -s http://3.109.5.227:8080/ \
    -auth @creds \
    safe-restart
