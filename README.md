# Technical Assignment for DevOps Engineer

## Summary
The answers to the technical assignment for the position of DevOps Engineer are in this repository. The tasks show proficiency with best practices, troubleshooting, and infrastructure deployment and management in a Linux-based, containerized, high-availability system.

---

## First Task: Install a Systemd Service

### Goal
Use systemd to deploy and administer a service on a Linux system.

### Deliverables

1. **Application Code:** A simple Python HTTP server.
2. **Systemd Unit File:** Manages the application as a service.
3. **Deployment Instructions:** Steps to deploy and verify the service.

### Instructions
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>/task1
   ```
2. Run the deployment script to install and enable the service:
   ```bash
   sudo ./deploy_service.sh
   ```
3. Verify the service status:
   ```bash
   systemctl status my-python-app.service

---

## Task 2: Docker-Based Application Deployment

### Objective
Containerize the application from Task 1 using Docker and manage it with Docker Compose.

### Deliverables
1. **Dockerfile:** For creating the application container.
2. **docker-compose.yml:** Configures the application and reverse proxy (NGINX).
3. **Deployment Instructions:** Steps to deploy the containers.

### Instructions
1. Navigate to the Docker deployment folder:
   ```bash
   cd <repository_folder>/task2
   ```
2. Build and deploy the containers:
   ```bash
   docker-compose up --build -d
   ```
3. Access the application at: `http://localhost`

---

## Task 3: Kubernetes Cluster Setup

### Objective
Deploy the application on a Kubernetes cluster with high availability and rolling updates.

### Deliverables
1. **Kubernetes Manifests:** Deployment, Service, and Ingress.
2. **Deployment Guide:** Steps to deploy and test the application.

### Instructions
1. Navigate to the Kubernetes folder:
   ```bash
   cd <repository_folder>/task3
   ```
2. Deploy the application:
   ```bash
   kubectl apply -f .
   ```
3. Verify the deployment:
   ```bash
   kubectl get pods,svc,ingress
   ```
4. Access the application via the LoadBalancer or Ingress.

---

## Task 4: Debugging and Troubleshooting

### Objective
Identify and fix issues in a misconfigured systemd service or Kubernetes Deployment.

### Deliverables
1. **Fixed Configuration Files:** Updated systemd service or Kubernetes manifests.
2. **Troubleshooting Log:** Explanation of the approach.

### Instructions
1. Navigate to the troubleshooting folder:
   ```bash
   cd <repository_folder>/task4
   ```
2. Review the troubleshooting log for details on the fixes applied.
3. Apply the fixed configuration as needed.

---

## Task 5: Talos-Focused Configuration (Optional)

### Objective
Manage and troubleshoot a Talos-based cluster.

### Deliverables
1. **Written Explanation:** How to manage and troubleshoot a Talos-based cluster.
2. **Configuration Example:** Deployment YAML for a sample workload.

### Instructions
1. Refer to the `task5` folder for a detailed guide and example configurations.
2. Use `talosctl` and `kubectl` commands to manage the cluster.

---

## Repository Structure
- `task1/`: Files for Task 1 (Systemd Service).
- `task2/`: Files for Task 2 (Docker Deployment).
- `task3/`: Files for Task 3 (Kubernetes Setup).
- `task4/`: Files for Task 4 (Debugging and Troubleshooting).
- `task5/`: Files for Task 5 (Talos Configuration).

---

## Prerequisites
- Linux environment
- Docker and Docker Compose installed
- Kubernetes cluster (e.g., Minikube, K3s, or cloud provider)
- `kubectl` installed
- Optional: Talosctl for Task 5
