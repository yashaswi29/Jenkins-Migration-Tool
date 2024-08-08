#!/bin/bash
java -jar jenkins-cli.jar \
    -s http://13.201.70.135:8080/ \
    -auth @creds \
    safe-restart
