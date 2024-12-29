Situation: Incorrectly setup Kubernetes deployment or systemd servic
e
Let's go over how to find and address problems in a misconfigured Kubernetes deployment or systemd service, as well as how to record the troubleshooting procedures.

1. Systemd Service configuration error

Finding the Problem
Assume that despite having a systemd service file, the service isn't coming up correctly.

An example of a Python-http-server.service that is misconfigured:

	[Unit]
	Description=Python HTTP Server
	After=network.target

	[Service]
	ExecStart=/usr/bin/python3 /home/user/app.py
	WorkingDirectory=/home/user
	Restart=always
	User=www-data
	Group=www-data
	StandardOutput=append:/var/log/python-http-server.log
	StandardError=append:/var/log/python-http-server.log

	[Install]
	WantedBy=multi-user.target

Procedure for Troubleshooting

1- Verify the service's status: To verify the service's status and determine why it failed, run the following command.

	sudo systemctl status python-http-server.service

The output could look something like this:

	python-http-server.service - Python HTTP Server
	Loaded: loaded (/etc/systemd/system/python-http-server.service; enabled; vendor preset: enabled)
	Active: failed (Result: exit-code) since Tue 2024-12-24 15:00:00 UTC; 10s ago
	Process: 1234 ExecStart=/usr/bin/python3 /home/user/app.py (code=exited, status=2)

2- Check logs for mistakes: we can examine the logs to learn more about why the service failed:

	journalctl -u python-http-server.service

This could indicate a mistake such as:

	/home/user/app.py: No such file or directory

Finding the Issue:
The error message states that the www-data user cannot access or does not have the file /home/user/app.py.
Resolving the Problem
Adjust the permissions or file path: Verify that the www-data user can execute the Python script and that it is there at the designated place.

First, see if the script is present:

	ls /home/user/app.py

If the file doesn't exist, we might need to make sure the script is in /home/user or change the location in the systemd file's ExecStart directive.

Verify the appropriate permissions:

	sudo chown www-data:www-data /home/user/app.py
	sudo chmod 755 /home/user/app.py

Restart the service and reload systemd:

	sudo systemctl daemon-reload
	sudo systemctl restart python-http-server.service

Make sure the service is operational:

	sudo systemctl status python-http-server.service

2. Inaccurate Kubernetes Installation
Finding the Problem
Assume that the Python HTTP server's Kubernetes deployment is incorrect. The replicas are not being made correctly, and the service is not exposing the right port.

An example of a deployment that is not configured deployment.Yaml:

	apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-http-server
spec:
  replicas: 2
  selector:
    matchLabels:
      app: python-http-server
  template:
    metadata:
      labels:
        app: python-http-server
    spec:
      containers:
        - name: python-http-server
          image: python-http-server:latest
          ports:
            - containerPort: 80
          imagePullPolicy: IfNotPresent

Procedure for Troubleshooting

1-Verify the status of the deployment: To check if the deployment is proceeding well, run the following command:

	kubectl get pods

If there are problems, we may notice that the pods are not operating or that the deployment is incorrect.

2-Analyze the pods' logs: Use kubectl logs to inspect the pods' logs if they aren't operating properly.

	kubectl logs <pod-name>

We might find an error like:

	Error: 8080 is already in use

Finding the Issue: The container is attempting to bind to port 80 rather than port 8080, which is the port that the app.py exposes.

Resolving the Problem
Adjust the deployment's port: Refresh the deployment.To expose the proper port (8080 rather than 80), use yaml.
deployment that is fixed deployment.Yaml:	

apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-http-server
spec:
  replicas: 2
  selector:
    matchLabels:
      app: python-http-server
  template:
    metadata:
      labels:
        app: python-http-server
    spec:
      containers:
        - name: python-http-server
          image: python-http-server:latest
          ports:
            - containerPort: 8080  # Corrected port
          imagePullPolicy: IfNotPresent

Use the deployment that has been fixed:

	kubectl apply -f deployment.yaml

Check the deployment:

	kubectl get pods
	kubectl get deployment python-http-server

Check the service:

Use the external IP or the defined hostname to test the service if you have exposed it using a load balancer or ingress.

Log of Troubleshooting

Systemd service troubleshooting step-by-step:

Verify the status of the service: Run python-http-server.service with sudo systemctl status.

Use journalctl to examine logs for errors: journalctl -u python-http-server.service.

Adjust the permissions and file path: Make sure the www-data user can execute the script and that it is located in /home/user/app.py.

Use sudo systemctl daemon-reload && sudo systemctl restart python-http-server.service to restart the service and reload systemd.

Use sudo systemctl status python-http-server.service to check the service.


Detailed troubleshooting for the deployment of Kubernetes:

Verify the pod's status: To check if the pods are operating, use kubectl get pods.

To look for mistakes, examine logs: kubectl logs <pod-name>.

Correct the port mismatch: Adjust the deployment's port configuration.yaml (between 80 and 8080).

Fixed Configuration Files as Deliverables:

Python-http-server.service (systemd) has been fixed.
Kubernetes Deployment's deployment.yaml file was fixed.

Log of Troubleshooting:

examined the logs and service status to determine the problem.
Port configurations, permissions, and file paths have all been fixed.
Restarting the services and pods allowed me to confirm the fixes.


