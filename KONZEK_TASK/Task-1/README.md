1-Save the Python Script: Save the Python HTTP server code in a file, e.g., /path/to/your_script.py.

2-Save the Systemd Unit File: Save the systemd unit file content in /etc/systemd/system/python-http-server.service.

Adjust File Paths and Permissions:

Replace /path/to/your_script.py with the actual path to your script.

Update your_user and your_group to the appropriate user and group.

3-Check File Permissions: Ensure the script is executable and accessible by the user specified in the service:

chmod +x /path/to/your_script.py

4-Create the Log File Directory: /var/log/python_http_server.log

sudo mkdir -p /var/log
sudo touch /var/log/python_http_server.log
sudo chown user:group /var/log/python_http_server.log #Your User name and group

5-Enable and Start the Service: Run the following commands to enable and start the service:

sudo systemctl daemon-reload
sudo systemctl enable python-http-server.service
sudo systemctl start python-http-server.service

6-Verify the Service: Check the service status and logs:

sudo systemctl status python-http-server.service
tail -f /var/log/python_http_server.log

7- Test the Application: Open a browser or use curl to access the server:

curl http://localhost:8080
