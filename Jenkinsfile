pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 -m venv .ci-venv'
                sh '.ci-venv/bin/python -m pip install --upgrade pip'
                sh '.ci-venv/bin/python -m pip install -r app/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '.ci-venv/bin/python -m pytest -v app/tests'
            }
        }
    }

    post {
        always {
            sh 'rm -rf .ci-venv'
        }
    }
}
