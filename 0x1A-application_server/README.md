# 0x1A-application_server
Serving flask web application using gunicorn
sudo apt install -y net-tools
# i installed pip and python3-dev
sudo apt-get update
sudo apt-get install python3-pip python3-dev nginx
# i installed gunicorn and flask
pip install gunicorn flask
# I stopped datadog as it was using port 5000
sudo systemctl stop datadog-agent

