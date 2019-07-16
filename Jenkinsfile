pipeline {
  agent {
    node {
      label 'slave1_label'
    }

  }
  stages {
    stage('Echo Text (Prepare)') {
      steps {
        sh '''echo "Heydee"
sudo rm -rf flask-app/junit-report'''
      }
    }
    stage('git checkout') {
      steps {
        git(url: 'https://github.com/yshpyluk/ci_cd', branch: 'master', credentialsId: 'dea8cf38-2982-452d-b2be-bcd63af9e207')
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

      }
    }
    stage('Archive JUnit') {
      steps {
        junit 'flask-app/junit-report/report.xml'
      }
    }
    stage('Cleanup') {
      steps {
        sh 'sudo rm -rf flask-app/junit-report'
      }
    }
  }
}