pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/kudratmullani/ros-app.git'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t ros2-jazzy-demo .'
            }
        }

        stage('Run ROS Container (Smoke Test)') {
            steps {
                bat 'docker run --rm --privileged ros2-jazzy-demo sleep 5'
            }
        }
    }

    post {
        success {
            echo '✅ ROS 2 Jazzy Docker image built and ran successfully'
        }
        failure {
            echo '❌ CI failed – check Docker build or runtime logs'
        }
        always {
            bat 'docker system prune -f || true'
        }
    }
}
