pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh "ls -la && \
                    python3 -v && \
                    pip3 -v"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}