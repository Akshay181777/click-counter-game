pipeline {
    agent any

    environment {
        SONAR_SCANNER = 'qube'
        SONARQUBE_SERVER = 'server-sonar'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Akshay181777/click-counter-game.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE_SERVER}") {
                    sh """
                        ${tool SONAR_SCANNER}/bin/sonar-scanner \
                        -Dsonar.projectKey=click-counter-game \
                        -Dsonar.projectName=click-counter-game \
                        -Dsonar.sources=. \
                        -Dsonar.inclusions=**/*.py,**/*.js,**/*.html \
                        -Dsonar.python.version=3 \
                        -Dsonar.javascript.node.executable=/usr/bin/node
                    """
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 10, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
