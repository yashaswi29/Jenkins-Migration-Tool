import jenkins
import requests
import json
import os

# Jenkins server configuration
# username = os.environ.get('JENKINS_USER')
# password = os.environ.get('JENKINS_TOKEN')
host = "http://3.6.39.114:8080/manage/cli/" 
username = "yashaswi"  
password = "11503db44711d5479c3f4d78bc92e5bfd7" 
server = jenkins.Jenkins(host, username, password)
config_dir = "/Users/yashaswitiwari/Developer/Groovy/py-jen/fetch_pull/job_configs"
print(f"Using configuration directory: {config_dir}")

def push_job_configs(server, config_dir):
    for filename in os.listdir(config_dir):
        if filename.endswith(".xml"):
            job_name = filename[:-4]  
            config_file_path = os.path.join(config_dir, filename)
            with open(config_file_path, 'r') as f:
                config_xml = f.read()
            if server.job_exists(job_name):
                print(f"Reconfiguring job: {job_name}")
                server.reconfig_job(job_name, config_xml)
            else:
                print(f"Creating job: {job_name}")
                server.create_job(job_name, config_xml)
            print(f"Pushed configuration for job: {job_name}")

def main():
    try:
        user = server.get_whoami()
        version = server.get_version()
        print(f"Hello {user['fullName']} from Jenkins {version}")
        push_job_configs(server, config_dir)
    except jenkins.JenkinsException as e:
        print(f"Error connecting to Jenkins server: {e}")

if __name__ == "__main__":
    main()


# https://python-jenkins.readthedocs.io/en/latest/examples.html

#other commands from the python-jenkins documentation which might be useful

# my_job = server.get_job_config('cool-job')
# print(my_job) # prints XML configuration
# server.build_job('empty')
# server.disable_job('empty')
# server.copy_job('empty', 'empty_copy')
# server.enable_job('empty_copy')
# server.reconfig_job('empty_copy', jenkins.RECONFIG_XML)

# server.delete_job('empty')
# server.delete_job('empty_copy')

# # build a parameterized job
# # requires creating and configuring the api-test job to accept 'param1' & 'param2'
# server.build_job('api-test', {'param1': 'test value 1', 'param2': 'test value 2'})
# last_build_number = server.get_job_info('api-test')['lastCompletedBuild']['number']
# build_info = server.get_build_info('api-test', last_build_number)
# print build_info

# # get all jobs from the specific view
# jobs = server.get_jobs(view_name='View Name')
# print jobs

# server.create_view('EMPTY', jenkins.EMPTY_VIEW_CONFIG_XML)
# view_config = server.get_view_config('EMPTY')
# views = server.get_views()
# server.delete_view('EMPTY')
# print views

# server.create_node('slave1')
# nodes = get_nodes()
# print nodes
# node_config = server.get_node_info('slave1')
# print node_config
# server.disable_node('slave1')
# server.enable_node('slave1')

# # create node with parameters
# params = {
#     'port': '22',
#     'username': 'juser',
#     'credentialsId': '10f3a3c8-be35-327e-b60b-a3e5edb0e45f',
#     'host': 'my.jenkins.slave1'
# }
# server.create_node(
#     'slave1',
#     nodeDescription='my test slave',
#     remoteFS='/home/juser',
#     labels='precise',
#     exclusive=True,
#     launcher=jenkins.LAUNCHER_SSH,
#     launcher_params=params)

# server.build_job('foo')
# queue_info = server.get_queue_info()
# id = queue_info[0].get('id')
# server.cancel_queue(id)

# next_bn = server.get_job_info('job_name')['nextBuildNumber']
# server.set_next_build_number('job_name', next_bn + 50)

# server.create_promotion('prom_name', 'prom_job', jenkins.EMPTY_PROMO_CONFIG_XML)
# server.promotion_exists('prom_name', 'prom_job')
# print server.get_promotions('prom_job')

# server.reconfig_promotion('prom_name', 'prom_job', jenkins.PROMO_RECONFIG_XML)
# print server.get_promotion_config('prom_name', 'prom_job')

# server.delete_promotion('prom_name', 'prom_job')

#When the username and token is not hardcde use,# if username is None or password is None:
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