pipeline {
    agent any

    stages {
        stage('Setup python') {
            steps {
                sh "python -v"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}