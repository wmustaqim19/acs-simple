pipeline {
  agent { label 'docker-apps2' }

  stages {

    stage('Build') {
      steps {
        sh "docker build -t acs-simple:${BRANCH_NAME} ."
      }
    }

    stage('Deploy STAGING') {
      when { branch 'staging' }
      steps {
        sh "chmod +x deploy-staging.sh"
        sh "./deploy-staging.sh"
      }
    }

    stage('Approval PROD') {
      when { branch 'main' }
      steps {
        input message: 'Deploy to PRODUCTION?'
      }
    }

    stage('Deploy PROD') {
      when { branch 'main' }
      steps {
        sh "chmod +x deploy-prod.sh"
        sh "./deploy-prod.sh"
      }
    }
  }
}
