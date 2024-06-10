0x1B. Web Stack Debugging #4

Debugging refers to identifying and fixing issues in a web application or server stack. The goal is to ensure smooth operation and optimal performance. Here are some key points from the Web Stack Debugging #4:

Simulating HTTP Requests: The video demonstrates simulating HTTP requests to a web server. For example, making 2000 requests to a server with 100 requests at a time. The video shows that 943 requests failed. The goal is to fix the stack to achieve zero failures. Remember, when something goes wrong, logs are your best friends!
Install ‘puppet-lint’: The README mentions installing puppet-lint, a tool for checking Puppet manifests. You can install it using the following commands:

Task Description
In this web stack debugging task, we are testing how well our web server setup featuring Nginx is performing under pressure. Unfortunately, it’s not doing well, as we’re experiencing a large number of failed requests.

For benchmarking, we’re using ApacheBench, a popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed. Our goal is to fix our stack so that we get to 0 failed requests. Remember that when something is going wrong, logs are your best friends!

Puppet Manifests
All files will be interpreted on Ubuntu 14.04 LTS.
Files should end with a new line.
A README.md file at the root of the project folder is mandatory.
Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
Your Puppet manifests must run without error.
The first line of your Puppet manifests must be a comment explaining what the manifest is about.
Puppet manifest files must end with the extension .pp.
Files will be checked with Puppet v3.4.
Installation of puppet-lint
To install puppet-lint, follow these steps:

$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1

Debugger: Foster Setor
