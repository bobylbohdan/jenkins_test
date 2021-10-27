pipeline {
    agent any

    stages {
        stage('Setup python') {
            steps {
                sh "python3 -v"
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