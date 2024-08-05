#!/bin/bash
java -jar jenkins-cli.jar \
    -s http://3.7.254.62:8080/ \
    -auth @creds \
    safe-restart
