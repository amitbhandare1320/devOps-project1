pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/amitbhandare1320/devOps-project1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t amit1320/app-demo:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh 'docker push amit1320/app-demo:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl rollout restart deployment flask-app'
            }
        }
    }
}
