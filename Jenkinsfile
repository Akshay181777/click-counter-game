pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sonar-token')
    }

    tools {
        // This MUST match the name in Global Tool Configuration
        sonarRunner 'sonar-scanner'
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
                        sonar-scanner \
                        -Dsonar.projectKey=click-counter-game \
                        -Dsonar.projectName=click-counter-game \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://13.61.147.55:9000 \
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
            echo "❌ Pipeline Failed! Check SonarQube."
        }
    }
}
