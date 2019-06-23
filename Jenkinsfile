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
    stage('Run App') {
      steps {
        sh '''#!/bin/bash
docker-compose up -d;'''
      }
    }
  }
}