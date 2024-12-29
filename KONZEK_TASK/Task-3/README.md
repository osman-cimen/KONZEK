Kubernetes Manifests:

deployment.yaml
service.yaml
ingress.yaml (if using Ingress)

Guide on Deploying and Testing:

Create the Kubernetes resources with kubectl apply -f <filename>.

Verify the application is running with kubectl get pods and kubectl get svc.

Test the application via LoadBalancer or Ingress.

Using LoadBalancer: Once the LoadBalancer service is created, you can get the external IP with:

kubectl get svc python-http-server

The external IP will be listed under the EXTERNAL-IP column. You can access the application at http://<EXTERNAL-IP>

Using Ingress: 
If you're using Ingress, ensure that you have an Ingress controller (e.g., NGINX) running. You can then access the application by adding python-http-server.local to your /etc/hosts file (pointing to the Ingress controller’s external IP) or using a DNS name. You can access it via http://python-http-server.local.

Rolling Updates for the Application

Kubernetes supports rolling updates natively. To demonstrate a rolling update, modify the Docker image or application code (e.g., change the response text in app.py), rebuild the Docker image, and push it to your container registry.

Then, update the Deployment with the new image:

kubectl set image deployment/python-http-server python-http-server=python-http-server:latest
This command will trigger a rolling update, where Kubernetes will gradually replace old pods with new ones while ensuring there is no downtime.

To verify that the rolling update is happening:

kubectl rollout status deployment/python-http-server

This will show the status of the deployment update. Once the update is complete, you can check the running pods with:

kubectl get pods

Deploying and Testing the Application
Deployment steps:

Create the Deployment and Service:

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

For Ingress, use:

kubectl apply -f ingress.yaml

Verify that the pods are running:

kubectl get pods

Check the service:


kubectl get svc python-http-server

For LoadBalancer, check the external IP.

For Ingress, ensure the Ingress controller is working, and access the app via the hostname.
Test the Application:

Access the application using the LoadBalancer's external IP or the Ingress URL:

curl http://<EXTERNAL-IP>   # For LoadBalancer
curl http://python-http-server.local   # For Ingress (if configured)

Perform Rolling Updates:

To perform a rolling update, modify the image tag in the Deployment YAML or use kubectl set image as shown earlier.

kubectl set image deployment/python-http-server python-http-server=python-http-server:<new-tag>

Monitor the rolling update:

kubectl rollout status deployment/python-http-server

Perform a rolling update with kubectl set image
