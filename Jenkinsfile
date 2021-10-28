pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh "pip3 install -r requirements.txt"
            }
        }
        stage('Test') {
            steps {
                sh "python3 -m pytest --cov=lib ./tests"
            }
        }
        stage('Deploy') {
            steps {
                sh "python3 __main__.py"
            }
        }
    }
}