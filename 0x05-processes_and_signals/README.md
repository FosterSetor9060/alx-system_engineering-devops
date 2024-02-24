0x05. Processes and signals
DevOps
Shell
Bash
Syscall
Scripting
 By: Sylvain Kalache








For those who want to know more and learn about all signals, check out this article.

At the end of this project you are expected to be able to explain, without the help of Google:

What is a PID
What is a process
How to find a process PID
How to kill a process
What is a signal
What are the 2 signals that cannot be ignored
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 14.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing
Write a Bash script that displays its PID.

GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 0-what-is-my-pid
Write a Bash script that displays a list of currently running processes.

Requirements:

Must show all processes, for all users, including those which might not have a TTY
Display a user-oriented format
Show process hierarchy
GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 1-list_your_processes
Using your previous exercise command, write a Bash script that displays line containing the bash word, this allowing you to easily get the PID of your Bash process

Requirements:

You cannot use pgrep
The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)
Here we can see that my Bash PID is 4404.

GitHub repository: holberton-system_engineering-devops
Directory: 0x05-processes_and_signals
File: 2-show_your_bash_pid
Write a Bash script that displays the PID, along with the process name, of processes which name contains the word bash.

Requirements:

You cannot use ps
Here we can see that:
