pipeline {
    agent any

    tools {
        sonarRunner 'sonar-scanner'
    }

    environment {
        SONAR_TOKEN = credentials('sonar-token')
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('server-sonar') {
                    sh """
                        ${tool 'sonar-scanner'}/bin/sonar-scanner \
                        -Dsonar.projectKey=click-counter-game \
                        -Dsonar.projectName=click-counter-game \
                        -Dsonar.sources=. \
                        -Dsonar.login=${SONAR_TOKEN}
                    """
                }
            }
        }

        stage('Quality Gate Check') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

    post {
        success {
            echo "✅ Quality Gate Passed!"
        }
        failure {
            echo "❌ Pipeline Failed!"
        }
    }
}
