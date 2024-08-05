import jenkins
import json
import os

host = "http://3.7.254.62:8080/"
username = os.environ.get('JENKINS_USER')
password = os.environ.get('JENKINS_TOKEN')
server = jenkins.Jenkins(host, username, password)

try:
    user = server.get_whoami()
    version = server.get_version()
    print(user)
    print('Hello %s from Jenkins %s' % (user['fullName'], version))
except jenkins.BadHTTPException as e:
    print(f"HTTP error occurred: {e}")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# creating blank jobs
# server.create_job("job1", jenkins.EMPTY_CONFIG_XML)

#create pre planned jobs using xml and python
# project1_xml = open ("project1.xml", mode ='r', encoding ='utf-8').read()
# server.create_job("job2", project1_xml)

#view jobs
# jobs = server.get_jobs()
# print(jobs)

#updated jobs // this updated means, you should have the updated xml
# project1_xml = open ("project1.xml", mode ='r', encoding ='utf-8').read()

# #trigger jobs
# server.build_job("job1")
