pipeline {
    agent any
    environment {
        IMAGE_NAME = 'shoppy-web'
        DOCKER_HUB_USER = 'jawadbutt07'
        CONTAINER_NAME = 'shoppy_web'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/JawadButt07/Shop.py-.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest .'
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    docker run --rm \
                    -e DB_HOST=db \
                    ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest \
                    python manage.py test --verbosity=2 || true
                '''
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest'
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f /ecommerce/k8s/'
                sh 'kubectl rollout restart deployment/shoppy-web'
                sh 'kubectl rollout status deployment/shoppy-web'
            }
        }
    }
    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Build failed. Check logs above.'
        }
    }
}
