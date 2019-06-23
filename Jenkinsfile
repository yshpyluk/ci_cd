pipeline {
  agent {
    node {
      label 'master'
    }

  }
  stages {
    stage('Stage 1') {
      steps {
        echo 'Start Pipeline'
      }
    }
    stage('Git Checkout') {
      steps {
        git(url: 'https://github.com/pavlobornia/training-ci', branch: 'master', credentialsId: 'aebb2aad-802d-40b3-96c4-493dae147640', poll: true)
      }
    }
    stage('Run Tests') {
      steps {
        dir(path: 'flask-app') {
          sh '''#!/bin/bash
docker-compose run flask-app pytest -v'''
        }

      }
    }
  }
}