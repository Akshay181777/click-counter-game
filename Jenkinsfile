pipeline {
    agent any

    environment {
        SONAR_SCANNER = 'qube'                 // Your Jenkins global tool name for SonarQube Scanner
        SONARQUBE_SERVER = 'server-sonar'      // Your Jenkins SonarQube server name
        SONAR_TOKEN = credentials('gene-token') // Jenkins secret text token
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                git url: 'https://github.com/Akshay181777/click-counter-game.git', branch: 'main'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo 'Running SonarQube Analysis...'
                withSonarQubeEnv("${SONARQUBE_SERVER}") {
                    sh """
                        ${tool SONAR_SCANNER}/bin/sonar-scanner \
                        -Dsonar.projectKey=gene-token \
                        -Dsonar.sources=. \
                        -Dsonar.inclusions=**/*.js,**/*.html \
                        -Dsonar.host.url=${SONARQUBE_SERVER} \
                        -Dsonar.login=${SONAR_TOKEN}
                    """
                }
            }
        }

        stage('Quality Gate') {
            steps {
                echo 'Waiting for SonarQube Quality Gate result...'
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

    post {
        success {
            echo 'SonarQube Analysis Passed ✅'
        }
        failure {
            echo 'SonarQube Analysis Failed ❌'
        }
    }
}
