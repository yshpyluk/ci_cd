pipeline {
  agent {
    node {
      label 'slave1_label'
    }

  }
  stages {
    stage('Echo Text') {
      steps {
        sh 'echo "Heydee"'
      }
    }
    stage('git checkout') {
      steps {
        git(url: 'https://github.com/yshpyluk/ci_cd', branch: 'master', credentialsId: 'dea8cf38-2982-452d-b2be-bcd63af9e207')
      }
    }
    stage('Run app') {
      steps {
        dir(path: 'flask-app') {
          sh 'docker-compose up -d --build'
        }

      }
    }
    stage('Run Tests') {
      steps {
        dir(path: 'flask-app') {
          sh '''docker-compose down
docker-compose build flask-app
docker-compose run flask-app pytest -v --junit-xml=/var/opt/junit-report/report.xml
docker-compose down'''
        }

        junit 'flask-app/junit-report/report.xml'
        sh 'sudo rm -rf flask-app/junit-report'
      }
    }
  }
}