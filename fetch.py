import jenkins
import os

def fetch_and_save_config(server, job_name, output_file):
    try:
        config = server.get_job_config(job_name)  
        with open(output_file, 'w') as f:
            f.write(config)
        print(f"Fetched and saved config for job: {job_name}")
    except jenkins.NotFoundException as e: 
        print(f"Job '{job_name}' not found: {e}")
    except Exception as e: 
        print(f"Error fetching config for job '{job_name}': {e}")

def main():
    host = "http://35.154.135.229:8080/" 
    username = "yashaswi"
    password = "11b94281514548a5e07a4125bd13c1fb42" 
    output_dir = "job_configs"
    os.makedirs(output_dir, exist_ok=True)

    try:
        server = jenkins.Jenkins(host, username, password)
        all_jobs = server.get_all_jobs()
        job_names = [job['name'] for job in all_jobs] 
        for job_name in job_names:
            output_file = os.path.join(output_dir, f"{job_name}.xml")
            fetch_and_save_config(server, job_name, output_file)

    except jenkins.JenkinsException as e:  
        print(f"Error connecting to Jenkins server: {e}")

if __name__ == "__main__":
    main()
