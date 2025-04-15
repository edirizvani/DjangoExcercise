pipeline {
  agent any
  stages {
    stage('Clone repository') {
      steps {
        checkout scm
      }
    }

    stage('Build image') {
      steps {
        script {
          dockerImage = docker.build("${IMAGE_NAME}:${env.BRANCH_NAME}-${env.BUILD_NUMBER}")
        }

      }
    }

    stage('Push image') {
      when {
        branch 'dev'
      }
      steps {
        script {
          docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            dockerImage.push("${env.BRANCH_NAME}-${env.BUILD_NUMBER}")
            dockerImage.push("${env.BRANCH_NAME}-latest")
          }
        }

      }
    }

  }
  environment {
    IMAGE_NAME = 'edirizvani/djangoexercise'
  }
}
