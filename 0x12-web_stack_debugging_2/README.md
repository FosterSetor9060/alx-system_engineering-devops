0x12. Web Stack Debugging #2
Description
This project focuses on debugging web stacks. You’ll be given broken or buggy web stacks in isolated containers and tasked with fixing them to a working state. For each task, you’ll write a script automating the necessary commands to resolve the issues.

Concepts
For this project, students are expected to understand the concept of web stack debugging.

Requirements
All your files will be interpreted on Ubuntu 14.04 LTS.
All your files should end with a new line.
A README.md file at the root of the project folder is mandatory.
All your Bash script files must be executable.
Your Bash scripts must pass Shellcheck without any errors.
Your Bash scripts must run without errors.
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash.
The second line of all your Bash scripts should be a comment explaining what the script does.
Tasks
0. Run Software as Another User (mandatory)
The user root is the “superuser” on Linux, capable of performing any action. However, it’s good practice not to be logged in as root to avoid accidental destructive commands. Instead, run as a privileged user who can perform tasks that the root user can do. Write a Bash script that accepts one argument: the username. The script should run the whoami command under the specified user.

Example:

$ whoami
root
$ ./0-iamsomeoneelse www-data
www-data
$ whoami
root

1. Run Nginx as Nginx (mandatory)
Running web servers as the root user is a security risk. To prevent attackers from logging in as root, it’s best to run web servers as less privileged users. In this task, fix the container so that Nginx runs as the nginx user. The following requirements apply:

Nginx must be running as the nginx user.
Nginx must listen on all active IPs on port 8080.
You cannot use apt-get remove.
Write a Bash script that configures the container to meet the above requirements.

Author: Foster Setor 
