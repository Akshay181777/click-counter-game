pipeline {
    agent any

    environment {
        IMAGE_NAME = "click-counter-game"
        CONTAINER_NAME = "click-counter-game-container"
        ECR_URI = "949156002932.dkr.ecr.eu-north-1.amazonaws.com/click-counter-game"
        AWS_REGION = "eu-north-1"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'sonar-scanner'
                    withSonarQubeEnv('server-sonar') {
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=click-counter-game \
                            -Dsonar.projectName=click-counter-game \
                            -Dsonar.sources=.
                        """
                    }
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

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push Docker Image to ECR') {
            steps {
                sh '''
                # Login to ECR
                aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_URI

                # Tag the image for ECR
                docker tag $IMAGE_NAME:latest $ECR_URI:latest

                # Push to ECR
                docker push $ECR_URI:latest
                '''
            }
        }

        stage('Deploy Container on EC2') {
            steps {
                sh '''
                # Stop old container if exists
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true

                # Pull latest image from ECR
                docker pull $ECR_URI:latest

                # Run container
                docker run -d -p 8000:8000 --name $CONTAINER_NAME $ECR_URI:latest
                '''
            }
        }
    }
}
