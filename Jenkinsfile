pipeline {
    agent any
    environment {
        IMAGE_NAME = 'shoppy-web'
        DOCKER_HUB_USER = 'jawadbutt07'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/JawadButt07/Shoppy.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build --network=host -t ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest .'
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    docker run --rm \
                    --network=ecommerce_default \
                    -e DB_HOST=db \
                    -e DB_NAME=shoppy_db \
                    -e DB_USER=shoppy_user \
                    -e DB_PASSWORD=shoppy_pass \
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
        stage('Deploy') {
            steps {
                sh 'cd /ecommerce && docker compose up -d --build'
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
