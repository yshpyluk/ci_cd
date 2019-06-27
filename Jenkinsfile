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
        sh 'echo git'
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
#docker-compose down
#docker-compose rm -sf
'''
            }

            junit 'flask-app/junit-report/report.xml'
            sh 'sudo rm -rf flask-app/junit-report'
          }
        }
        stage('Parralle Stage') {
          steps {
            retry(count: 5) {
              timeout(time: 10) {
                sh 'sleep $((RANDOM % 20))'
              }

            }

          }
        }
      }
    }
    stage('Run App') {
      steps {
        dir(path: 'flask-app') {
          sh '''#!/bin/bash
#docker-compose up -d
echo "RUN APP"
'''
        }

      }
    }
  }
}