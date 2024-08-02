
#!/bin/bash
set -x
for plugin in $(cat plugins.txt); do \
    java -jar /Users/yashaswitiwari/Developer/Groovy/py-jen/jenkins-cli.jar \
    -s http://localhost:8080/ \
    -auth yashaswi:yashaswi \
    install-plugin $plugin; \
done
java -jar /Users/yashaswitiwari/Developer/Groovy/py-jen/jenkins-cli.jar -s http://localhost:8080/ -auth yashaswi:yashaswi safe-restart