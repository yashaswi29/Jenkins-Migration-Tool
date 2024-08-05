import jenkins
import requests
import json
import os

# Jenkins server configuration
host = "http://3.7.254.62:8080/"
# username = os.environ.get('JENKINS_USER')
# password = os.environ.get('JENKINS_TOKEN')
username = "yashaswi"
password = "111eac27585fd3bd393cf083f75fad94c4"
server = jenkins.Jenkins(host, username, password)
user = server.get_whoami()
version = server.get_version()

# if username is None or password is None:
#     print("JENKINS_USER and JENKINS_TOKEN environment variables must be set.")
# else:
#     try:
#         # Connect to Jenkins server
#         server = jenkins.Jenkins(host, username, password)
#         user = server.get_whoami()
#         version = server.get_version()
#         print(user)
#         print(f'Hello {user["fullName"]} from Jenkins {version}')
#     except jenkins.JenkinsException as e:
#         print(f"Failed to connect to Jenkins: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# creating blank jobs
# server.create_job("job1", jenkins.EMPTY_CONFIG_XML)

# create pre planned jobs using xml and python
project1_xml = open ("project1.xml", mode ='r', encoding ='utf-8').read()
server.create_job("job2", project1_xml)

#view jobs
# jobs = server.get_jobs()
# print(jobs)

#updated jobs // this updated means, you should have the updated xml
# project1_xml = open ("project1.xml", mode ='r', encoding ='utf-8').read()

# #trigger jobs
# server.build_job("job1")
