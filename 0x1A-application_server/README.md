# 0x1A. Application Server

## Concepts
For this project, we expect you to look at these concepts:
- Web Server
- Server
- Web stack debugging

## Background Context
Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project, you will add this piece to your infrastructure, plug it into your Nginx, and make it serve your Airbnb clone project.

## Resources
Read or watch:
- Application server vs web server
- How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04
- Running Gunicorn
- Be careful with the way Flask manages slashes in route - strict_slashes
- Upstart documentation

## Requirements
### General
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Everything Python-related must be done using `python3`.
- All config files must have comments.

### Bash Scripts
- All your files will be interpreted on Ubuntu 16.04 LTS.
- All your files should end with a new line.
- All your Bash script files must be executable.
- Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error.
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
- The second line of all your Bash scripts should be a comment explaining what the script is doing.

### Your servers
| Name           | Username | IP             | State   |
|----------------|----------|----------------|---------|
| 423066-web-01  | ubuntu   | 100.25.153.16  | running |
| 423066-web-02  | ubuntu   | 100.25.156.205 | running |
| 423066-lb-01   | ubuntu   | 34.207.222.185 | running |

## Tasks
### 0. Set up development with Python (mandatory)
Let’s serve what you built for AirBnB clone v2 - Web framework on `web-01`. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

**Requirements:**
- Make sure that task #3 of your SSH project is completed for `web-01`. The checker will connect to your servers.
- Install the `net-tools` package on your server: `sudo apt install -y net-tools`.
- Git clone your `AirBnB_clone_v2` on your `web-01` server.
- Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port 5000.
- Your Flask application object must be named `app` (This will allow us to run and check your code).

**Example:**
Author: Foster Setor

