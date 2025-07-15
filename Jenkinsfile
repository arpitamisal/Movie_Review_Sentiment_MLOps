pipeline {
  agent any
  stages {
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t sentiment-api .'
      }
    }
    stage('Train Model') {
      steps {
        sh 'python train.py'
      }
    }
    stage('Deploy API') {
      steps {
        sh 'docker run -d -p 5000:5000 sentiment-api'
      }
    }
  }
  post {
    success {
      echo '✅ Build and deployment successful!'
    }
    failure {
      echo '❌ Build failed. Check the console output.'
    }
  }
}
