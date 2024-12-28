pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/MONO-C1oud/basic-flask-app.git']]])
            }
        }
        stage('Install Dependencies') {
            steps {
                // Use Python and pip commands compatible with Windows
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Use pytest command for Windows
                bat 'pytest tests'
            }
        }
        stage('Build Application') {
            steps {
                // Simulate build with an echo statement (replace with actual build steps if needed)
                bat 'echo Building the application...'
            }
        }
        stage('Deploy Application') {
            steps {
                // Use xcopy to copy application files to the deployment directory
                bat 'xcopy /E /I /Y .\\* C:\\path\\to\\deployment\\directory\\'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
