pipeline {
  agent {
    node {
      label 'master'
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
  }
}