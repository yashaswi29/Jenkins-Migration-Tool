#!/bin/bash
java -jar jenkins-cli.jar \
    -s http://3.6.39.114:8080/manage/cli/ \
    -auth @creds \
    safe-restart
