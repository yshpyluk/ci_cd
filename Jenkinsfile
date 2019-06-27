pipeline {
  agent {
    node {
      label 'testslave'
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
        git(url: 'https://github.com/pavlobornia/training-ci', credentialsId: 'aebb2aad-802d-40b3-96c4-493dae147640', branch: 'master')
      }
    }
    stage('Run Unit Tests') {
      parallel {
        stage('Run Unit Tests') {
          steps {
            dir(path: 'flask-app') {
              sh '''#!/bin/bash
docker-compose down
docker-compose build flask-app
docker-compose run flask-app pytest -v --junit-xml=./junit-report/report.xml
#docker-compose up -d
#docker-compose exec -T flask-app pytest -v --junit-xml=./junit-report/report.xml
docker-compose down
#docker-compose rm -sf
'''
            }

            junit 'flask-app/junit-report/report.xml'
            sh 'sudo rm -rf flask-app/junit-report'
          }
        }
        stage('Sleep 5') {
          steps {
            sh 'sleep 5'
          }
        }
        stage('Sleep 6') {
          steps {
            sleep 6
          }
        }
      }
    }
    stage('Run App') {
      steps {
        dir(path: 'flask-app') {
          sh '''#!/bin/bash
echo "RUN APP"
docker-compose up -d --build'''
        }

      }
    }
  }
}