# Jenkins Migration Toolkit

### Migrate Your Jenkins Jobs, Plugins, and Server Configurations Seamlessly

![Jenkins](https://img.shields.io/badge/Jenkins-Migration-blue.svg) 

## 📋 Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Pre-requisites](#pre-requisites)
4. [Setup Guide](#setup-guide)
   - [1. Clone the Repository](#1-clone-the-repository)
   - [2. Install Jenkins](#2-install-jenkins)
   - [3. Configure Server A](#3-configure-server-a)
   - [4. Configure Server B](#4-configure-server-b)
   - [5. Push to GitHub](#5-push-to-github)
5. [File Descriptions](#file-descriptions)
6. [How It Works](#how-it-works)
7. [Troubleshooting](#troubleshooting)
8. [Contributing](#contributing)
9. [License](#license)

## 📝 Introduction
Effortlessly migrate your Jenkins jobs, plugins, and server configurations from Server A to Server B with this toolkit. This repository contains scripts, configurations, and automated pipelines to make the migration process as seamless as possible, reducing manual work and potential errors.

## ✨ Features
- **Automated Job Migration**: Quickly fetch and install Jenkins jobs from one server to another.
- **Plugin Management**: Transfer and install necessary plugins on the target server.
- **Jenkins Configuration as Code (JCasC)**: Helps maintain the configuration of the Jenkins server.
- **Simple Setup**: Easy-to-follow instructions to guide you through the process.

## 🔧 Pre-requisites
Before starting, ensure you have:
- Access to **Jenkins Server A** (source) and **Jenkins Server B** (target).
- Installed **Python 3.x**, **Git**, and **Java** on your local machine.
- Jenkins CLI (`jenkins-cli.jar`) downloaded from Jenkins UI.
- Proper permissions on both servers.

## 🛠 Setup Guide

### 1. Clone the Repository
```bash
git clone 
cd Jenkins-Migration
```

### 2. Install Jenkins
Follow the official Jenkins installation guide for your environment:

- [Jenkins Installation Documentation](https://www.jenkins.io/doc/book/installing/)

### 3. Configure Server A
1. **Update `fetch.py`:** Replace `host` and `username` with the current URL and username of Jenkins Server A.
   ```python
   # Example snippet in fetch.py
   host = "http://your-jenkins-server-A.com"
   username = "your-username"
   ```
2. **Generate Jenkins API Token**

3. **Go to the Jenkins Dashboard**, click on your username (top right), and click **Configure**.

4. **Scroll down to the **API Token** section and generate a new token.**

5. **Save the token securely.**

### Store Credentials
In the `creds` file, use the following format:
```csharp
[Username:api_token]
```
### 4. Configure Server B

1. **Update `test1.py`:** Replace the `host` with the current URL of Jenkins Server B.
   ```python
   # Example snippet in test1.py
   host = "http://your-jenkins-server-B.com"
   ```
2. **Modify restart_script.sh and plugin_script.sh: Replace the host in both scripts with the URL of Server B.**
    ```bash
    # Example in restart_script.sh and plugin_script.sh
    java -jar jenkins-cli.jar -s http://your-jenkins-server-B.com restart
    ```
3. **Modify restart_script.sh and plugin_script.sh: Replace the host in both scripts with the URL of Server B.**
    ```bash
    # Example in restart_script.sh and plugin_script.sh
    java -jar jenkins-cli.jar -s http://your-jenkins-server-B.com restart
    ```
### 5. Push the Code 
    ```bash
    git add .
    git commit -m "Initial Jenkins Migration Setup"
    git push origin <branch-name>
    ```
### 6. 📁 File Descriptions

| File Name          | Description                                                         |
|--------------------|---------------------------------------------------------------------|
| `fetch.py`         | Retrieves specified jobs from Server A and pulls the XML files.    |
| `creds`            | Stores Jenkins Server A credentials (username and API token).      |
| `jcasc.yaml`       | Jenkins Configuration as Code file, to be configured manually.     |
| `jenkins-cli.jar`  | Jenkins Command-Line Interface tool.                               |
| `job_names.txt`    | Contains names of the jobs to be fetched from Server A.            |
| `plugins.txt`      | List of plugins to be installed on Server B.                       |
| `plugin_script.sh` | Script to install plugins on Server B.                             |
| `plugins.groovy`   | Groovy script for plugin installation.                             |
| `restart_script.sh`| Script to restart Server B.                                        |
| `test1.py`         | Python script to install jobs on Server B.                         |
| `requirements.txt` | Python dependencies required for this toolkit.                     |

### ⚙️ How It Works

1. **Fetch Jobs:** `fetch.py` reads job names from `job_names.txt` and pulls the job configuration from Server A.
   ```bash
   python fetch.py
   ```
2. **Install Plugins**
    `plugin_script.sh` reads `plugins.txt` and installs the required plugins on Server B.
    
    ```bash
    bash plugin_script.sh
    ```
3. **Install Jobs**
    `test1.py` uploads and configures the fetched jobs on Server B.
    ```python
    python test1.py
    ```
4. **Restart Server**
    Use `restart_script.sh` to restart Server B for changes to take effect.
    ```python
    bash restart_script.sh
    ```
### ⚠️ Note: Configuration (jcasc.yaml) must be done manually on Server B.
### 🛠 Troubleshooting
- **Authentication Failed:** Make sure the API token is correct and saved in the `creds` file.
- **Connection Issues:** Verify the URLs of both Jenkins servers.
- **Plugins Not Installing:** Double-check the `plugins.txt` file for any misspelled plugin names.

### 🤝 Contributing
We welcome contributions! Feel free to fork this repository, make your improvements, and create a pull request.

```bash
# Step 1: Fork the repository.
# Step 2: Create a new branch.
git checkout -b feature-branch

# Step 3: Commit your changes.
git add .
git commit -m "Add your message here"

# Step 4: Push to your fork.
git push origin feature-branch

# Step 5: Open a pull request.
```

