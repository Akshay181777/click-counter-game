pipeline {
    agent any

    environment {
        SONAR_SCANNER = 'qube'           // Jenkins SonarQube Scanner tool name
        SONARQUBE_SERVER = 'server-sonar' // Jenkins SonarQube server name
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
                        -Dsonar.javascript.node.executable=none
                    """
                }
            }
        }

        stage('Quality Gate') {
            steps {
                script {
                    timeout(time: 10, unit: 'MINUTES') {
                        def qg = waitForQualityGate abortPipeline: true
                        echo "Quality Gate status: ${qg.status}"
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
        success {
            echo "Quality Gate passed! ✅"
        }
        failure {
            echo "Quality Gate failed ❌"
        }
    }
}
