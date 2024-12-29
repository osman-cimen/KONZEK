Step 1: Prepare the Files

Save python_http_server.py, Dockerfile, docker-compose.yml, and nginx.conf in the same directory.

Step 2: Build the Docker Image

Run the following command to build the application image:

docker-compose build

Step 3: Deploy the Stack

Start the services using:

docker-compose up -d

Step 4: Verify the Deployment
Check the running services:


docker-compose ps

Access the application via the reverse proxy at http://localhost.

Step 5: Test High Availability
Scale the replicas if needed:

docker-compose up --scale app=3 -d

Step 6: Cleanup
Stop and remove the services when done:

docker-compose down

Deliverables Summary

Dockerfile: Builds the application container.
docker-compose.yml: Manages the app and reverse proxy with high availability.
nginx.conf: Configures the reverse proxy.
