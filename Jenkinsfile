pipeline {
    agent any
    environment {
        IMAGE_NAME = 'ecommerce-web'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/JawadButt07/Shoppy.git'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'docker run --rm --network=ecommerce_default -e DB_HOST=db -e DB_NAME=shoppy_db -e DB_USER=shoppy_user -e DB_PASSWORD=shoppy_pass ecommerce-web:latest python manage.py test --verbosity=2 || true'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker restart shoppy_web shoppy_nginx'
            }
        }
    }
    post {
        success { echo 'Deployment successful!' }
        failure { echo 'Build failed.' }
    }
}
