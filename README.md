Title
DevOps CI/CD Pipeline using Jenkins, Docker, and Kubernetes

Project Description
This project demonstrates an end-to-end CI/CD pipeline for a Flask application.
The pipeline automates code build, Docker image creation, image push to Docker Hub,
and deployment using Kubernetes.

Tools used
• Git & GitHub  
• Jenkins (CI/CD)  
• Docker  
• Docker Hub  
• Kubernetes (Minikube)  
• AWS EC2 (Ubuntu)  
• Python (Flask)

Project Architecture
Developer → GitHub → Jenkins Pipeline
           → Docker Build → Docker Hub
           → Kubernetes Deployment
           → Application Running on EC2


CI/CD Workflow
1. Code pushed to GitHub
2. Jenkins pulls the latest code
3. Docker image is built automatically
4. Image is pushed to Docker Hub
5. Kubernetes deploys the updated application


How to Run
• Clone the repository
• Build Docker image
• Run container or deploy via Kubernetes

PREREQUISITES
AWS EC2 (Ubuntu 22.04)
Ports open in Security Group: 22, 5000
GitHub repo cloned
Docker installed
(Optional) Jenkins installed

CONNECT TO EC2
INSTALL REQUIRED PACKAGES
sudo apt update -y
sudo apt install -y git docker.io python3-pip
sudo systemctl start docker
sudo systemctl enable docker

Add user to docker group
sudo usermod -aG docker ubuntu
exit

Login or connect  again

CLONE PROJECT FROM GITHUB
git clone https://github.com/amitbhandare1320/devOps-project1.git
cd devOps-project1
PROJECT FILES:ls
BUILD DOCKER IMAGE:
docker build -t app-demo .

RUN DOCKER CONTAINER (PUBLIC ACCESS):
docker run -d --name flask-app -p 5000:5000 app-demo

check by docker ps

Kubernetes Deployment
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
To run continue:
nohup kubectl port-forward service/flask-service 5000:5000 --address 0.0.0.0 > portforward.log 2>&1 &

To kill :
ps aux | grep port-forward
pkill -f "kubectl port-forward"


Structure:
Dockerfile
Jenkinsfile
deployment.yaml
service.yaml
app.py
backend.py
templates/
README.md
