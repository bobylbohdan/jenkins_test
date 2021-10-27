pipeline {
    agent any

    stages {
        stage('Setup python') {
            steps {
                sh "apt-get -y update && \
                    apt-get install -y --no-install-recommends \
                    python3.7 python3-pip python3.7-dev python3.7-distutils \
                    build-essential pkg-config software-properties-common curl unzip \
                    wget && \
                    apt-get clean       &&  \
                    rm -rf /var/lib/apt/lists/*"
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