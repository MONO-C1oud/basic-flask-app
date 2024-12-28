pipeline {
    agent any

    environment {
        VIRTUAL_ENV = ".venv"  // Virtual environment directory
        DEPLOY_DIR = "/var/www/flask-app" // Deployment directory
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "Cloning the repository..."
                git branch: 'main', url: 'https://github.com/MONO-C1oud/basic-flask-app.git'
            }
        }

        stage('Set Up Environment') {
            steps {
                echo "Setting up Python environment..."
                sh '''
                python3 -m venv ${VIRTUAL_ENV}
                source ${VIRTUAL_ENV}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests with pytest..."
                sh '''
                source ${VIRTUAL_ENV}/bin/activate
                pytest --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('Build Application') {
            steps {
                echo "Building application..."
                sh '''
                source ${VIRTUAL_ENV}/bin/activate
                python setup.py build
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                echo "Deploying application..."
                sh '''
                mkdir -p ${DEPLOY_DIR}
                cp -r * ${DEPLOY_DIR}
                '''
                echo "Restarting application..."
                sh '''
                sudo systemctl restart flask-app
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check the logs for details."
        }
    }
}
