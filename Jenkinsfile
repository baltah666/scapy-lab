pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python3.9 arp6.py'
      }
    }
  }
}
